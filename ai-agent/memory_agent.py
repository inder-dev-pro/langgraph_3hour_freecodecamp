from typing import TypedDict, List, Union
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage

class AgentState(TypedDict):
    messages:List[Union[HumanMessage, AIMessage]]

load_dotenv()

llm=ChatGroq(model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

def simple_bot(state:AgentState) -> AgentState:
    """This bot will handle all the requests given by the user"""
    response=llm.invoke(state['messages'])
    print(f"{response.content}")
    return state

graph=StateGraph(AgentState)
graph.add_node("bot", simple_bot)
graph.set_entry_point("bot")
graph.set_finish_point("bot")
app=graph.compile()

conversation_history=[]

user_input=input("Enter: ")
while(user_input!="exit") :
    conversation_history.append(HumanMessage(content=user_input))
    response=app.invoke({"messages":conversation_history})
    conversation_history=response["messages"]
    user_input=input("Enter: ")

with open("logging.txt", "w") as file:
    file.write("Your chat log\n\n!")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"Human: {message.content}\n\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")

    file.write("End of the Chat\n\n")


