import numpy as np
import matplotlib.pyplot as plt

# Monthly data (1 = Jan, 12 = Dec)
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
sales = np.array([3300, 2550, 1350, 2300, 4500, 1880, 2600, 2600, 3500, 4300, 5750, 6500]
)






# Fit a polynomial of degree 2 (quadratic)
degree = 2
coeffs = np.polyfit(months, sales, degree)

# Generate predicted sales values
months_extended = np.linspace(1, 18, 100)  # For plotting future predictions too
predicted_sales = np.polyval(coeffs, months_extended)

# Plot original data
plt.scatter(months, sales, color='blue', label='Actual Sales')

# Plot polynomial trend
plt.plot(months_extended, predicted_sales, color='green', label=f'Degree-{degree} Polynomial Fit')

# Mark future predictions (months 13 to 18)
future_months = months_extended[months_extended > 12]
future_sales = predicted_sales[months_extended > 12]
plt.plot(future_months, future_sales, 'r--', label='Future Predictions')

# Labeling
plt.title("Monthly Sales Prediction Using Polynomial Regression")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.legend()
plt.show()



