import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RouteState import RouteState


class BuyAgent:
    """
    课程购买智能体
    """

    async def execute(self, state: RouteState):
        pass