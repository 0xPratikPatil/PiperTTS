#!/bin/bash

python3 -m piper_train.preprocess \
  --language en-us \
  --input-dir Jarvis \
  --output-dir Jarvis-training \
  --dataset-format ljspeech \
  --single-speaker \
  --sample-rate 22050