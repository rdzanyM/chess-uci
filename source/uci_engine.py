import chess
import chess.engine


class ChessEngineUCI:
    def __init__(self, engine_name, author="rdzanym"):
        self.engine_name = engine_name
        self.author = author
        self.board = chess.Board()

    def uci(self):
        print(f"id name {self.engine_name}")
        print(f"id author {self.author}")
        print("uciok")

    def isready(self):
        print("readyok")

    def ucinewgame(self):
        self.board.reset()

    def position(self, args):
        if args:
            if args.startswith("startpos"):
                self.board.reset()
            elif args.startswith("fen"):
                fen = args[4:].split("moves")[0].strip()
                self.board.set_fen(fen)
            if "moves" in args:
                moves = args.split("moves")[1].strip()
                for move in moves.split():
                    self.board.push_uci(move)

    def go(self, args):
        raise NotImplementedError("The 'go' method should be implemented in a subclass.")

    def run(self):
        while True:
            try:
                command = input()
            except EOFError:
                break
            command, args = (command.split(" ", 1) + [None])[:2]

            match command:
                case "uci":
                    self.uci()
                case "isready":
                    self.isready()
                case "ucinewgame":
                    self.ucinewgame()
                case "position":
                    self.position(args)
                case "go":
                    self.go(args)
                case "quit":
                    break
                case _:
                    print("Unknown command")
