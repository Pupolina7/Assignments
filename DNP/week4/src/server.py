import sys
from concurrent import futures
from typing import Iterable, Optional, Dict

import grpc

import tic_tac_toe_pb2_grpc as ttt_grpc
import tic_tac_toe_pb2 as ttt


def get_winner(moves: Iterable[ttt.Move]) -> Optional[ttt.Mark]:
    winning_combinations = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Cols
        (1, 5, 9), (3, 5, 7),  # Diagonals
    )

    x_moves = []
    o_moves = []

    for move in moves:
        if move.mark == ttt.MARK_CROSS:
            x_moves.append(move.cell)
        elif move.mark == ttt.MARK_NOUGHT:
            o_moves.append(move.cell)

    for combination in winning_combinations:
        if all((cell in x_moves) for cell in combination):
            return ttt.Mark.MARK_CROSS
        if all((cell in o_moves) for cell in combination):
            return ttt.Mark.MARK_NOUGHT

    return None


class TicTacToeServicer(ttt_grpc.TicTacToeServicer):
    def __init__(self):
        self.games: Dict[int, ttt.Game] = {}

    def CreateGame(self, request, context):
        game_id = len(self.games) + 1
        new_game = ttt.Game(id=game_id, is_finished=False, turn=ttt.Mark.MARK_CROSS, moves=[])
        self.games[game_id] = new_game
        print('CreateGame()')
        return new_game

    def GetGame(self, request, context):
        game = self.games.get(request.game_id)
        print(f"GetGame(game_id={request.game_id})")
        if game is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Game with the specified ID does not exist")
            return ttt.Game
        return game

    def MakeMove(self, request, context):
        game = self.games.get(request.game_id)
        mark = 'X' if request.move.mark == ttt.Mark.MARK_CROSS else 'O'
        print(f"MakeMove(game_id={request.game_id}, move=Move(mark={mark}, cell={request.move.cell}))")
        if game is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Game with the specified ID does not exist")
            return ttt.Game

        if request.move.cell < 1 or request.move.cell > 9:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Move's cell is invalid")
            return game

        if game.is_finished:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("Game is already finished")
            return game

        if game.turn != request.move.mark:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("It's not the player's turn")
            return game

        for move in game.moves:
            if move.cell == request.move.cell:
                context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
                context.set_details("Cell is already occupied")
                return game

        game.moves.append(request.move)
        winner = get_winner(game.moves)
        if winner is not None:
            game.is_finished = True
            game.winner = winner
        elif len(game.moves) == 9:
            game.is_finished = True
        else:
            game.turn = ttt.Mark.MARK_NOUGHT if game.turn == ttt.Mark.MARK_CROSS else ttt.Mark.MARK_CROSS
        return game


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python server.py <port>")
            sys.exit(1)
        port = sys.argv[1]
        print("Server listening on 0.0.0.0:{}...".format(port))
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        ttt_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(), server)
        server.add_insecure_port('[::]:{}'.format(port))
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Exiting...")
