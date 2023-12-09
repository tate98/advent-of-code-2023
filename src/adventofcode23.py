def day_one():
    vals = "0123456789"
    input = open('src/input.txt', 'r')
    lines = input.readlines()
    res = 0
    first, last = '', ''

    for line in lines:
        for c in line:
            if c in vals:
                if not first:
                    first = c
                last = c
        res += int(first + last)
        first = ''
        last = ''

    print(res)

def main():
    day_one()

if __name__ == "__main__":
    main()
