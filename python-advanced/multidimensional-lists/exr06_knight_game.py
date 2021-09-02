def read_board():
    """
    """
    matrix = []
    n = int(input())

    for _ in range(n):
        matrix.append(list(input()))

    return matrix    


def find_all_knights(matrix):
    """
    """
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'K':
                positions.append((i, j))

    return positions            


def knights_are_attacking_each_other(matrix):
    """
    """
    knight_positions = find_all_knights(matrix)

    for row, col in knight_positions:
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]

        for position in positions_to_check:
            pos_row, pos_col = position

            if not (0 <= pos_row <= len(matrix) - 1):
                continue
            if not (0 <= pos_col <= len(matrix) - 1):
                continue

            if matrix[pos_row][pos_col] == 'K':
                return True

    return False


def calculate_aggression(knight_positions, matrix):
    """
    """
    aggression_scores = dict()

    for row, col in knight_positions:
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1),
        ]

        attacked_count = 0
        for attacked_row, attacked_col in positions_to_check:
            if not (0 <= attacked_row <= len(matrix) - 1):
                continue
            if not (0 <= attacked_col <= len(matrix) - 1):
                continue

            if matrix[attacked_row][attacked_col] == 'K':
                attacked_count += 1

        aggression_scores[(row, col)] = attacked_count
    
    return aggression_scores


def find_max_aggression(aggression_scores):
    """
    """
    max_so_far = None
    max_pos = 0
    for pos, aggression in aggression_scores.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos

    return max_pos


def main():
    """
    """
    matrix = read_board()

    removed_knights = 0
    while knights_are_attacking_each_other(matrix):
        knight_position = find_all_knights(matrix)
        aggression_scores = calculate_aggression(knight_position, matrix)
        row, col = find_max_aggression(aggression_scores)
        matrix[row][col] = '0'
        removed_knights += 1

    return removed_knights


if __name__ == '__main__':
    print(main())
