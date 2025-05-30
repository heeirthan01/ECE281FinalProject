import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def sort_dataframe_by_name(images: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the DataFrame by the 'name' column.
    """
    return images.sort_values(by='filename').reset_index(drop=True)

def remove_repeated_images(images: pd.DataFrame) -> pd.DataFrame:
    """
    Removes repeated images from the DataFrame.
    """
    return images.drop_duplicates(subset='filename').reset_index(drop=True)
    
def process_dataframe(images: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the DataFrame by removing repeated images and sorting by name.
    """
    images = remove_repeated_images(images)
    images = sort_dataframe_by_name(images)
    return images

def plot_images_with_gt(gt: pd.DataFrame, df_list, process_type_list) -> None:
    """
    Plots the images with their ground truth labels.
    """

    # image_name = [ img[img.rfind("\\"):] for img in gt['filename'].to_list()]
    image_name = range(gt.shape[0])
    process_type_list = [process_type.split('.')[1] for process_type in process_type_list]
        
    
    gt_logit = gt['logit'].to_list()

    _, ax = plt.subplots()
    ax.scatter(image_name, gt_logit, label='Ground Truth Logit', color='red', alpha=0.6)
    for i in range(len(df_list)):
        logit = df_list[i]['logit'].to_list()
        ax.scatter(image_name, logit, label=process_type_list[i], alpha=0.6)
    ax.set_xlabel('Images')
    ax.set_ylabel('Logit Value')
    ax.set_title('Comparison of Warped Images and Ground Truth Logits')
    ax.legend()

csv_list = ['out.warped_images.csv','out.rotated_images.csv','out.rotated_images225.csv','out.rotated_warped_images225.csv', 'out.downsamphalf_images.csv', 'out.downsamphalf_images.csv']
ground_truth = pd.read_csv('out.example_images.csv')
ground_truth = process_dataframe(ground_truth)
ground_truth['logit'] = ground_truth['logit'].round()

df_list = []

for csv_file in csv_list:
    df = pd.read_csv(csv_file)
    df = process_dataframe(df)
    df_list.append(df)
print(len(df_list))
plot_images_with_gt(ground_truth, df_list, csv_list)
plt.show()
