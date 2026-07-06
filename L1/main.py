import operator
from typing import Annotated, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt
from dotenv import load_dotenv

load_dotenv()

# --- STATE ---
class State(TypedDict):
    nlist: list[str]

 # --- NODE ---
def node_a(state: State) -> State:
    print(f"node a is receiving {state['nlist']}")
    note = "Hello World from Node a"
    return State(nlist=[note])

# --- BUILD GRAPH ---
builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_edge(START, "a")
builder.add_edge("a", END)
graph = builder.compile()   

# --- INVOKE ---
initial_state = State(nlist=["Hello Node a, how are you?"])
result = graph.invoke(initial_state)
print("Final state:", result)