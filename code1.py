import pandas as pd
import streamlit as st

# Load product data
data = pd.DataFrame({
    "Product": ["TMP 4.3 EO", "Product B", "Product C"],
    "Chain Starter MW": [134.173, 150.200, 140.500],
    "Oxide MW": [44.0524, 50.000, 45.000],
    "Target OH Value": [520.0892, 500.000, 530.000],
    "Growth Ratio": [2.41, 2.30, 2.50],
    "Catalyst %": [0.02, 0.015, 0.025],
    "Reaction Temp": [165, 160, 170]
})

def calculate(product_name, custom_params=None):
    # Fetch product details
    product = data[data["Product"] == product_name].iloc[0]

    # Extract parameters
    chain_starter_mw = product["Chain Starter MW"]
    oxide_mw = product["Oxide MW"]
    target_oh_value = product["Target OH Value"]
    growth_ratio = custom_params.get("growth_ratio", product["Growth Ratio"])
    catalyst_percent = product["Catalyst %"]
    reaction_temp = product["Reaction Temp"]

    # Perform calculations
    chain_starter_qty = 15000 / (1 + growth_ratio)  # Example
    oxide_qty = 15000 - chain_starter_qty  # Example
    catalyst_qty = (catalyst_percent / 100) * 15000

    # Return results
    results = {
        "Chain Starter MW": chain_starter_mw,
        "Oxide MW": oxide_mw,
        "Target OH Value": target_oh_value,
        "Growth Ratio": growth_ratio,
        "Chain Starter Qty (kg)": round(chain_starter_qty, 2),
        "Oxide Qty (kg)": round(oxide_qty, 2),
        "Catalyst Qty (kg)": round(catalyst_qty, 2),
        "Reaction Temp (°C)": reaction_temp,
    }
    return results

# Streamlit App
st.title("Polymer Recipe Calculator")

# Product Selection
product_name = st.selectbox("Select a Product", data["Product"])

# Optional User Inputs
st.sidebar.header("Custom Parameters")
custom_growth_ratio = st.sidebar.number_input("Growth Ratio", value=2.41, step=0.01)
custom_target_oh = st.sidebar.number_input("Target OH Value", value=520.0892, step=1.0)

# Calculate Button
if st.button("Calculate"):
    # Perform calculations
    custom_params = {"growth_ratio": custom_growth_ratio, "target_oh": custom_target_oh}
    results = calculate(product_name, custom_params)

    # Display Results
    st.subheader("Calculation Results")
    st.write(results)

    # Visualize Results
    st.subheader("Visualization")
    st.bar_chart([results["Chain Starter Qty (kg)"], results["Oxide Qty (kg)"]])