import numpy as np

def day_three() -> int:
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

def main():
    print(day_three())

if __name__ == "__main__":
    main()
