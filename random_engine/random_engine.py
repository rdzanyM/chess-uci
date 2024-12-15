import random
import chess
import chess.engine

def apply_moves(position_command, board):
    if "moves" in position_command:
        moves = position_command.split("moves")[1].strip()
        for move in moves.split():
            board.push_uci(move)

def main():
    board = chess.Board()
    while True:
        try:
            command = input()
        except EOFError:
            break
        command, args = (command.split(" ", 1) + [None])[:2]
        match command:
            case "uci":
                print("id name RandomEngine")
                print("id author rdzanym")
                print("uciok")

            case "isready":
                print("readyok")

            case "ucinewgame":
                board.reset()

            case "position":
                if args:
                    if args.startswith("startpos"):
                        board.reset()
                    elif args.startswith("fen"):
                        fen = args[4:].split("moves")[0].strip()
                        board.set_fen(fen) 
                    if "moves" in args:
                        moves = args.split("moves")[1].strip()
                        for move in moves.split():
                            board.push_uci(move)

            case "go":
                legal_moves = list(board.legal_moves)
                if legal_moves:
                    move = random.choice(legal_moves)
                    print(f"info score cp 0 pv {move.uci()}")
                print(f"bestmove {move.uci()}")

            case "quit":
                break

            case _:
                print("Unknown command")

if __name__ == "__main__":
    main()
