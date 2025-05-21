from typing import Dict
import numpy as np
from mahjong.core.env import MahjongEnv
from mahjong.core.types import TileType, ActionType, MahjongType

def print_observation(obs: Dict):
    """Helper function to print the observation in a readable format"""
    print("\nCurrent Player:", obs['current_player'])
    
    print("\nHand:")
    for tile_type in TileType:
        count = obs['hand'][tile_type.value]
        if count > 0:
            print(f"{tile_type.name}: {count}")
    
    print("\nDiscards:")
    for tile_type in TileType:
        count = obs['discards'][tile_type.value]
        if count > 0:
            print(f"{tile_type.name}: {count}")
    
    print("\nDora Indicators:")
    for value in obs['dora_indicators']:
        if value > 0:
            print(TileType(value).name)
    
    print("\nWaiting Actions:")
    actions = ["CHI", "PON", "KAN", "RON", "TSUMO"]
    for i, action in enumerate(actions):
        if obs['waiting_actions'][i]:
            print(f"Can {action}")
    print()

def main():
    # Create the environment
    env = MahjongEnv(num_players=4, mahjong_type=MahjongType.INTERNATIONAL)
    
    # Reset the environment
    obs, _ = env.reset()
    print("Initial State:")
    print_observation(obs)
    
    # Run a few example steps
    for i in range(5):
        print(f"\nStep {i + 1}")
        
        # For this example, just randomly choose an action
        # In a real implementation, you would use an AI agent here
        if np.any(obs['waiting_actions']):
            # If any special actions are available, randomly choose one
            special_actions = np.where(obs['waiting_actions'])[0]
            action = len(TileType) + np.random.choice(special_actions)
        else:
            # Otherwise, discard a random tile from hand
            possible_tiles = np.where(obs['hand'] > 0)[0]
            action = np.random.choice(possible_tiles)
        
        # Take the action
        obs, reward, terminated, truncated, info = env.step(action)
        
        print(f"Action taken: {TileType(action).name if action < len(TileType) else ActionType(action - len(TileType) + 101).name}")
        print(f"Reward: {reward}")
        print_observation(obs)
        
        if terminated or truncated:
            print("Game Over!")
            break

if __name__ == "__main__":
    main() 