import streamlit as st
import datetime

# --- APP CONFIGURATION ---
st.set_page_config(page_title="My Calorie Tracker", page_icon="🍎")
st.title("🍎 Daily Calorie Counter")

# Initialize a list in the "session state" so data doesn't disappear when the page reloads
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- INPUT SECTION ---
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    food_item = col1.text_input("What did you eat?")
    calories = col2.number_input("Calories", min_value=0, step=1)
    submit = st.form_submit_button("Add Entry")

    if submit and food_item:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.logs.append({"time": now, "item": food_item, "calories": calories})
        st.success(f"Added {food_item}!")

# --- DISPLAY SECTION ---
st.subheader("Today's Log")

if st.session_state.logs:
    total_calories = 0
    for entry in st.session_state.logs:
        st.write(f"**{entry['time']}** - {entry['item']}: {entry['calories']} kcal")
        total_calories += entry['calories']
    
    st.divider()
    st.metric(label="Total Calories Consumed", value=f"{total_calories} kcal")
    
    if st.button("Clear Log"):
        st.session_state.logs = []
        st.rerun()
else:
    st.info("No food logged yet. Start eating!")
    