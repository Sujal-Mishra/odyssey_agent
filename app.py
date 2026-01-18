
import streamlit as st
from agent.graph import travel_graph

st.title("🧭 AI Travel Planning Agent")

user_input = st.text_input("Describe your trip:")

if st.button("Generate Itinerary"):
    state = {
        "user_input": user_input,
        "destination": "",
        "budget": 0,
        "days": 0,
        "interests": [],
        "itinerary": "",
        "feedback": ""
    }
    result = travel_graph.invoke(state)
    st.subheader("Your Travel Itinerary")
    st.write(result["itinerary"])
