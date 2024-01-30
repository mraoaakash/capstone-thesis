import os
import pandas as pd 
import numpy as np
import shutil
import matplotlib.pyplot as plt
from matplotlib import rc 
import argparse
import cv2
from math import sqrt


rc('font',**{'family':'serif','serif':['Times New Roman']})

def image_df(dir):
    """
    Creates a dataframe with the image names and their corresponding labels.
    """
    print('----------------------')
    print('Generating Data Frame')
    print('----------------------')

    image_list = os.listdir(dir)
    image_list.sort()
    try:
        image_list.remove('.DS_Store')
    except:
        pass

    image_list_path = [os.path.join(dir, image) for image in image_list]

    image_df = pd.DataFrame({'image_path': image_list_path, 'image_name': image_list})

    print('Generated Data Frame')
    print('---------------------')

    return image_df

def pick_images(df, n, seed):
    """
    Randomly picks n images from the dataframe.
    """
    print('---------------------')
    print('Picking Random Images')
    print('---------------------')

    np.random.seed(seed)
    df = df.sample(n=n)

    print('Picked Random Images')
    print('--------------------')
    return df

def move_images(df,out_dir):
    """
    Moves the images from the dataframe to the output directory.
    """
    print('--------------------')
    print('Moving Picked Images')
    print('--------------------')
    out_dir = os.path.join(out_dir, 'picked_images')
    os.makedirs(out_dir, exist_ok=True)
    for index, row in df.iterrows():
        shutil.copy(row['image_path'], out_dir)
    
    new_paths = [os.path.join(out_dir, image) for image in df['image_name']]
    new_df = pd.DataFrame({'image_path': new_paths, 'image_name': df['image_name']})
    print('Moved Picked Images')
    print('-------------------')

    return new_df

def plot_image_grid(df, n, i, seed, out_dir):
    """
    Plots a grid of images.
    """
    df_cpy = df.copy()
    df_cpy.reset_index(inplace=True)


    print('-------------------')
    print('Plotting Image Grid')
    print('-------------------')

    out_dir = os.path.join(out_dir, 'image_grid')
    os.makedirs(out_dir, exist_ok=True)

    fig, ax = plt.subplots(int(sqrt(n)), int(sqrt(n)), figsize=(i*3, i*3))
    np.random.seed(seed)
    for i in range(int(sqrt(n))):
        for j in range(int(sqrt(n))):
            index = np.random.randint(0, n)
            img = cv2.imread(df_cpy['image_path'][index])
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ax[i,j].imshow(img)
            ax[i,j].axis('off')
            ax[i,j].set_title(df_cpy['image_name'][index])
    
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'image_grid.png'))


def norm_func(df, method="reinhard"):
    pass

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--input_dir', type=str, default='data/processed_images')
    argparse.add_argument('--output_dir', type=str, default='data/picked_images')
    argparse.add_argument('--n', type=int, default=10)
    argparse.add_argument('--i', type=int, default=5)
    argparse.add_argument('--seed', type=int, default=42)
    args = argparse.parse_args()

    df = image_df(args.input_dir)
    print(df.head())
    df = pick_images(df, args.n, args.seed)
    new_df = move_images(df, args.output_dir)
    plot_image_grid(df, args.n, args.i, args.seed, args.output_dir)
