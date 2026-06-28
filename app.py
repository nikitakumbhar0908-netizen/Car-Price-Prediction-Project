import streamlit as st
import pandas as pd
import pickle


df = pd.read_csv("cleaned_quikr_car.csv")


model = pickle.load(open("CarPricePredictionModel.pkl", "rb"))

st.title("🚗 Car Price Prediction")


company = st.selectbox(
    "Select Company",
    sorted(df["company"].unique())
)


car_models = sorted(df[df["company"] == company]["name"].unique())

name = st.selectbox(
    "Select Car Model",
    car_models
)


year = st.selectbox(
    "Select Manufacturing Year",
    sorted(df["year"].unique(), reverse=True)
)


kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    step=1000
)


fuel_type = st.selectbox(
    "Select Fuel Type",
    sorted(df["fuel_type"].unique())
)


if st.button("Predict Price"):
    input_data = pd.DataFrame(
        [[company, name, year, kms_driven, fuel_type]],
        columns=["company", "name", "year", "kms_driven", "fuel_type"]
    )

    prediction = model.predict(input_data)

    st.success(f"Estimated Car Price: ₹ {int(prediction[0][0]):,}")