import math


def subtract_square():
    # n is a range to valid taken numpers
    player = True
    coins_numper = int(input('Enter a coins numper: '))
    while coins_numper <= 0:
        coins_numper = int(
            input('Enter a valid coins numper is bigger than 0: '))
    while coins_numper > 0:
        player = not player
        while True:
            num = float(
                input('Player {},\nEnter a numper: '.format(player+1)))
            if pow(num, 2) % int(pow(num, 2)) == 0 and pow(num, 2) <= coins_numper:
                break
            else:
                print('Please, Enter a valid numper between 1 and {}: '.format(
                    int(math.sqrt(coins_numper))))
            # if num > 0 and math.sqrt(num) <= coins_numper and math.sqrt(num) % int(math.sqrt(num)) == 0:
            #     break
            # else:
            #     print('Enter a valid numper between (1,{}) and has a real square'.format(
            #         coins_numper))
        coins_numper -= int(pow(num, 2))
        print('the remaining coins is ', coins_numper)

    print('player{} is winning!!'.format(player+1 or 2))


subtract_square()
