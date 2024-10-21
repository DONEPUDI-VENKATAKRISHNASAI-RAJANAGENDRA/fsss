# MNIST Classification with Feedforward Neural Network (FNN)

This project implements a Feedforward Neural Network (FNN) for classifying MNIST handwritten digits. The network includes a Batch Normalization layer and a Dropout layer to improve the performance and prevent overfitting. The model is trained using the PyTorch framework and saved as a .pkl file for further use.

## Dataset

The [MNIST dataset](http://yann.lecun.com/exdb/mnist/) is a collection of 70,000 grayscale images of handwritten digits (0-9), where each image is of size 28x28 pixels. It consists of:

- 60,000 training images
- 10,000 testing images

## Project Structure

- main.py: Contains the FNN model, training, and evaluation code.
- sumapran_ass_1_part_4_2_model.pkl: The saved state of the trained model.
- README.md: This documentation file.
- requirements.txt: Lists required dependencies to run the project.
- data/: Directory where MNIST data is downloaded.

## Model Architecture

The FNN consists of the following layers:

1. *Fully Connected Layer (fc1)*: Input size 28x28, 128 units
2. *Batch Normalization (bn1)*: Normalizes the output of fc1
3. *Dropout*: Randomly drops 50% of units to prevent overfitting
4. *Fully Connected Layer (fc2)*: 128 units to 64 units
5. *Fully Connected Layer (fc3)*: 64 units to 10 units (number of classes)

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YourGitHubUsername/MNIST-FNN.git
cd MNIST-FNN
