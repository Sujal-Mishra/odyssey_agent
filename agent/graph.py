
from langgraph.graph import StateGraph
from agent.state import TravelState
from agent.nodes import parse_input, budget_check, plan_attractions, finalize_itinerary

builder = StateGraph(TravelState)
builder.add_node("parse", parse_input)
builder.add_node("budget", budget_check)
builder.add_node("attractions", plan_attractions)
builder.add_node("final", finalize_itinerary)

builder.set_entry_point("parse")
builder.add_edge("parse", "budget")
builder.add_edge("budget", "attractions")
builder.add_edge("attractions", "final")

travel_graph = builder.compile()
