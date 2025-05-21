import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 获取项目根目录
HERE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = Path(HERE).parent.parent.parent.parent.parent

# 数据库文件路径
DB_FILE = os.path.join(BASE_DIR, "data", "majiang.db")

# 确保数据目录存在
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 