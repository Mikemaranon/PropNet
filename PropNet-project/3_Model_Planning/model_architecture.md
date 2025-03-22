# Model Architecture

The housing price prediction model uses a **neural network** architecture to predict housing prices based on several features such as the number of bedrooms, area, parking availability, and more. The model architecture is designed to handle continuous numerical data and output a single continuous value, which in this case is the **price of a house**.

#### Key Components:
- **Input Layer**: The model receives multiple features related to housing data (e.g., area, number of bedrooms, etc.) as input.
- **Hidden Layers**: The model consists of dense hidden layers with **ReLU activation**. ReLU helps to introduce non-linearity and prevent issues like vanishing gradients.
- **Output Layer**: A single neuron outputs the predicted price, with a **linear activation function** since the problem is a regression task.

The architecture is simple yet effective for predicting prices due to the model's ability to learn complex relationships in the data.

#### Code for Model Architecture:
```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.InputLayer(input_shape=(X_train_scaled.shape[1],)),  # Input layer
    layers.Dense(64, activation='relu'),  # Hidden layer with 64 neurons
    layers.Dense(32, activation='relu'),  # Another hidden layer
    layers.Dense(1)  # Output layer, single value for price prediction
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```
In the above code, the model is built with:
- Two hidden layers: with `64 and 32 neurons` respectively, using ReLU activation.
- Output layer: A single neuron that outputs the predicted price.