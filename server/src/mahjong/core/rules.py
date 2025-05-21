from typing import List, Dict, Optional
from collections import Counter
from mahjong.core.types import TileType, MahjongType

class MahjongRules:
    @staticmethod
    def is_valid_chi(hand: List[TileType], target_tile: TileType) -> bool:
        """Check if a Chi (sequence) is possible with the given tile"""
        if target_tile >= TileType.WIND_EAST:  # Can't make sequences with honor tiles
            return False
            
        tile_value = target_tile.value
        tile_type = tile_value // 9 * 9  # Get base value for the tile type (man, pin, sou)
        
        # Check if we can form a sequence
        tile_number = tile_value % 9
        possible_sequences = []
        
        # Tile can be at start, middle, or end of sequence
        if tile_number <= 6:  # Can be start of sequence
            possible_sequences.append([tile_value, tile_value + 1, tile_value + 2])
        if 1 <= tile_number <= 7:  # Can be middle of sequence
            possible_sequences.append([tile_value - 1, tile_value, tile_value + 1])
        if tile_number >= 2:  # Can be end of sequence
            possible_sequences.append([tile_value - 2, tile_value - 1, tile_value])
            
        hand_counter = Counter(hand)
        
        for seq in possible_sequences:
            can_make_sequence = True
            for tile_val in seq:
                if tile_val == target_tile.value:
                    continue
                if hand_counter[TileType(tile_val)] < 1:
                    can_make_sequence = False
                    break
            if can_make_sequence:
                return True
                
        return False

    @staticmethod
    def is_valid_pon(hand: List[TileType], target_tile: TileType) -> bool:
        """Check if a Pon (triplet) is possible with the given tile"""
        return sum(1 for tile in hand if tile == target_tile) >= 2

    @staticmethod
    def is_valid_kan(hand: List[TileType], target_tile: TileType, closed: bool = True) -> bool:
        """Check if a Kan (quad) is possible with the given tile"""
        if closed:
            return sum(1 for tile in hand if tile == target_tile) == 3
        return sum(1 for tile in hand if tile == target_tile) == 3

    @staticmethod
    def is_winning_hand(hand: List[TileType], mahjong_type: MahjongType = MahjongType.INTERNATIONAL) -> bool:
        """
        Check if the hand is a winning hand.
        Basic implementation - checks for 4 sets (triplets/sequences) and a pair
        """
        if len(hand) != 14:
            return False
            
        hand_counter = Counter(hand)
        
        # Try each tile as the pair
        for tile, count in hand_counter.items():
            if count >= 2:
                # Remove the pair and check if remaining tiles form valid sets
                remaining_tiles = list(hand)
                remaining_tiles.remove(tile)
                remaining_tiles.remove(tile)
                
                if MahjongRules._can_form_sets(remaining_tiles):
                    return True
                    
        return False

    @staticmethod
    def _can_form_sets(tiles: List[TileType]) -> bool:
        """Helper method to check if tiles can be arranged into valid sets"""
        if not tiles:
            return True
            
        # Try forming a triplet
        counter = Counter(tiles)
        for tile, count in counter.items():
            if count >= 3:
                remaining = list(tiles)
                for _ in range(3):
                    remaining.remove(tile)
                if MahjongRules._can_form_sets(remaining):
                    return True
                    
        # Try forming a sequence
        for tile in tiles:
            if tile >= TileType.WIND_EAST:  # Can't make sequences with honor tiles
                continue
            
            tile_value = tile.value
            if (TileType(tile_value + 1) in tiles and 
                TileType(tile_value + 2) in tiles and 
                tile_value % 9 <= 6):  # Ensure we don't cross tile types
                    
                remaining = list(tiles)
                remaining.remove(tile)
                remaining.remove(TileType(tile_value + 1))
                remaining.remove(TileType(tile_value + 2))
                if MahjongRules._can_form_sets(remaining):
                    return True
                    
        return False 