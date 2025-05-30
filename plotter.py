import csv
import matplotlib.pyplot as plt 
import numpy as np

gtlogits = []
with open('out.example_images.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for i,row in enumerate(reader):
        logit = float(row[1])
        gtlogits.append(logit)

ground_truth = [round(logit) for logit in gtlogits]

files = ['out.gblurred_images.csv','out.downsamphalf_images.csv','out.warped_images.csv','out.example_images.csv','out.rotated_images.csv','out.rotated_images225.csv','out.rotated_warped_images225.csv']
filenames = ['gblurred_error.png','downsampled_error.png','yang_warped.png','example_imageserror.png','rotated_45error.png','rotated_225error.png','rotate_and_warped225error.png']
titles = ['Gaussian Blurred','Downsampled by 2','Pure Identity Transform','Original','Rotated 45', 'Rotated 225', 'Rotated 225 + Identity Transform']
for j in range(len(files)):
    logits = []
    with open(files[j], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i,row in enumerate(reader):
            logit = float(row[1])
            logits.append(logit)

    error = []
    cnt = 0
    for i in range(len(ground_truth)):
        if cnt % 2 == 0:
            error.append(abs(ground_truth[i]-logits[i]))
        cnt+=1
    cum_error = np.cumsum(error)    
    length = np.arange(1, len(cum_error)+1)
    plt.plot(length,cum_error)
    plt.scatter(length[-1], cum_error[-1], color='red')  # Mark the final point
    plt.annotate(f'Total Cumulative Error: {cum_error[-1]:.2f}', (length[-1], cum_error[-1]), 
                 textcoords="offset points", xytext=(-80,0), ha='center', color='black')
    plt.xlabel('Image')
    plt.ylabel('Cumulative error')
    plt.title(f'Cumulative Prediction Error for {titles[j]} Images')
    plt.savefig(f'figures/{filenames[j]}')
    plt.show()

    


