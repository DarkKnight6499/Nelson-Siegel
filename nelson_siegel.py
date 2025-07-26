import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit    
    
df= pd.read_csv('india_bond.csv')
maturities = df['Maturity'].values
yields = df['Yield'].values


def nelson_siegel(x, beta0, beta1, beta2, tau):
    term1 = beta0
    term2   = beta1 * (1 - np.exp(-x / tau)) / (x / tau)
    term3 = beta2 * ((1 - np.exp(-x / tau)) / (x / tau) - np.exp(-x / tau))
    return term1 + term2 + term3


initial_guess = [7, -2, 1, 2]
params, _ = curve_fit(nelson_siegel, maturities, yields, p0=initial_guess)

beta0, beta1, beta2, tau = params
print(f"β₀ (level): {beta0:.2f}")
print(f"β₁ (slope): {beta1:.2f}")
print(f"β₂ (curvature): {beta2:.6f}")
print(f"τ (decay): {tau:.2f}")

x_fit = np.linspace(min(maturities), max(maturities), 100)
y_fit = nelson_siegel(x_fit, *params)


plt.figure(figsize=(10, 6))
plt.plot(maturities, yields, 'o', label='Observed yields')
plt.plot(x_fit, y_fit, '-', label='Nelson-Siegel fit', color='green')
plt.xlabel("Maturity (Years)")
plt.ylabel("Yield (%)")
plt.title("Yield Curve Fit - Nelson-Siegel Model")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
