from torch.utils.data import Dataset
import os
from PIL import Image


class MyDataset(Dataset):
    def __init__(self, root_dir, label_dir):
        # 如何理解self，从理论上、从用处上。  从用处上——一个函数里面的变量另外的函数用不了，加上self之后，其他的函数也可以用了
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.dir_path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.dir_path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        item_path = os.path.join(self.dir_path, img_name)
        img = Image.open(item_path).convert('RGB')  # Imagefile
        label = self.label_path
        return img, label

    def __len__(self):
        return len(self.img_path)


root = 'D:\Pycharm\workspace\leetcode\data'
label_dir = 'D:\Pycharm\workspace\leetcode\label'
ants_dataset = MyDataset(root, label_dir)  # ants_dataset这个实例，其属性会包含所有初始化类中的变量
ants_0 = ants_dataset[0]  # 会调用__getitem__，返回img和label
