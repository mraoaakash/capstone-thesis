import os
import pandas as pd 
import numpy as np
import shutil
import matplotlib.pyplot as plt
from matplotlib import rc 
import argparse


rc('font',**{'family':'serif','serif':['Times New Roman']})

def image_df(dir):
    """
    Creates a dataframe with the image names and their corresponding labels.
    """
    image_list = os.listdir(dir)
    image_list.sort()
    try:
        image_list.remove('.DS_Store')
    except:
        pass

    image_list_path = [os.path.join(dir, image) for image in image_list]

    image_df = pd.DataFrame({'image_path': image_list_path, 'image_name': image_list})

    return image_df

def pick_images(df, n, seed):
    """
    Randomly picks n images from the dataframe.
    """
    np.random.seed(seed)
    df = df.sample(n=n)

    return df

def move_images(df,out_dir):
    """
    Moves the images from the dataframe to the output directory.
    """
    os.makedirs(out_dir, exist_ok=True)
    for index, row in df.iterrows():
        shutil.copy(row['image_path'], out_dir)
    
    new_paths = [os.path.join(out_dir, image) for image in df['image_name']]
    new_df = pd.DataFrame({'image_path': new_paths, 'image_name': df['image_name']})
    return new_df

def plot_image_grid(df, n, i, seed, out_dir):
    """
    Plots a grid of images.
    """

    for index, row in df.iterrows():
        if index == i:
            image = plt.imread(row['image_path'])
            plt.imshow(image)
            plt.axis('off')
            plt.savefig(os.path.join(out_dir, 'picked_image.png'), bbox_inches='tight')
            # plt.show()
            break

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
