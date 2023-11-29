import streamlit as st
import info

def start():
    st.title(info.title)
    st.write("I can convert between 12 hour time and 24 hour time!")
    st.write("---")
start()
name = st.text_input("What is your first name?") #NEW


def function():
    timeType = st.radio(f"{name}, do you want to convert your time to 12 or 24 hour time?",["24-hour time","12-hour time"])#NEW
    if timeType == "24-hour time":
        st.image(info.image24,width = 500)
        hour = st.number_input("Select the hour(s):",min_value=1,max_value=12,value=6,step=1) #NEW
        minute = st.number_input("Select the minute(s):",min_value=0,max_value=59,value=0,step=1)
        amPm = st.radio("Is that time in AM or PM?",["a.m.","p.m."])
        newmin = ""
        
        if minute < 10:
            newmin = f"0{minute}"
        else:
            newmin = minute

        if amPm != "p.m.":
            newhour = hour
            st.write(f"{name}, your time in 12 hour time to 24 hour time is **{newhour}:{newmin}.**")
        else:
            if hour == 12:
                newhour = hour
            else:
                newhour = hour + 12
            st.write(f"{name}, your time in 12 hour time to 24 hour time is **{newhour}:{newmin}.**")
    else:
        st.image(info.image12, width = 500)
        hour = st.number_input("Select the hour(s):",min_value=0,max_value=23,value=12,step=1)
        minute = st.number_input("Select the minute(s):",min_value=0,max_value=59,value=0,step=1)
        newmin = ""
        if minute < 10:
            newmin = f"0{minute}"
        else:
            newmin = minute
        
        if hour < 13 and hour > 0:
            newhour = hour
            st.write(f"{name}, your time in 24 hour time to 12 hour time is **{newhour}:{newmin} a.m.**")
        elif hour == 0:
            st.write(f"{name}, your time in 24 hour time to 12 hour time is **12:{newmin} a.m.**")
        else:
            newhour = hour-12
            st.write(f"{name}, your time in 24 hour time to 12 hour time is **{newhour}:{newmin} p.m.**")

    
if name != "":
    function()
