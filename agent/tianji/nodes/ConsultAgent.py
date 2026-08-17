import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RouteState import RouteState

class ConsultAgent:
    """
    课程咨询智能体
    """

    async def execute(self, state: RouteState):
        pass