# Majiang (Mahjong): A Game of Strategy and Luck

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Node.js 18.x](https://img.shields.io/badge/Node.js-18.x-green.svg)](https://nodejs.org/)

![Mahjong Game Screenshot](./docs/screenshot.png)

**麻将策略游戏平台** - 集成经典玩法与AI对抗的现代Web实现

English | [中文简体](./README.zh-CN.md)

## ✨ 核心功能

### 🎮 游戏系统
- 四人经典麻将（国际麻将规则，日本立直麻将规则）
- 实时多人在线对战
- 智能观战系统
- 牌局回放功能
- 段位排名系统

### 🧠 AI模块
- 强化学习训练框架（PPO/DQN）
- 人类玩家行为预测
- 自适应难度调整
- 残局分析模式
- AI对战历史可视化

### 🌐 社交功能
- 好友系统与私聊
- 牌局数据统计
- 成就系统
- 实时语音聊天
- 跨平台存档

## 🛠️ 技术栈

### 前端架构
| 模块          | 技术选型                     |
|---------------|-----------------------------|
| 核心框架      | Next.js 14 (App Router)     |
| 状态管理      | Zustand + Immer             |
| 样式方案      | TailwindCSS + CSS Modules   |
| 动画引擎      | Framer Motion               |
| 网络通信      | Socket.io-client + SWR      |

### 服务端架构
| 模块          | 技术选型                     |
|---------------|-----------------------------|
| 核心框架      | Flask + Socket.IO           |
| 数据库        | PostgreSQL + Redis          |
| ORM           | SQLAlchemy 2.0              |
| 任务队列      | Celery                      |
| 部署方案      | Docker + Kubernetes         |

### AI子系统
| 组件          | 技术选型                     |
|---------------|-----------------------------|
| 训练框架      | PyTorch + RLlib             |
| 环境接口      | OpenAI Gym                  |
| 特征工程      | NumPy + Pandas              |
| 模型服务      | FastAPI + ONNX Runtime      |

## 🚀 快速开始

### 开发环境要求
- Node.js 18.x + pnpm
- Python 3.9+ + Poetry
- PostgreSQL 15 + Redis 7

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourname/mahjong-app.git
cd mahjong-app

# 前端依赖
cd client && pnpm install

# 后端依赖
cd ../server && poetry install

# AI模块依赖
cd ../ai && poetry install
```

### 数据库初始化

```bash
flask db init
flask db migrate
flask db upgrade
```