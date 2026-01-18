
from typing import TypedDict, List

class TravelState(TypedDict):
    user_input: str
    destination: str
    budget: int
    days: int
    interests: List[str]
    itinerary: str
    feedback: str
