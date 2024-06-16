import torch
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from torchvision import transforms as tvt


class DataModule(pl.LightningDataModule):
    def __init__(
        self,
        predict_set,
        num_workers: int = 1,
        batch_size=20,
        text=None,
    ):
        super().__init__()
        self.predict_set = predict_set
        self.batch_size = batch_size
        self.text = text
        self.num_workers = num_workers



    def predict_dataloader(self):
        return DataLoader(self.predict_set,
                          shuffle=False,
                          batch_size=self.batch_size,
                          )


    def collate_fn(self, batch):
        size = len(batch)
        formulas = [self.text.text2int(i[1]) for i in batch]
        formula_len = torch.LongTensor([i.size(-1) + 1 for i in formulas])
        formulas = pad_sequence(formulas, batch_first=True)
        sos = torch.zeros(size, 1) + self.text.word2id["<s>"]
        eos = torch.zeros(size, 1) + self.text.word2id["<e>"]
        formulas = torch.cat((sos, formulas, eos), dim=-1).to(dtype=torch.long)

        images = [i[0] for i in batch]
        max_width, max_height = 0, 0
        for img in images:
            c, h, w = img.size()
            max_width = max(max_width, w)
            max_height = max(max_height, h)

        def padding(img):
            c, h, w = img.size()
            padder = tvt.Pad((0, 0, max_width - w, max_height - h))
            return padder(img)

        images = torch.stack(list(map(padding, images))).to(dtype=torch.float)
        return images, formulas, formula_len
