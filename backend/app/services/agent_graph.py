"""
LangGraph AI CRM Agent

User
 ↓
LLM
 ↓
CRM Tool
 ↓
Update Form
 ↓
Final AI Response
"""

import json
from typing import Annotated, TypedDict

from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

from langchain_groq import ChatGroq

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from langgraph.graph.message import add_messages
from langgraph.prebuilt import (
    ToolNode,
    tools_condition,
)

from app.core.config import settings
from app.services.prompts import SYSTEM_PROMPT
from app.services.tools import TOOLS



class CRMState(TypedDict):

    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]

    form_state: dict



llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.1,
)



llm_with_tools = llm.bind_tools(
    TOOLS
)



def assistant(state: CRMState):

    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT
        ),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [response],
        "form_state": state.get(
            "form_state",
            {}
        ),
    }



def update_form(state: CRMState):

    form_state = state.get(
        "form_state",
        {}
    )


    for message in state["messages"]:

        if not isinstance(
            message,
            ToolMessage
        ):
            continue


        content = message.content


        if isinstance(content, str):

            try:
                content = json.loads(content)

            except Exception:
                continue


        if not isinstance(content, dict):
            continue


        data = content.get(
            "data",
            {}
        )


        if not data:
            continue


        for key, value in data.items():

            if value is not None:
                form_state[key] = value



    return {
        "messages": state["messages"],
        "form_state": form_state,
    }



tool_node = ToolNode(
    TOOLS
)



workflow = StateGraph(
    CRMState
)


workflow.add_node(
    "assistant",
    assistant
)


workflow.add_node(
    "tools",
    tool_node
)


workflow.add_node(
    "update_form",
    update_form
)



workflow.add_edge(
    START,
    "assistant"
)



workflow.add_conditional_edges(
    "assistant",
    tools_condition
)



workflow.add_edge(
    "tools",
    "update_form"
)



workflow.add_edge(
    "update_form",
    END
)



memory = MemorySaver()



graph = workflow.compile(
    checkpointer=memory
)



def run_agent(
    user_message: str,
    thread_id: str,
    form_state: dict | None = None,
):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }


    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=user_message
                )
            ],
            "form_state":
                form_state or {},
        },
        config=config,
    )


    assistant_message = "Action completed successfully."


    for message in reversed(
        result["messages"]
    ):

        if isinstance(
            message,
            ToolMessage
        ):

            try:

                tool_data = json.loads(
                    message.content
                )

                assistant_message = (
                    tool_data.get(
                        "message",
                        assistant_message
                    )
                )

            except Exception:

                assistant_message = (
                    message.content
                )

            break


        if isinstance(
            message,
            AIMessage
        ) and message.content:

            assistant_message = (
                message.content
            )

            break



    return {

        "assistant_message":
            assistant_message,


        "form_state":
            result.get(
                "form_state",
                {}
            ),

    }