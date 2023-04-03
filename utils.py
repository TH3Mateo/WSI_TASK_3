import numpy as np


















def evaluate(board,symbol):
    amounts = max_strikes(board,symbol)
    return




def most_a_occurrences(string,sign):
    current_a_count = 0
    max_a_count = 0

    for char in string:
        if char == sign:
            current_a_count += 1
            max_a_count = max(max_a_count, current_a_count)
        else:
            current_a_count = 0

    return max_a_count

def max_strikes(board, symbol):
    s = len(board)
    maxes = [0,0,0,0,0]
    for i in range(s):
        print(board[i])
        maxes[most_a_occurrences(board[i],symbol)] += 1

    for i in range(s):
        print([row[i] for row in board])
        maxes[most_a_occurrences([row[i] for row in board],symbol)]+=1

    for i in range(s*2-1):
        print(np.diagonal(board,s-i))
        maxes[most_a_occurrences(np.diagonal(board,s-i),symbol)]+=1

    for i in range(s*2-1):
        print(np.diagonal(np.fliplr(board),s-i))
        maxes[most_a_occurrences(np.diagonal(np.fliplr(board),s-i),symbol)]+=1
    return maxes

def main():
    eee = [[0, 0, 1, 2, 1],
           [0, 1, 2, 2, 2],
           [2, 2, 1, 2, 2],
           [1, 1, 2, 2, 1],
           [1, 1, 2, 1, 1]]
    print(max_strikes(eee,2))



main()