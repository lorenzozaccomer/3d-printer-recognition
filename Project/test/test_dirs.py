
import os
import torchvision
from torchvision import datasets

path = 'D:\\repositories\\3d-printer-recognition\\Images'

# Return the folders on Image folder
def test__ReturnImageFolderFromPath(path):
    return os.listdir(path)



# Test image list
def test__ImageList(path):
    folder_list = []
    for f in os.listdir(path):
        folder_list.append(os.path.join(path,f))
    return folder_list

# Return the paths from primary folder
def test__FoldersOnImageList(path):
    return list((os.path.join(path,f) for f in os.listdir(path)))



def test__create_datasets(path):
    return {x: datasets.ImageFolder(os.path.join(path, x))
                  for x in ['train', 'valid']}


def test__dim_datasets(path):
    return {x: len(image_datasets[x]) for x in ['train', 'valid']}

# show the folder inside Images folder
images_folder = test__ReturnImageFolderFromPath(path)
print(images_folder)

# lists the folders on Image folder
list_path_folders = test__FoldersOnImageList(path)
print(list_path_folders)

# create image dataset
image_datasets = test__create_datasets(path)
print(image_datasets)

#return size of datasets
dim_datasets = test__dim_datasets(path)
print(dim_datasets)