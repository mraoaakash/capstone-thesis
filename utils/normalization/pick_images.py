import os
import pandas as pd 
import numpy as np
import shutil
import matplotlib.pyplot as plt
from matplotlib import rc 


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
    for index, row in df.iterrows():
        shutil.copy(row['image_path'], out_dir)
    
    new_paths = [os.path.join(out_dir, image) for image in df['image_name']]
    new_df = pd.DataFrame({'image_path': new_paths, 'image_name': df['image_name']})
    return new_df

def plot_image_grid(df, n, i, seed, out_dir):
    """
    Plots a grid of images.
    """

    fig, ax = plt.subplots(nrows=n//i, ncols=i, figsize=(10,10))
    np.random.seed(seed)
    for row in ax:
        for col in row:
            image = df.sample(n=1)
            col.imshow(plt.imread(image['image_path'].values[0]))
            col.axis('off')
            col.set_title(image['image_name'].values[0], fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'image_grid.png'), dpi=300)