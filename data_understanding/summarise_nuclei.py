import argparse
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math


def summarise(df,save_path):
    os.makedirs(save_path, exist_ok=True)

    df = pd.read_csv(os.path.join(df, 'master','master.csv'))
    classes = ['Stromal (Non-TIL)','sTIL','Any Tumor','Other']
    data_classes = df['label'].value_counts()
    # mapping the classes to the correct names
    data_classes.index = classes
    data_classes = data_classes.sort_index()
    data_classes = data_classes.to_frame()
    data_classes['count'] = np.array(data_classes['count'])/1000
    print(data_classes)

    plt.figure(figsize=(5,5))
    plt.bar(data_classes.index, data_classes['count'])
    plt.xticks(rotation=45)
    plt.xlabel('Classes', fontsize=14, fontweight='bold')
    plt.ylabel('Number of images (1000s)', fontsize=14, fontweight='bold')
    plt.title('Number of images per class', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(args.output, 'class_distribution.png'), dpi=300)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Summarise the nuclei dataset')
    parser.add_argument('-i', '--input', type=str, help='Path to the csv file')
    parser.add_argument('-o', '--output', type=str, help='Path to the output folder')
    args = parser.parse_args()
    summarise(args.input, args.output)
                    