import opendatasets as od
import os

def list_of_kaggle_datasets(data_url):
    """
    list_of_kaggle_datasets will download kaggle datasets from the provided URL and return a list of the paths to retrieve the files
    """
    dir_path = data_url.split('/')[-1] # Name of the folder that will be created to store the files
    list_of_files = [] # Blank list to append the paths of the files
    # Download the datasets from Kaggle
    print('Note: You need to provide your Kaggle API credentials')
    od.download(data_url)
    file_names = os.listdir(dir_path)
    # Retrieve the path for the downloaded files
    for file in file_names:
        list_of_files.append((dir_path + '/' + file))
        print('Files downloaded:')
        print(dir_path + '/' + file)
    # Return final list
    return list_of_files