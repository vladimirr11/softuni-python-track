def read_matrix():
    """
    """
    matrix = []
    for _ in range(5):
        values = [x for x in input().split()]
        matrix.append(values)

    return matrix


matrix = read_matrix()

num_commands = int(input())


def move(matrix, direction, steps):
    """
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'A':

                if direction == 'right' and (col + steps) < len(matrix):
                    if matrix[row][col + steps] == '.':
                        matrix[row][col] = '.'
                        matrix[row][col + steps] = 'A'
                    else:
                        continue

                elif direction == 'left' and (col - steps) > 0:
                    if matrix[row][col - steps] == '.':
                        matrix[row][col] = '.'
                        matrix[row][col - steps] = 'A'
                    else:
                        continue

                elif direction == 'up' and (row - steps) > 0:
                    if matrix[row - steps][col] == '.':
                        matrix[row][col] = '.'
                        matrix[row - steps][col] = 'A'
                    else:
                        continue

                elif direction == 'down' and (row + steps) < len(matrix):
                    if matrix[row + steps][col] == '.':
                        matrix[row][col] = '.'
                        matrix[row + steps][col] = 'A'
                    else:
                        continue

    return matrix


def valiadate_existing_targets(matrix):
    """
    """
    flag = False
    targets = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'x':
                flag = True
                targets += 1

    return flag, targets


def shoot_target(matrix, direction):
    """
    """
    shotted_targets = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'A':

                if direction == 'right':
                    for i in range(col, len(matrix[0]) - 1):
                        if matrix[row][i] == 'x':
                            matrix[row][i] = '.'
                            shotted_targets.append((row, i))
                            break

                elif direction == 'left':
                    for i in range(col - 1, 0, -1):
                        if matrix[row][i] == 'x':
                            matrix[row][i] = '.'
                            shotted_targets.append((row, i))
                            break

                elif direction == 'up':
                    for i in range(row - 1, 0, -1):
                        if matrix[i][col] == 'x':
                            matrix[i][col] = '.'
                            shotted_targets.append((i, col))
                            break
                
                elif direction == 'down':
                    for i in range(row, len(matrix[0])):
                        if matrix[i][col] == 'x':
                            matrix[i][col] = '.'
                            shotted_targets.append((i, col))
                            break

    are_targets_left, num_targets = valiadate_existing_targets(matrix)

    return matrix, shotted_targets, are_targets_left, num_targets


def execute_commands(num_commands, matrix):
    """
    """
    hitted_targets = []
    for _ in range(num_commands):

        command = input().split()

        if command[0] == 'move':
            direction, steps = command[1], command[2]
            steps = int(steps)
            matrix = move(matrix, direction, steps)

        if command[0] == 'shoot':
            direction = command[1]

            matrix, shotted_tagets, any_tagets_left, curr_num_targets = shoot_target(matrix, direction)

            hitted_targets.extend(shotted_tagets)

            if any_tagets_left == False:
                print(f'Training completed! All {len(hitted_targets)} targets hit.')
                for hitted_target in hitted_targets:
                    print(f'[{hitted_target[0]}, {hitted_target[1]}]')

                return
    
    print(f'Training not completed! {curr_num_targets} targets left.')
    for pos in shotted_tagets:
        print(f'[{pos[0]}, {pos[1]}]')


if __name__ == '__main__':
    execute_commands(num_commands, matrix)
