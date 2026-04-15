import random
import math


def minimax(depth, index, is_max, values, height, counter):
    counter[0] += 1  # count node visit

    if depth == height:
        return values[index]

    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, values, height, counter),
            minimax(depth + 1, index * 2 + 1, False, values, height, counter)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, values, height, counter),
            minimax(depth + 1, index * 2 + 1, True, values, height, counter)
        )


def alphabeta(depth, index, is_max, values, height, alpha, beta, counter, pruned):
    counter[0] += 1  # count node visit

    if depth == height:
        return values[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False, values, height, alpha, beta, counter, pruned)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                pruned[0] += 1
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True, values, height, alpha, beta, counter, pruned)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                pruned[0] += 1
                break
        return best


def run_case(values):
    n = len(values)
    height = int(math.log2(n))

    print("Generated Leaf Nodes:", values)

    # Minimax
    mini_count = [0]
    optimal_minimax = minimax(0, 0, True, values, height, mini_count)

    print("Minimax:")
    print("    Nodes Evaluated:", mini_count[0])
    print("    Optimal Value:", optimal_minimax)

    # Alpha-Beta
    ab_count = [0]
    pruned = [0]

    optimal_ab = alphabeta(0, 0, True, values, height, -math.inf, math.inf, ab_count, pruned)

    print("Alpha-Beta Pruning:")
    print("    Nodes Evaluated:", ab_count[0])
    print("    Nodes Pruned:", pruned[0])

    # Efficiency
    improvement = ((mini_count[0] - ab_count[0]) / mini_count[0]) * 100
    print("Efficiency Improvement: {:.2f}%".format(improvement))
    print("\n")




# Case 1
case1 = [3, 5, 2, 9, 12, 5, 23, 23]

run_case(case1)

# Case 2
case2 = [8, 6, 7, 4, 15, 10, 9, 11]

run_case(case2)