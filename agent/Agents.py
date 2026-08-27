import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from BaseAgent import BaseAgent
from tianji import router_agent, text_agent
from tja2a import tja2a_agent

# 智能体id 与 对应的智能体实例
AGENTS: dict[int, BaseAgent] = {
    router_agent.id(): router_agent,  # 1001
    text_agent.id(): text_agent,  # 1002
    tja2a_agent.id(): tja2a_agent,  # 1003
}