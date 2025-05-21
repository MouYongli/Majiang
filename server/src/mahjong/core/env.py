import gymnasium as gym
import numpy as np
from typing import List, Tuple, Dict, Any, Optional
from mahjong.core.types import TileType, ActionType, MahjongType
from mahjong.core.rules import MahjongRules

class MahjongEnv(gym.Env):
    """
    Mahjong environment following gym interface.
    This environment implements Chinese Mahjong rules by default.
    """
    metadata = {'render_modes': ['human', 'rgb_array'], 'render_fps': 4}

    def __init__(self, num_players: int = 4, mahjong_type: MahjongType = MahjongType.INTERNATIONAL):
        super().__init__()
        
        self.num_players = num_players
        self.mahjong_type = mahjong_type
        
        # Define action space
        # Actions include: DISCARD (for each tile type), CHI, PON, KAN, RON, TSUMO
        self.action_space = gym.spaces.Discrete(
            len(TileType) + len([ActionType.CHI, ActionType.PON, ActionType.KAN, ActionType.RON, ActionType.TSUMO])
        )
        
        # Define observation space
        self.observation_space = gym.spaces.Dict({
            'hand': gym.spaces.Box(low=0, high=4, shape=(len(TileType),), dtype=np.int8),
            'discards': gym.spaces.Box(low=0, high=4, shape=(len(TileType),), dtype=np.int8),
            'dora_indicators': gym.spaces.Box(low=0, high=len(TileType), shape=(5,), dtype=np.int8),
            'current_player': gym.spaces.Discrete(num_players),
            'last_action': gym.spaces.Discrete(self.action_space.n),
            'waiting_actions': gym.spaces.MultiBinary(5)  # CHI, PON, KAN, RON, TSUMO
        })
        
        self.rules = MahjongRules()
        self.reset()

    def reset(self, seed: Optional[int] = None, options: Optional[Dict] = None) -> Tuple[Dict, Dict]:
        super().reset(seed=seed)
        
        # Initialize wall
        self.wall = self._create_wall()
        np.random.shuffle(self.wall)
        
        # Initialize game state
        self.hands = [[] for _ in range(self.num_players)]
        self.discards = []
        self.dora_indicators = self.wall[-5:]  # Last 5 tiles as dora indicators
        self.wall = self.wall[:-5]
        
        # Deal initial tiles
        self._deal_initial_hands()
        
        # Game state
        self.current_player = 0
        self.last_action = None
        self.last_discard = None
        self.waiting_actions = np.zeros(5, dtype=np.int8)  # CHI, PON, KAN, RON, TSUMO
        
        return self._get_observation(), {}

    def step(self, action: int) -> Tuple[Dict, float, bool, bool, Dict]:
        reward = 0
        terminated = False
        truncated = False
        info = {}
        
        # Handle special actions first
        if action >= len(TileType):
            action_type = list(ActionType)[action - len(TileType)]
            if action_type == ActionType.CHI and self.waiting_actions[0]:
                if self.rules.is_valid_chi(self.hands[self.current_player], self.last_discard):
                    self._perform_chi()
                    reward = 1
                else:
                    reward = -1
            elif action_type == ActionType.PON and self.waiting_actions[1]:
                if self.rules.is_valid_pon(self.hands[self.current_player], self.last_discard):
                    self._perform_pon()
                    reward = 1
                else:
                    reward = -1
            elif action_type == ActionType.KAN and self.waiting_actions[2]:
                if self.rules.is_valid_kan(self.hands[self.current_player], self.last_discard):
                    self._perform_kan()
                    reward = 2
                else:
                    reward = -1
            elif action_type == ActionType.RON and self.waiting_actions[3]:
                if self.rules.is_winning_hand(self.hands[self.current_player] + [self.last_discard]):
                    reward = 10
                    terminated = True
                else:
                    reward = -5
            elif action_type == ActionType.TSUMO and self.waiting_actions[4]:
                if self.rules.is_winning_hand(self.hands[self.current_player]):
                    reward = 15
                    terminated = True
                else:
                    reward = -5
        else:
            # Regular discard action
            tile = TileType(action)
            if tile in self.hands[self.current_player]:
                self._perform_discard(tile)
                reward = 0
                
                # Check if other players can make actions
                self._update_waiting_actions()
            else:
                reward = -1
        
        # Check if wall is empty
        if len(self.wall) == 0:
            truncated = True
        
        return self._get_observation(), reward, terminated, truncated, info

    def _perform_discard(self, tile: TileType):
        """Perform a discard action"""
        self.hands[self.current_player].remove(tile)
        self.discards.append(tile)
        self.last_discard = tile
        self.current_player = (self.current_player + 1) % self.num_players
        self.last_action = ActionType.DISCARD

    def _perform_chi(self):
        """Perform a Chi action"""
        # Implementation details for Chi
        pass

    def _perform_pon(self):
        """Perform a Pon action"""
        # Implementation details for Pon
        pass

    def _perform_kan(self):
        """Perform a Kan action"""
        # Implementation details for Kan
        pass

    def _update_waiting_actions(self):
        """Update which special actions are available to players"""
        self.waiting_actions = np.zeros(5, dtype=np.int8)
        
        for i in range(self.num_players):
            if i == self.current_player:
                continue
                
            if self.rules.is_valid_chi(self.hands[i], self.last_discard):
                self.waiting_actions[0] = 1
            if self.rules.is_valid_pon(self.hands[i], self.last_discard):
                self.waiting_actions[1] = 1
            if self.rules.is_valid_kan(self.hands[i], self.last_discard):
                self.waiting_actions[2] = 1
            if self.rules.is_winning_hand(self.hands[i] + [self.last_discard]):
                self.waiting_actions[3] = 1
        
        # Check for Tsumo
        if self.rules.is_winning_hand(self.hands[self.current_player]):
            self.waiting_actions[4] = 1

    def _get_observation(self) -> Dict:
        """Convert current game state to observation space format"""
        hand_array = np.zeros(len(TileType), dtype=np.int8)
        for tile in self.hands[self.current_player]:
            hand_array[tile] += 1
            
        discard_array = np.zeros(len(TileType), dtype=np.int8)
        for tile in self.discards:
            discard_array[tile] += 1
            
        dora_array = np.array(
            [tile.value for tile in self.dora_indicators] + [0] * (5 - len(self.dora_indicators)),
            dtype=np.int8
        )
        
        return {
            'hand': hand_array,
            'discards': discard_array,
            'dora_indicators': dora_array,
            'current_player': self.current_player,
            'last_action': self.last_action if self.last_action is not None else 0,
            'waiting_actions': self.waiting_actions
        }

    def render(self):
        """Render the game state"""
        # TODO: Implement rendering
        pass

    def _create_wall(self) -> List[TileType]:
        """Create and return a complete set of Mahjong tiles"""
        wall = []
        # Add numbered tiles (Characters, Dots, Bamboo)
        for tile in range(TileType.MAN_1, TileType.SOU_9 + 1):
            wall.extend([TileType(tile)] * 4)
        
        # Add honor tiles
        for tile in range(TileType.WIND_EAST, TileType.DRAGON_WHITE + 1):
            wall.extend([TileType(tile)] * 4)
            
        # Add flower tiles if playing Chinese Mahjong
        if self.mahjong_type == MahjongType.INTERNATIONAL:
            for tile in range(TileType.SPRING, TileType.CHRYSANTHEMUM + 1):
                wall.append(TileType(tile))
                
        return wall

    def _deal_initial_hands(self):
        """Deal initial tiles to all players"""
        tiles_per_player = 13
        for i in range(self.num_players):
            self.hands[i] = self.wall[:tiles_per_player]
            self.wall = self.wall[tiles_per_player:]

    def _get_observation(self) -> Dict:
        """Convert current game state to observation space format"""
        hand_array = np.zeros(len(TileType), dtype=np.int8)
        for tile in self.hands[self.current_player]:
            hand_array[tile] += 1
            
        discard_array = np.zeros(len(TileType), dtype=np.int8)
        for tile in self.discards:
            discard_array[tile] += 1
            
        dora_array = np.array(
            [tile.value for tile in self.dora_indicators] + [0] * (5 - len(self.dora_indicators)),
            dtype=np.int8
        )
        
        return {
            'hand': hand_array,
            'discards': discard_array,
            'dora_indicators': dora_array,
            'current_player': self.current_player,
            'last_action': self.last_action if self.last_action is not None else 0,
            'waiting_actions': self.waiting_actions
        } 