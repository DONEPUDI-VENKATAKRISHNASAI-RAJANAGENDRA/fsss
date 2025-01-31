import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import pickle

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyperparameters
num_epochs = 5
batch_size = 64
learning_rate = 0.001

# MNIST dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

# Define the neural network model
class FNN(nn.Module):
    def _init_(self):
        super(FNN, self)._init_()
        self.fc1 = nn.Linear(28*28, 128)
        self.bn1 = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, 64)
        self.dropout = nn.Dropout(p=0.5)
        self.fc3 = nn.Linear(64, 10)
    
    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten the image
        x = torch.relu(self.bn1(self.fc1(x)))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Instantiate the model, define the loss function and the optimizer
model = FNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Function to calculate the loss
def calculate_loss(loader):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
    return total_loss / len(loader)

# Training loop
train_losses = []
test_losses = []

for epoch in range(num_epochs):
    model.train()
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Log training loss
        train_losses.append(loss.item())
        
    # Log test loss after each epoch
    test_loss = calculate_loss(test_loader)
    test_losses.append(test_loss)
    
    print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss:.4f}')

# Save the trained model as a pickle file
with open('sumapran_ass_1_part_4_2_model.pkl', 'wb') as f:
    pickle.dump(model.state_dict(), f)


# Plotting the training and test loss curves separately in one figure
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Training loss vs. training iterations
axs[0].plot(train_losses, label='Training Loss', color='blue')
axs[0].set_xlabel('Training Iterations')
axs[0].set_ylabel('Training Loss')
axs[0].set_title('Training Loss vs. Training Iterations')
axs[0].legend()

# Test loss vs. training iterations
axs[1].plot([i * len(train_loader) for i in range(num_epochs)], test_losses, label='Test Loss', color='red')
axs[1].set_xlabel('Training Iterations')
axs[1].set_ylabel('Test Loss')
axs[1].set_title('Test Loss vs. Training Iterations')
axs[1].legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()