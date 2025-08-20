# Author: 23f1002057@ds.study.iitm.ac.in
# Marimo interactive analysis notebook

import marimo

__generated_with = "0.9.16"
app = marimo.App()


# --- Imports ---
@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


# --- Interactive controls ---
@app.cell
def __(mo):
    # Sliders for mean and std
    mean = mo.ui.slider(-10, 10, 1, value=0, label="Mean (μ)")
    std = mo.ui.slider(1, 5, 1, value=1, label="Standard Deviation (σ)")

    # Dropdown for sample size
    size = mo.ui.dropdown(
        options=[100, 500, 1000, 5000],
        value=1000,
        label="Sample Size"
    )
    return mean, std, size


# --- Data generation ---
@app.cell
def __(np, mean, std, size):
    np.random.seed(42)
    data = np.random.normal(loc=mean.value, scale=std.value, size=size.value)
    return data,


# --- Histogram plot ---
@app.cell
def __(plt, data, mean, std):
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
    ax.set_title(f"Normal Distribution (μ={mean.value}, σ={std.value})")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    plt.show()
    return fig,


# --- Stats display ---
@app.cell
def __(mo, data):
    mean_val = np.mean(data)
    std_val = np.std(data)
    mo.md(f"""
    ### 📊 Data Summary  
    - Mean: **{mean_val:.2f}**  
    - Std Dev: **{std_val:.2f}**  
    - Min: **{np.min(data):.2f}**  
    - Max: **{np.max(data):.2f}**  
    """)
    return mean_val, std_val


# --- Welcome cell ---
@app.cell
def __(mo):
    mo.md("""
    # 🎛️ Interactive Normal Distribution Explorer  
    Adjust the sliders and dropdown below to explore how the **mean (μ)**, **standard deviation (σ)**, and **sample size** affect a normal distribution.
    """)
    return


if __name__ == "__main__":
    app.run()
