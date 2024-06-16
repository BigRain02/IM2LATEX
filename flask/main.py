#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import torch
from torch.utils.checkpoint import checkpoint
from torch import nn, Tensor
from image2latex.model import Image2LatexModel
from data.dataset import LatexPredictDataset
from data.datamodule import DataModule
from image2latex.text import Text100k
import pytorch_lightning as pl
import argparse
import numpy as np
from torchvision import transforms as tvt

if __name__ == "__main__":
    torch.manual_seed(12)
    np.random.seed(12)

    text = Text100k()

    predict_set = LatexPredictDataset(predict_img_path='image/1a00a76d4e.png')

    dm = DataModule(
        predict_set,
        4,
        8,
        text,
    )
    # Create a Trainer instance
    trainer = pl.Trainer(
        accelerator="cpu",  # Specify CPU accelerator
        devices=1,  # Use 1 CPU core
        max_epochs=10,  # Set max number of epochs
        deterministic=True,  # Ensure deterministic behavior
    )

    model = Image2LatexModel(lr=0.001, n_class=10)
    ckpt_path = 'ckpt/Conv_BiLSTM_LSTM.ckpt'
    if ckpt_path:
        model = model.load_from_checkpoint(ckpt_path)

    print("=" * 10 + "[Predict]" + "=" * 10)
    latex = trainer.predict(datamodule=dm, model=model, ckpt_path=ckpt_path)

    print(latex[0])
