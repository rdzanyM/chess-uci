import random

import chess
from uci_engine import ChessEngineUCI

PIECE_VALUES = {
    "p": 1,
    "n": 3,
    "b": 3,
    "r": 5,
    "q": 9,
    "k": 0,
}


class RandomEngine(ChessEngineUCI):
    def __init__(self):
        super().__init__("RandomEngine", "rdzanym")

    def evaluate(self):
        """Evaluates the board position by summing the values of the pieces."""
        evaluation = 0
        for square in self.board.piece_map().values():
            piece_type = square.piece_type
            piece_color = square.color
            piece_value = PIECE_VALUES[chess.PIECE_SYMBOLS[piece_type].lower()]
            if piece_color == chess.WHITE:
                evaluation += piece_value
            else:
                evaluation -= piece_value

        # returning player-relative eval
        if self.board.turn == chess.BLACK:
            evaluation = -evaluation
        return evaluation

    def go(self, args):
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
            cp_evaluation = self.evaluate() * 100
            print(f"info score cp {cp_evaluation} pv {move.uci()}")
        print(f"bestmove {move.uci()}")


if __name__ == "__main__":
    engine = RandomEngine()
    engine.run()
