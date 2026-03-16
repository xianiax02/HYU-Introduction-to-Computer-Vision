# Violence Video Detection

Computer vision project for detecting violent situations in CCTV videos.

## Overview

This project approaches violence detection as a video understanding problem where motion matters as much as appearance.  
To reflect this, the model uses both RGB frames and optical flow instead of relying on RGB alone.

## Key Idea

- Extract dense motion information with Farneback optical flow
- Build 5-channel video inputs with `RGB 3 + Flow 2`
- Apply a Two-Stream architecture for appearance and motion
- Improve the baseline 3D CNN with an EfficientNet-B0 based fusion model

## Result

- Baseline FusionModel: `Accuracy 70.0%`, `AUROC 0.860`
- EfficientFusionModel: `Accuracy 85.0%`, `AUROC 0.968`

## Files

- [optical_flow .ipynb](./optical_flow%20.ipynb): Lucas-Kanade optical flow implementation from scratch
- [train_v3_efficientnet.ipynb](./train_v3_efficientnet.ipynb): EfficientNet-B0 based two-stream fusion model

## Tech Stack

`Python` `PyTorch` `OpenCV` `NumPy` `Google Colab` `Weights & Biases`
