import streamlit as st

st.write("Want to know about my story?")
yes = st.button("Yes")
no = st.button("No")

if yes:
    content = """
    My story from when i was 3 years old from when i am 10 years old.
    i was born on 13-2-2016
    when I was 3 years old, My dad bought me the first ever cat to step in the house.
    Her name was Tillu and She was 3 months old.
    and for 1 year, nothing really happened.
    but when i turned 5 years old, Tillu was very lonely. so my dad bought another cat
    His name was Jack and when he was in the basket, his nose was dropping :).
    and then, Jack beated Tillu a lot. on that time, My Dad was in London and my Mom
    was with me. One day, i couldn't learn ABCD, My mom got so angry she was beating
    me badly and i inside the bed was saying, 'Please someone save me.'.
    and then another day, My mom said, 'If you learn ABCD, I will give you chocolate.'
    And then i learned ABCD and my mom gave me chocolate every day.
    My first school was American Academy. I gave the test and i passed.
    and then my 2nd school was My Public school. i studied there until
    1st class. and my 3rd school is Meerut Public School main wing. and i am in 
    This school right now. my dad introduced me to Javascript. it was way too hard
    and then, my dad introduced me to Scratch, which was like kids game
    But then, My dad introduced me to python on September, 2025.
    It was very easy and cool!
    and then on October 2024, A new cat entered the house.
    Her name was Rozie, and then, on december, 2024,
    4 kittens wer born. 2 of them was sold by my dad and 2 stayed in the house.
    and then on september 2024, My brother was born. and then on
    July 2025, 6 kittens were born.
    one died and they all were killed by one of the kitten born on december, 2024.
    and then, on 13-2-2026 will be my birthday!
    """
    st.success(content)
if no:
    st.write("Okay, we will not tell anything.")

