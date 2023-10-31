import langchain_helper as lch
import streamlit as st

st.title("Pet names")

animal_type = st.sidebar.selectbox("What is your pet?",("Cat", "Dog", "Cow", "Hamster"))

if animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What color is your Cat?",max_chars=15)

if animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What color is your Dog?",max_chars=15)

if animal_type == "Cow":
    pet_color = st.sidebar.text_area(label="What color is your Cow?",max_chars=15)

if animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What color is your Hamster?",max_chars=15)


if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response['pet_name'])
