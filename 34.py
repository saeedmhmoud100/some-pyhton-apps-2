def number_scrabble():
    nums_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player0 = []
    player1 = []
    List = []
    player = False
    while True:

        if player:
            List = player1
        else:
            List = player0
        while True:
            num = int(input('Player {} with {} numpers,\nSelect a Numper from {}: '.format(
                int(player+1), List, nums_range)))
            if num in nums_range:
                nums_range.remove(num)
                break
            else:
                print('\nSelect a numper from {}\nAgain!!'.format(
                    str(nums_range)[1:-1]))

        if player:
            player1.append(num)
        else:
            player0.append(num)

        player = not player

        for i1 in List:
            for i2 in List:
                for i3 in List:
                    if i1 != i2 and i1 != i3 and i2 != i3 and i1+i2+i3 == 15:
                        print('=============================')
                        print('The all numpers of player{} is {}'.format(
                            int(player) or 2, List))
                        print('{} + {} + {} = {}'.format(i1, i2, i3, i1+i2+i3))
                        print('Player {} Win!'.format(int(player) or 2))
                        print('=============================')
                        return True
        if not len(nums_range) > 0:
            print('numpers of player 1 ==> {}'.format(player0))
            print('numpers of player 2 ==> {}'.format(player1))
            print('=============================')
            print('There is no winner!')
            print('=============================')
            break


number_scrabble()
