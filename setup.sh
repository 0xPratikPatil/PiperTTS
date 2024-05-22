#!/bin/bash

apt update	-y
apt install -y software-properties-common
apt install -y add-apt-repository
add-apt-repository ppa:deadsnakes/ppa -y
apt update	-y
apt install -y python3.10-full python3.10-dev build-essential python3-dev espeak-ng
python3.10 -m  venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade wheel setuptools
pip install -r requirements.txt
pip install -e .
bash build_monotonic_align.sh
wget https://huggingface.co/datasets/rhasspy/piper-checkpoints/resolve/main/en/en_US/ljspeech/high/ljspeech-2000.ckpt?download=true -O ljspeech-2000.ckpt
bash Preprocessing.sh
bash train.sh
