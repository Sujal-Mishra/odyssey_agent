
from tools.budget_tool import estimate_budget
from tools.attraction_tool import recommend_attractions

def parse_input(state):
    state["destination"] = "Paris"
    state["budget"] = 80000
    state["days"] = 5
    state["interests"] = ["culture", "food"]
    return state

def budget_check(state):
    info = estimate_budget.invoke({
        "destination": state["destination"],
        "days": state["days"]
    })
    state["itinerary"] = info
    return state

def plan_attractions(state):
    places = recommend_attractions.invoke({
        "destination": state["destination"],
        "interests": state["interests"]
    })
    state["itinerary"] += "\n" + places
    return state

def finalize_itinerary(state):
    state["itinerary"] += "\n\nDay-wise itinerary generated successfully."
    return state
