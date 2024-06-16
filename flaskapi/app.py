# coding: utf-8
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from image2latex.model import Image2LatexModel
from data.dataset import LatexPredictDataset
from data.datamodule import DataModule
from image2latex.text import Text100k
import pytorch_lightning as pl

app = Flask(__name__)
CORS(app)
text = Text100k()
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

@app.route("/model",methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        file.save('flask/'+secure_filename(file.filename))

        predict_set = LatexPredictDataset(predict_img_path='flask/'+secure_filename(file.filename))
        dm = DataModule(
            predict_set,
            4,
            8,
            text,
        )
        latex = trainer.predict(datamodule=dm, model=model, ckpt_path=ckpt_path)
    return jsonify(latex[0]),200

if __name__ == '__main__':
    app.run(debug=True, port=8080)

