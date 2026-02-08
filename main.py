import streamlit as st

st.title("Whose Birthday is this?")
st.write("13-2-2026")

st.write("Want to know whose birthday is this? If you know, type the name. If not, click 'Yes'.")

# Input and buttons
input_name = st.text_input(label="Name...")
yes = st.button("Yes")
no = st.button("No")

# Fix: Correct name check
if yes:
    st.success("It is Yamaan Faraz's Birthday")
    st.balloons()
if no:
    st.write("Command accepted..."
             "Nothing will be told...")
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

    st.title(f"And the most important Question, which pokemon do {input_name} likes?")
    st.write("If you know, type the name in the input box and if not, click 'Yes' to know and if you do not want to tell, press 'No'.")
    input_name2 = st.text_input(label="Name...", key="name2")
    yes3 = st.button("Yes", key="yes3")
    no3 = st.button("No", key="no3")
    if input_name2 == "Pikachu":
        st.success(f"You are right! Pikachu is the most favourite pokemon of {input_name}!")
        st.balloons()
        st.image("pikachu.png", width=100)
    if yes3:
        st.write(f"Pikachu is the most favourite pokemon of {input_name}.")
        st.image("pikachu.png", width=100)
    if no3:
        st.write("Command accepted..."
             "Nothing will be told...")


