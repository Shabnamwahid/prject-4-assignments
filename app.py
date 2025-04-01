import streamlit as st

# Display the title
st.title("🏋️ BMI Calculator")

# Input field for weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=1.0)

# Input field for height in meters
height = st.number_input("Enter your height (meters):", min_value=0.5)

# Button to trigger BMI calculation
if st.button("Calculate BMI"):
    if height > 0:
        # Calculate BMI
        bmi = weight / (height ** 2)
        st.write(f"### Your BMI is: {bmi:.2f}")

        # Provide interpretation based on BMI value
        if bmi < 18.5:
            st.write("**You are underweight.**")
        elif 18.5 <= bmi < 24.9:
            st.write("**You have a normal weight.**")
        elif 25 <= bmi < 29.9:
            st.write("**You are overweight.**")
        else:
            st.write("**You are obese.**")
    else:
        st.error("Height must be greater than zero.")

