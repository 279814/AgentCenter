import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from BaseAgent import BaseAgent
from tianji import router_agent

# 智能体id 与 对应的智能体实例
AGENTS: dict[int, BaseAgent] = {
    router_agent.id(): router_agent,  # 1001
}