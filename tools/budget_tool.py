
from langchain.tools import tool

@tool
def estimate_budget(destination: str, days: int) -> str:
    return f"Estimated budget for {days} days in {destination} is ₹{days * 3000}"
