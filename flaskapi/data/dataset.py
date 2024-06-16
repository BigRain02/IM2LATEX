from torch.utils.data import DataLoader, Dataset
import pandas as pd
import torch
import torchvision
from torchvision import transforms as tvt
import math
import os



class LatexPredictDataset(Dataset):
    def __init__(self, predict_img_path: str):
        super().__init__()
        if predict_img_path:
            assert os.path.exists(predict_img_path), "Image not found"
            self.walker = [predict_img_path]
        else:
            self.walker = []
        self.transform = tvt.Compose([tvt.Normalize((0.5), (0.5)),])

    def __len__(self):
        return len(self.walker)

    def __getitem__(self, idx):
        img_path = self.walker[idx]

        image = torchvision.io.read_image(img_path)
        image = image.to(dtype=torch.float)
        image /= image.max()
        image = self.transform(image)  # transform image to [-1, 1]

        return image
