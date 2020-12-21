#!/bin/bash

# Instructions - https://github.com/ml5js/training-charRNN
# These are the hyperparameters you can change to fit your data
# input.txt contained tons of repetitions of 'pick-up-lines.txt'
# in an attempt to increase the volume of the dataset.
python train.py --data_path=./input.txt \
--rnn_size 64 \
--num_layers 2 \
--seq_length 64 \
--batch_size 32 \
--output_keep_prob 0.75 \
--num_epochs 16 \
--save_checkpoints ./checkpoints \
--save_model ./models
