from fastapi import FastAPI, Request
from starlette.responses import PlainTextResponse
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from routers import auth_router

# ========================= 创建 FastAPI 实例 =========================
app = FastAPI(
    title="Agent Center Web Server",
    description="黑马程序员智能体中心"
)


# ========================= 异常处理 =========================
def system_exception_handler(req: Request, exc: Exception):
    """
    全局异常处理函数，将异常转换为 500 响应
    """
    return PlainTextResponse(
        content=str(exc),
        status_code=500
    )


# 添加全局异常处理器
app.add_exception_handler(Exception, system_exception_handler)

# ========================= 路由注册 =========================
# 将各个子路由模块挂载到不同前缀下
app.include_router(router=auth_router, prefix="/auth", tags=["auth"])