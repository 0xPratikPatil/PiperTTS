#!/bin/bash

python3 -m piper_train \
    --dataset-dir Jarvis-training \
    --accelerator 'gpu' \
    --devices 1 \
    --batch-size 32 \
    --validation-split 0.0 \
    --num-test-examples 0 \
    --max_epochs 2500 \
    --resume_from_checkpoint ljspeech-2000.ckpt \
    --checkpoint-epochs 25 \
    --precision 32 \
    --quality high