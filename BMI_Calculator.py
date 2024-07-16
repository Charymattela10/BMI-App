import streamlit as st

with st.form("BMI Calculator", border = False):
    col1, col2, col3 = st.columns([2,2,1])
with col1:
    weight = st.number_input("Your Weight in kgs")
with col2:
    height = st.number_input("Your Height in meters")
with col3:
    submit = st.form_submit_button('Calculate')

healthy_weights = []

if submit:

    BMI = round((weight)/(height)**2, 2)

    for i in range(1,120):
        bmi = round((i)/(height)**2, 2)
        if bmi > 18.5 and bmi<= 24.9:
            healthy_weights.append(i)
    min_weight = min(healthy_weights)
    max_weight = max(healthy_weights)

    if BMI <= 18.5:
        st.error("You're UnderWeight")
        st.write("Keep weight in between {} and {}".format(min_weight, max_weight))
    elif BMI > 18.5 and BMI <= 24.9:
        st.success("Healthy / Normal")
        st.write("Keep weight in between {} and {}".format(min_weight, max_weight))
    elif BMI > 25 and BMI <= 29.9:
        st.warning("you're Overweight")
        st.write("Keep weight in between {} and {}".format(min_weight, max_weight))
    else:
        st.error("you're Obese")
        st.write("Keep weight in between {} and {}".format(min_weight, max_weight))

