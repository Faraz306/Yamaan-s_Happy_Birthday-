import streamlit as st

st.title("Whose Birthday is this?")
st.write("13-2-2026")

st.write("Want to know whose birthday is this? If you know, type the name. If not, click 'Yes'.")

# Input and buttons
input_name = st.text_input(label="Name...")
yes = st.button("Yes")
no = st.button("No")

# Fix: Correct name check
if input_name.strip() in ["Yamaan", "Yamaan Faraz"]:
    st.success("You are right! It is Yamaan Faraz's birthday!")
    st.balloons()

    # Ask about guests
    st.write(f"If you want to know who will come in {input_name}'s birthday, press Yes, otherwise press No.")
    yes2 = st.button("Yes", key="yes2")
    no2 = st.button("No", key="no2")

    if yes2:
        cats = ["Jack", "Pinu", "Chinu", "Cacto", "Kalia"]
        st.success(f"{', '.join(cats)} will come in {input_name}'s birthday!")
        st.balloons()
    elif no2:
        st.write("Okay, we will not tell the name.")
