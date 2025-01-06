# Conway Life Game

import random
import time
import os

def init_board(N):
    board = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.choice([0, 1]))
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for cell in row:
            print("⬛" if cell == 1 else "⬜", end=" ")
        print()

def count_neighbors(board, i, j):
    N = len(board)
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0 or x >= N or y >= N:
                continue
            count += board[x][y]
    return count

def next_board(board):
    N = len(board)
    new_board = []
    for i in range(N):
        row = []
        for j in range(N):
            count = count_neighbors(board, i, j)
            if board[i][j] == 1:
                if count < 2 or count > 3:
                    row.append(0)
                else:
                    row.append(1)
            else:
                if count == 3:
                    row.append(1)
                else:
                    row.append(0)
        new_board.append(row)
    return new_board

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    N = 10
    board = init_board(N)
    while True:
        clear_screen()
        print_board(board)
        time.sleep(0.5)
        board = next_board(board)

if __name__ == "__main__":
    main()

# The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.