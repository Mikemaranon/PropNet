# Model Definition

This model is defined as a **regression model** designed to predict the price of houses based on various input features. The model takes input data, processes it through multiple layers, and outputs a single prediction—the estimated house price.

#### Data Preprocessing:
Before training, the data is preprocessed to ensure better performance and faster convergence:
- **StandardScaler** is used to normalize the input features to have zero mean and unit variance.
- The target variable, `price`, is divided by 1,000,000 to scale the prices down and make the model training more stable.

#### Model Compilation:
The model is compiled with the following settings:
- **Optimizer**: `Adam`, a commonly used optimizer that adapts the learning rate during training.
- **Loss Function**: `Mean Squared Error (MSE)`, appropriate for regression tasks.
- **Metrics**: `Mean Absolute Error (MAE)`, used to evaluate the average absolute difference between predicted and actual prices.

#### Code for Data Preprocessing:
```python
# Normalizing the features and target
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

# Scaling the target (price)
y_scaled = y / 1_000_000
```
#### Model training:
```python
# Training the model on the preprocessed data
history = model.fit(X_scaled, y_scaled, epochs=100, batch_size=32, validation_split=0.2)
```
The model is trained for `100 epochs` with a batch size of `32`, which allows it to learn the relationships between features and the price effectively.

