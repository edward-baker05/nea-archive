from board import play_games
from board import play_random_move
from minimax import create_minimax_player
from qtable import (qtables, play_training_games_x,
                           play_training_games_o, create_q_table_player)

from mcts import play_mcts_move, perform_training_playouts

# from mcts import (play_game_and_reset_playouts,
#                          play_mcts_move_with_live_playouts)

play_minimax_move_randomized = create_minimax_player(True)
play_minimax_move_not_randomized = create_minimax_player(False)

print("Playing random vs random:")
print("-------------------------")
play_games(1000, play_random_move, play_random_move)
print("")

print("Playing minimax not random vs minimax random:")
print("---------------------------------------------")
play_games(1000, play_minimax_move_not_randomized, play_minimax_move_randomized)
print("")
print("Playing minimax random vs minimax not random:")
print("---------------------------------------------")
play_games(1000, play_minimax_move_randomized, play_minimax_move_not_randomized)
print("")
print("Playing minimax not random vs minimax not random:")
print("-------------------------------------------------")
play_games(1000, play_minimax_move_not_randomized,
           play_minimax_move_not_randomized)
print("")
print("Playing minimax random vs minimax random:")
print("-----------------------------------------")
play_games(1000, play_minimax_move_randomized, play_minimax_move_randomized)
print("")

print("Playing minimax random vs random:")
print("---------------------------------")
play_games(1000, play_minimax_move_randomized, play_random_move)
print("")
print("Playing random vs minimax random:")
print("---------------------------------")
play_games(1000, play_random_move, play_minimax_move_randomized)
print("")

print("Training qtable X vs. random...")
play_training_games_x(q_tables=qtables,
                      o_strategies=[play_random_move])
print("Training qtable O vs. random...")
play_training_games_o(q_tables=qtables,
                      x_strategies=[play_random_move])
print("")

play_q_table_move = create_q_table_player(qtables)
print("Playing qtable vs random:")
print("-------------------------")
play_games(1000, play_q_table_move, play_random_move)
print("")
print("Playing qtable vs minimax random:")
print("---------------------------------")
play_games(1000, play_q_table_move, play_minimax_move_randomized)
print("")
print("Playing qtable vs minimax:")
print("--------------------------")
play_games(1000, play_q_table_move, play_minimax_move_not_randomized)
print("")

print("Playing random vs qtable:")
print("-------------------------")
play_games(1000, play_random_move, play_q_table_move)
print("")
print("Playing minimax random vs qtable:")
print("---------------------------------")
play_games(1000, play_minimax_move_randomized, play_q_table_move)
print("")
print("Playing minimax vs qtable:")
print("--------------------------")
play_games(1000, play_minimax_move_not_randomized, play_q_table_move)
print("")

print("Playing qtable vs qtable:")
print("-------------------------")
play_games(1000, play_q_table_move, play_q_table_move)
print("")
print(f"number of items in qtable = {len(qtables[0].qtable.cache)}")
print("")

print("Training MCTS...")
perform_training_playouts()
print("")
print("Playing random vs MCTS:")
print("-----------------------")
play_games(1000, play_random_move, play_mcts_move)
print("")
print("Playing minimax vs MCTS:")
print("------------------------")
play_games(1000, play_minimax_move_not_randomized, play_mcts_move)
print("")
print("Playing minimax random vs MCTS:")
print("-------------------------------")
play_games(1000, play_minimax_move_randomized, play_mcts_move)
print("")
print("Playing MCTS vs random:")
print("-----------------------")
play_games(1000, play_mcts_move, play_random_move)
print("")
print("Playing MCTS vs minimax:")
print("------------------------")
play_games(1000, play_mcts_move, play_minimax_move_not_randomized)
print("")
print("Playing MCTS vs minimax random:")
print("-------------------------------")
play_games(1000, play_mcts_move, play_minimax_move_randomized)
print("")
print("Playing MCTS vs MCTS:")
print("---------------------")
play_games(1000, play_mcts_move, play_mcts_move)
print("")

# You can uncomment the code below to run MCTS in online mode
# print("Running MCTS in online mode, but may take a while...")
# print("")
# print("Playing random vs MCTS:")
# print("-----------------------")
# play_games(100, play_random_move, play_mcts_move_with_live_playouts,
#            play_game_and_reset_playouts)
# print("")
# print("Playing minimax vs MCTS:")
# print("------------------------")
# play_games(100, play_minimax_move_not_randomized,
#            play_mcts_move_with_live_playouts, play_game_and_reset_playouts)
# print("")
# print("Playing minimax random vs MCTS:")
# print("-------------------------------")
# play_games(100, play_minimax_move_randomized, play_mcts_move_with_live_playouts,
#            play_game_and_reset_playouts)
# print("")
# print("Playing MCTS vs random:")
# print("-----------------------")
# play_games(100, play_mcts_move_with_live_playouts, play_random_move,
#            play_game_and_reset_playouts)
# print("")
# print("Playing MCTS vs minimax:")
# print("------------------------")
# play_games(100, play_mcts_move_with_live_playouts, play_minimax_move_not_randomized,
#            play_game_and_reset_playouts)
# print("")
# print("Playing MCTS vs minimax random:")
# print("-------------------------------")
# play_games(100, play_mcts_move_with_live_playouts, play_minimax_move_randomized,
#            play_game_and_reset_playouts)
# print("")
# print("Playing MCTS vs MCTS:")
# print("---------------------")
# play_games(100, play_mcts_move_with_live_playouts,
#            play_mcts_move_with_live_playouts, play_game_and_reset_playouts)
# print("")
