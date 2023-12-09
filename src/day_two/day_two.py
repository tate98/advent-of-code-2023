def parse( line: str ) -> int:
    firstSplit = line.split(':')
    value = int(firstSplit[0].replace("Game ", ""))
    secondSplit = firstSplit[1].split(';')

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

def find_min_possible( colors : list ) -> list:
    vals = {"red" : 0, "blue" : 0, "green" : 0}
    for color in colors:
        if "red" in color:
            val = int(color.replace(" red", ""))
            vals["red"] = val
        if "green" in color:
            val = int(color.replace(" green", ""))
            vals["green"] = val
        if "blue" in color:
            val = int(color.replace(" blue", ""))
            vals["blue"] = val
    return vals

def find_power( line: str ) -> int:
    color_strs = ["red", "blue", "green"]
    firstSplit = line.split(':')
    secondSplit = firstSplit[1].split(';')
    min_vals = {"red" : -1, "green" : -1, "blue" : -1}

    for draw in secondSplit:
        colors = draw.split(',')
        vals = find_min_possible( colors )
        for c in color_strs:
            min_vals[c] = max(min_vals[c], vals[c])
    print(min_vals)

    return min_vals["red"] * min_vals["green"] * min_vals["blue"]

def day_two():
    input = open('src/day_two/input2.txt', 'r')
    lines = input.readlines()
    res = 0

    for line in lines:
        res += find_power(line)

    return res


def main():
    print(day_two())

if __name__ == "__main__":
    main()
