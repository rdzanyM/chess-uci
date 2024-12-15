import random
from uci_engine import ChessEngineUCI

class RandomEngine(ChessEngineUCI):
    def __init__(self):
        super().__init__("RandomEngine", "rdzanym")

    def go(self, args):
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
            print(f"info score cp 0 pv {move.uci()}")
        print(f"bestmove {move.uci()}")

if __name__ == "__main__":
    engine = RandomEngine()
    engine.run()
