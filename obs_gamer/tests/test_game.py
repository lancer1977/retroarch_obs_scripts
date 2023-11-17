import unittest

from game import Game
from retroarch import RetroArchGame
from test_data import *



class TestSegaCDGame(unittest.TestCase):
    def test_validate(self):
        retroarchData = RetroArchGame(fakeSegaCDGameJson())        
        game = Game(retroarchData)
        self.assertEqual(game.platform ,"segacd")
        self.assertEqual(game.title , "Adventures of Batman & Robin, The")
        self.assertEqual(game.country , "USA")
        self.assertEqual(game.core , "Sega - MS/GG/MD/CD (Genesis Plus GX)")
        
class TestGenesisGame(unittest.TestCase):
    def test_validate(self):
        retroarchData = RetroArchGame(fakeGenesisGameJson())        
        game = Game(retroarchData)
        self.assertEqual(game.platform ,"genesis")
        self.assertEqual(game.title , "Shining Force")
        self.assertEqual(game.country , "USA")
        self.assertEqual(game.core , "Sega - MS/GG/MD/CD (Genesis Plus GX)")
  
if __name__ == '__main__':
	unittest.main()