# Mahjong Game Server

This is a Mahjong game server built with FastAPI.

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/yourusername/mahjong-server.git
cd server
```

2. Create a conda environment and activate it

```bash
conda create --name mahjong python=3.12
conda activate mahjong
```

3. Install dependencies and install the project

```bash
pip install -e .
# pip install -r requirements.txt # if you want to install the dependencies separately.
```

4. Run the server

```bash
uvicorn app.main:app --reload
```


