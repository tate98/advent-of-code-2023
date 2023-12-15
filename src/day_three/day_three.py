import numpy as np
import collections

def day_three_p1() -> int:
    input = np.loadtxt('src/day_three/input3.txt', dtype=str, comments=None)
    numbers = "0123456789"
    cur_num = ""
    res = 0
    cur_num_good = False

    for i in range(len(input)):
        for j in range(len(input[0])):

            if input[i][j] in numbers:
                cur_num += input[i][j]
                if check_num_good(i, j, input):
                    cur_num_good = True

            else:
                if cur_num_good:
                    print(cur_num)
                    res += int(cur_num)
                cur_num_good = False
                cur_num = ""

            if j == len(input[0]) - 1:
                if cur_num_good:
                    print(cur_num)
                    res += int(cur_num)
                cur_num_good = False
                cur_num = ""

    return res

def check_num_good(i, j, input) -> bool:
    numbers = "0123456789."
    dirs = [1, 0, -1]
    for di in dirs:
        for dj in dirs:
            row = i + di
            col = j + dj
            if row >= 0 and row < len(input) and col >= 0 and col < len(input[0]):
                if input[row][col] not in numbers:
                    return True
    return False

def day_three_p2():
    d = collections.defaultdict(list)
    input = np.loadtxt('src/day_three/input3.txt', dtype=str, comments=None)
    numbers = "0123456789"
    res = 0

    i, j = 0, 0

    while i < len(input):
        while j < len(input[0]):
            if input[i][j] in numbers:
                num = get_num(i, j, input, numbers)
                numLen = len(num)
                gear = find_gear(i, j, numLen, input)
                if gear:
                    d[gear].append(int(num))
                j += numLen
            else:
                j += 1
        j = 0
        i += 1

    for key in d:
        if len(d[key]) > 1:
            res += d[key][0] * d[key][1]

    return res


def get_num(row, col, input, numbers) -> str:
    num = input[row][col]
    if col < len(input[0]) - 1 and input[row][col + 1] in numbers:
        num += input[row][col + 1]
    if col < len(input[0]) - 2 and input[row][col + 2] in numbers:
        num += input[row][col + 2]

    return num

def find_gear(row, col, numLen, input):
    if numLen == 1:
        dirsi = [1, 0, -1]
        dirsj = [1, 0, -1]
    
    elif numLen == 2:
        dirsi = [1, 0, -1]
        dirsj = [-1, 0, 1, 2]

    elif numLen == 3:
        dirsi = [1, 0, -1]
        dirsj = [-1, 0, 1, 2, 3]

    for i in dirsi:
        for j in dirsj:
            di = row + i
            dj = col + j
            if di >= 0 and di < len(input) and dj >= 0 and dj < len(input[0]) and input[di][dj] == '*':
                    return (di, dj)
            
    return None


def main():
    print(day_three_p2())

if __name__ == "__main__":
    main()
