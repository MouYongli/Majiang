# 雀神传说：智谋与天命的博弈

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Node.js 18.x](https://img.shields.io/badge/Node.js-18.x-green.svg)](https://nodejs.org/)

![Mahjong Game Screenshot](./docs/screenshot.png)

![Mahjong Game Screenshot](./public/svg/wang.svg)




**Mahjong Strategy Platform** - Modern Web Implementation with Classic Gameplay and AI Opponents

[中文简体](./README.zh-CN.md) | English

## ✨ Core Features

### 🎮 Game System
- 4-player Classic Mahjong (International & Japanese Riichi Rules)
- Real-time Multiplayer Battles
- Smart Spectator System
- Game Replay Functionality
- Tiered Ranking System

### 🧠 AI Module
- Reinforcement Learning Framework (PPO/DQN)
- Human Player Behavior Prediction
- Adaptive Difficulty Adjustment
- Endgame Analysis Mode
- AI Battle History Visualization

### 🌐 Social Features
- Friend System & Private Chat
- Game Statistics
- Achievement System
- Real-time Voice Chat
- Cross-platform Save Data

## 🛠️ Tech Stack

### Frontend Architecture
| Module         | Technologies               |
|----------------|----------------------------|
| Core Framework | Next.js 14 (App Router)    |
| State Management| Zustand + Immer           |
| Styling        | TailwindCSS + CSS Modules |
| Animation      | Framer Motion             |
| Networking     | Socket.io-client + SWR    |

### Backend Architecture
| Module         | Technologies               |
|----------------|----------------------------|
| Core Framework | Flask + Socket.IO         |
| Databases      | PostgreSQL + Redis        |
| ORM            | SQLAlchemy 2.0            |
| Task Queue     | Celery                    |
| Deployment     | Docker + Kubernetes       |

### AI Subsystem
| Component      | Technologies               |
|----------------|----------------------------|
| Training Framework | PyTorch + RLlib        |
| Environment Interface | OpenAI Gym          |
| Feature Engineering | NumPy + Pandas       |
| Model Serving   | FastAPI + ONNX Runtime     |

## 🚀 Getting Started

### Development Requirements
- Node.js 18.x + pnpm
- Python 3.9+ + Poetry
- PostgreSQL 15 + Redis 7

### Installation

```bash
# Clone repository
git clone https://github.com/yourname/mahjong-app.git
cd mahjong-app

# Frontend dependencies
cd client && pnpm install

# Backend dependencies
cd ../server && poetry install

# AI module dependencies
cd ../ai && poetry install
```

### Database Initialization

```bash
flask db init
flask db migrate
flask db upgrade
```

