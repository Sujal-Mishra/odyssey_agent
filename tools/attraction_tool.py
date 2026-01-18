
from langchain.tools import tool

@tool
def recommend_attractions(destination: str, interests: list) -> str:
    return f"Recommended attractions in {destination} based on interests: {interests}"
