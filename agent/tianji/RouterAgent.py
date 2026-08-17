import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, os.path.dirname(root_path))
sys.path.insert(0, model_file_path)
sys.path.insert(0, root_path)

from typing import Optional

from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.constants import START, END

from BaseAgent import *
from nodes import *
from RouteState import RouteState
from config import logger
from common import *


class RouterAgent(BaseAgent):
    """
    RouterAgent 是整个天机系统的核心路由智能体。

    负责：
    - 构建和维护 LangGraph 的推理状态图
    - 管理意图识别与路由逻辑
    - 以流式 SSE 输出最终结果
    - 持久化每个会话的状态（使用 LangGraph + Postgres Checkpointer）
    """

    # 声明用于 Graph 的所有节点智能体（节点 = 子 Agent）
    INTENT_MAPS = {
        "intent_agent": IntentAgent(),
        "recommend_agent": RecommendAgent(),
        "buy_agent": BuyAgent(),
        "consult_agent": ConsultAgent(),
        "knowledge_agent": KnowledgeAgent(),
        "unknown_agent": UnknownAgent(),
    }

    def __init__(self):
        self.graph: Optional[CompiledStateGraph] = None

    async def init(self):
        """
        初始化 RouterAgent
        """
        self.init_graph()

    # ---------------- Graph 初始化 ----------------
    def init_graph(self):
        """
        构建 RouterAgent 的状态图（LangGraph StateGraph）

        图结构：
        START → intent_agent → <条件路由> → recommend / buy / consult / knowledge / unknown → END
        """
        builder = StateGraph(RouteState)  # RouteState 用于定义 Graph 中的状态结构

        # 添加所有节点到 Graph（每个节点绑定对应智能体的 execute()）
        for name, agent in self.INTENT_MAPS.items():
            builder.add_node(name, agent.execute)

        # 设置图的起点：首先进入意图识别
        builder.add_edge(START, "intent_agent")

        # 定义意图路由函数
        def intent_router_gate(state: RouteState):
            intent = state.get("intent", "UNKNOWN")
            logger.debug(f"【IntentAgent】智能体识别到的意图：{intent}")
            return intent

        # 基于意图值进行条件跳转（INTENT_TO_AGENT 负责映射）
        builder.add_conditional_edges("intent_agent", intent_router_gate, INTENT_TO_AGENT)

        # 所有目标节点最终都结束于 END
        for target in INTENT_TO_AGENT.values():
            builder.add_edge(target, END)

        # 编译 Graph，并启用 Checkpointer
        self.graph = builder.compile()

    async def execute(self, question: str, session_id: str, user_token: str) -> AsyncIterable[str]:
        pass

    def id(self) -> int:
        """
        RouterAgent 的固定 ID。
        """
        return 1001

    async def session_detail(self, user_id: int, session_id: str) -> list:
        """暂不实现"""
        pass

    async def delete_session(self, session_id: str):
        """暂不实现"""
        pass

# 全局 RouterAgent 实例
router_agent = RouterAgent()