def day_one():
    vals = "0123456789"
    input = open('src/input.txt', 'r')
    lines = input.readlines()
    res = 0
    first, last = '', ''
    d = {"zero"  : "z0o", 
         "one"   : "o1e",
         "two"   : "t2o",
         "three" : "t3e",
         "four"  : "f4r",
         "five"  : "f5e",
         "six"   : "s6x",
         "seven" : "s7n",
         "eight" : "e8t",
         "nine"  : "n9e" }
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in lines:
        for num in nums:
            line = line.replace(num, d[num])
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
