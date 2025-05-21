from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mahjong.app.api.routers import users
from mahjong.app.api.models.user import Base
from mahjong.app.config.database import engine

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Majiang Game API",
    description="API for Majiang game",
    version="0.1.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(users.router, prefix="/api/users", tags=["users"])
