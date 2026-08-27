from langgraph.graph import StateGraph, MessagesState
from langgraph.constants import START, END


class A2AState(MessagesState):
    """
    自定义对话状态结构，继承自 LangGraph 的 MessagesState。
    增加意图字段，用于在各节点间传递解析后的意图。
    """
    intent: str