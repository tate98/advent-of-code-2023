def day_four():
    input = open('src/day_four/input4.txt', 'r')
    lines = input.readlines() 
    res = 0

    for line in lines:
        line = line.rstrip()
        all_nums = line.split(': ')[1]
        winning_nums = get_winning_nums(all_nums)
        my_nums = get_my_nums(all_nums)
        
        # filter out empty entries
        winning_nums = list(filter(None, winning_nums))
        my_nums = list(filter(None, my_nums))
        
        #sort
        winning_nums = sorted(winning_nums)
        my_nums = sorted(my_nums)

        points = 0
        n, m = 0, 0
        while n < len(winning_nums) and m < len(my_nums):
            if winning_nums[n] == my_nums[m]:
                if points == 0:
                    points = 1
                else:
                    points *= 2
                n += 1
                m += 1
            elif winning_nums[n] > my_nums[m]:
                m += 1
            else: # if winning_nums[n] < my_nums[m]:
                n += 1
        res += points

    return res



def get_winning_nums(all_nums) -> list:
    winning_nums = all_nums.split(' | ')[0].split(' ')
    return winning_nums

def get_my_nums(all_nums) -> list:
    my_nums = all_nums.split(' | ')[1].split(' ')
    return my_nums

def main():
    print(day_four())

if __name__ == "__main__":
    main()