import math


def subtract_square(n):
    # n is a range to valid taken numpers
    player = True
    range_nums = [i*i for i in range(1, n+1)]
    coins_numper = int(input('Enter a coins numper: '))
    while coins_numper <= 0:
        coins_numper = int(
            input('Enter a valid coins numper is bigger than 0: '))
    while coins_numper > 0:
        player = not player
        while True:
            num = float(
                input('Player {},\nEnter a numper from {}: '.format(player+1, range_nums)))
            if math.sqrt(num) % int(math.sqrt(num)) == 0 and num in range_nums:
                break
            else:
                print('Please select a numper from'.format(range_nums))
            # if num > 0 and math.sqrt(num) <= coins_numper and math.sqrt(num) % int(math.sqrt(num)) == 0:
            #     break
            # else:
            #     print('Enter a valid numper between (1,{}) and has a real square'.format(
            #         coins_numper))
        coins_numper -= int(math.sqrt(num))
        print('the remaining coins is ', coins_numper)

    print('player{} is winning!!'.format(player+1 or 2))


subtract_square(5)
