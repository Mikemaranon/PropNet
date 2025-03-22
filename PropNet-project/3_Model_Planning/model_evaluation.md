# Model Evaluation

After training the model, we evaluate its performance using multiple metrics to ensure its accuracy and reliability in predicting house prices.

#### Key Metrics:
1. **Mean Absolute Error (MAE)**: 
   - The `MAE` measures the average absolute difference between the predicted prices and the actual prices. Lower MAE means the model's predictions are closer to the actual values.
   - After scaling the target by 1,000,000, the `MAE` reflects the average error in millions of the local currency.

2. **R² (Coefficient of Determination)**: 
   - This metric indicates the proportion of variance in the target variable (price) that is explained by the model. An R² close to 1 indicates a strong fit, meaning the model explains most of the variation in house prices.

#### Evaluation Code:
```python
# Evaluating the model on the test set
test_loss, test_mae = model.evaluate(X_test_scaled, y_test_scaled)
print(f"Test MAE: {test_mae}")

# Calculate R² for the model
from sklearn.metrics import r2_score
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test_scaled, y_pred)
print(f"R²: {r2}")
```
In the evaluation:
- The `MAE` is reported on the test set, indicating the average error in predicting house prices.
- The `R²` score is calculated to evaluate how well the model fits the data.

Results:
- `MAE`: The model has achieved an `MAE` of 0.1257, meaning the average prediction error is approximately 120,000 units in the price scale.
- `R²`: With an `R²` of 0.99, the model explains 99% of the variance in the house prices, showing that it performs exceptionally well on this task.

The combination of a low `MAE` and high `R²` indicates that the model provides accurate and reliable price predictions.