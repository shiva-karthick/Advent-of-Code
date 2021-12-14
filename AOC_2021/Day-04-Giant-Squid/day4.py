from pprint import pprint


def check_bingo(matrix) -> bool:
    """
        Check if any row or column is completely marked
        Returns:
            bool: True if any row or column is completely marked

    """
    for i in range(len(matrix)):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == matrix[i][3] == matrix[i][4] == True:
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == matrix[3][i] == matrix[4][i] == True:
            return True
    return False
#    return any(
#            all(matrix[row][col] for col in range(len(matrix)))
#            for row in range(len(matrix))
#        ) or any(
#            all(matrix[col][row] for col in range(len(matrix)))
#            for row in range(len(matrix))
#        )
#

def part1():
    # Store all the matrix into 1 large list
    with open(r"input.txt") as reader:
        numbers = list(map(int, reader.readline().split(",")))

        mega_matrix = []
        small_matrix = []

        i = 0
        for line in reader:
            row = list(map(int, line.split()))
            if len(row):
                small_matrix.append(row)
                i += 1
                if i == 5:
                    i = 0
                    mega_matrix.append(small_matrix)
                    small_matrix = []

    # The actual problem solving part starts here !
    for number in numbers:
        for matrix in mega_matrix:
            # Check every number in the matrix
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == number:
                        matrix[i][j] = True
            if check_bingo(matrix):
                # print(matrix)
                unmarked_numbers = sum(list(map(lambda row: sum(
                    filter(lambda e: e if type(e) == int else 0, row)), matrix)))
                print(number)
                return unmarked_numbers * number


def part2():
    answer = 0
    # Store all the matrix into 1 large list
    with open(r"input.txt") as reader:
        numbers = list(map(int, reader.readline().split(",")))

        mega_matrix = []
        small_matrix = []
        i = 0

        for line in reader:
            row = list(map(int, line.split()))
            if len(row):
                small_matrix.append(row)
                i += 1
                if i == 5:
                    i = 0
                    mega_matrix.append(small_matrix)
                    small_matrix = []

    for number in numbers:
        new_parts = []
        for matrix in range(len(mega_matrix)):
            # Check every number in the matrix
            for i in range(len(mega_matrix[matrix])):
                for j in range(len(mega_matrix[matrix][0])):
                    if mega_matrix[matrix][i][j] == number:
                        mega_matrix[matrix][i][j] = True

            if check_bingo(mega_matrix[matrix]):
                unmarked_numbers = (sum(list(map(lambda row: sum(filter(lambda e: e if type(e) == int else 0, row)), mega_matrix[matrix]))))

                print(unmarked_numbers * number)
            else:
                new_parts.append(mega_matrix[matrix])
        mega_matrix = new_parts

part2() # 16830
