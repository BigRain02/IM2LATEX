import torch
from torch import nn, Tensor
from .im2latex import Image2Latex
from .text import Text
import pytorch_lightning as pl
from torchaudio.functional import edit_distance
from torchtext.data.metrics import bleu_score
from evaluate import load


class Image2LatexModel(pl.LightningModule):
    def __init__(
        self,
        lr,
        n_class: int,
        enc_dim: int = 512,
        enc_type: str = "conv_row_encoder",
        emb_dim: int = 80,
        dec_dim: int = 512,
        attn_dim: int = 512,
        num_layers: int = 1,
        dropout: float = 0.1,
        bidirectional: bool = False,
        decode_type: str = "greedy",
        text: Text = None,
        beam_width: int = 5,
        sos_id: int = 1,
        eos_id: int = 2,
        log_step: int = 100,
        log_text: bool = False,
    ):
        super().__init__()
        self.model = Image2Latex(
            n_class,
            enc_dim,
            enc_type,
            emb_dim,
            dec_dim,
            attn_dim,
            num_layers,
            dropout,
            bidirectional,
            decode_type,
            text,
            beam_width,
            sos_id,
            eos_id,
        )
        self.criterion = nn.CrossEntropyLoss()
        self.lr = lr
        self.text = text
        self.max_length = 150
        self.log_step = log_step
        self.log_text = log_text
        self.exact_match = load("exact_match")
        self.save_hyperparameters()

    def forward(self, images, formulas, formula_len):
        return self.model(images, formulas, formula_len)

    def predict_step(self, batch, batch_idx):
        image = batch

        latex = self.model.decode(image, self.max_length)

        print("Predicted:", latex)

        return latex
