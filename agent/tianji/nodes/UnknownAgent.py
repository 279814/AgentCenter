import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RouteState import RouteState

class UnknownAgent:
    """
    未知意图智能体（兜底智能体）
    """

    async def execute(self, state: RouteState):
        pass