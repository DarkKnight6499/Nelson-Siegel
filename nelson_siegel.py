# Importing necessary libraries
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit    

# Step 1: Load observed bond yield data from a CSV file
df = pd.read_csv('india_bond.csv')

# Extract the two main variables: 
# Maturities (in years) and Yields (in %)
maturities = df['Maturity'].values
yields = df['Yield'].values

# Step 2: Define the Nelson-Siegel yield curve function
# This function models the shape of the yield curve using 4 parameters:
# β0 = long-term rate, β1 = short-term slope, β2 = medium-term curvature, τ = decay factor
def nelson_siegel(x, beta0, beta1, beta2, tau):
    term1 = beta0
    term2 = beta1 * (1 - np.exp(-x / tau)) / (x / tau)
    term3 = beta2 * ((1 - np.exp(-x / tau)) / (x / tau) - np.exp(-x / tau))
    return term1 + term2 + term3

# Step 3: Provide an initial guess for the parameters
# These values help the curve fitting algorithm to start optimization
initial_guess = [7, -2, 1, 2]

# Step 4: Fit the Nelson-Siegel model to the actual market yield data
# curve_fit finds the best-fitting parameters that minimize the error between model and data
params, _ = curve_fit(nelson_siegel, maturities, yields, p0=initial_guess)

# Unpack the fitted parameters for clarity
beta0, beta1, beta2, tau = params

# Step 5: Print the estimated parameters with brief explanations
print(f"β₀ (level): {beta0:.2f}")        # Approximates long-term interest rate
print(f"β₁ (slope): {beta1:.2f}")        # Reflects short-term steepness
print(f"β₂ (curvature): {beta2:.6f}")    # Captures hump in mid-range
print(f"τ (decay): {tau:.2f}")           # Controls how fast curve flattens

# Step 6: Generate smooth fitted yield values across the entire maturity range
x_fit = np.linspace(min(maturities), max(maturities), 100)
y_fit = nelson_siegel(x_fit, *params)

# Step 7: Plot the observed yield curve and the fitted Nelson-Siegel model
plt.figure(figsize=(10, 6))
plt.plot(maturities, yields, 'o', label='Observed yields')           # Actual market data
plt.plot(x_fit, y_fit, '-', label='Nelson-Siegel fit', color='green') # Smooth model fit
plt.xlabel("Maturity (Years)")
plt.ylabel("Yield (%)")
plt.title("Yield Curve Fit - Nelson-Siegel Model")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()