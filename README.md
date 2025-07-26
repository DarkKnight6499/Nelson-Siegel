# Nelson-Siegel Yield Curve Fitting — India Bond Market

This project implements the Nelson-Siegel yield curve model to fit real-world government bond yield data from the Indian market. The goal is to estimate the term structure of interest rates using a well-established parametric model, commonly applied in fixed income analysis, monetary policy research, and quantitative finance.

## What is the Nelson-Siegel Model?

The Nelson-Siegel model expresses the yield to maturity as a function of time (x) using four parameters:

y(x) = β0 + β1 * [(1 - exp(-x/τ)) / (x/τ)] + β2 * [(1 - exp(-x/τ)) / (x/τ) - exp(-x/τ)]

Where:
- β0 (level): Long-term interest rate
- β1 (slope): Short-term component
- β2 (curvature): Medium-term hump
- τ (tau): Controls the exponential decay or how quickly the curve changes shape