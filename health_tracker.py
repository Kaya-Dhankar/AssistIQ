import streamlit as st
from datetime import datetime, date


def calculate_age(dob):
    today = date.today()
    age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age_years

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

def calculate_calories(age, gender, weight, height_cm, activity_factor):
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
    calories = bmr * activity_factor
    return round(calories, 2)

def show_tracker():
    st.title("Smart_Health ")

    st.header("Age Calculator")
    dob = st.date_input("Select your Date of Birth",
                        min_value=date(1900, 1, 1),
                        max_value=date(2050, 12, 31))
    if st.button("Calculate Age", key="calc_age"):
        age = calculate_age(dob)
        st.success(f"Your age is: {age} years")

    st.header("BMI Calculator")
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=300.0, step=0.1)
    feet = st.number_input("Enter your height - feet", min_value=1, max_value=8, step=1)
    inches = st.number_input("Enter your height - inches", min_value=0, max_value=11, step=1)
    height_cm = (feet * 12 + inches) * 2.54  # convert total height to cm

    if st.button("Calculate BMI", key="calc_bmi"):
        bmi, category = calculate_bmi(weight, height_cm)
        st.success(f"Your BMI is {bmi} ({category})")

    st.header("Calorie Calculator")
    age_cal = st.number_input("Enter your age (years)", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    weight_cal = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=300.0, step=0.1, key='weight_cal')
    height_cal = st.number_input("Enter your height (cm)", min_value=30.0, max_value=250.0, step=0.1, key='height_cal')
    activity_level = st.selectbox("Select your activity level",
                                  ["Sedentary (little or no exercise)",
                                   "Lightly active (light exercise/sports 1-3 days/week)",
                                   "Moderately active (moderate exercise/sports 3-5 days/week)",
                                   "Very active (hard exercise/sports 6-7 days/week)",
                                   "Extra active (very hard exercise & physical job)"])
    activity_factors = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
        "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
        "Very active (hard exercise/sports 6-7 days/week)": 1.725,
        "Extra active (very hard exercise & physical job)": 1.9
    }
    if st.button("Calculate Calories", key="calc_calories"):
        cal_need = calculate_calories(age_cal, gender, weight_cal, height_cal, activity_factors[activity_level])
        st.success(f"Your estimated daily calorie need is {cal_need} calories")
