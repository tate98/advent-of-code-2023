def parse( line: str ) -> int:
    firstSplit = line.split(':')
    value = int(firstSplit[0].replace("Game ", ""))
    secondSplit = firstSplit[1].split(';')
    print(secondSplit)

    for draw in secondSplit:
        colors = draw.split(',')
        if not validate_draw( colors ):
            return 0
    return value
        

def validate_draw( colors : list ) -> bool:
    maxRed, maxGreen, maxBlue = 12, 13, 14
    for color in colors:
        if "red" in color:
            val = int(color.replace(" red", ""))
            if val > maxRed:
                return False
        elif "green" in color:
            val = int(color.replace(" green", ""))
            if val > maxGreen:
                return False
        elif "blue" in color:
            val = int(color.replace(" blue", ""))
            if val > maxBlue:
                return False
    return True


def day_two():
    input = open('src/day_two/input2.txt', 'r')
    lines = input.readlines()
    res = 0

    for line in lines:
        res += parse(line)

    return res


def main():
    print(day_two())

if __name__ == "__main__":
    main()
