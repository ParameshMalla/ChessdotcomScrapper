import chess
import chess.pgn

pgm = open('Games/Alekhine/Alekhine1.pgn')

games = []

for game in pgm:
    games.append(game)

exporter = chess.pgn.FileExporter(games)
game.accept(exporter)