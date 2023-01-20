cities = {
    'giza': 45646,
    'cairo': 254465,
    'asuan': 12232,
    'menia': 5482,
    'souhag': 4548,
    'kalubia': 54836,
    'bani-suafe': 47696,
    'sharm-elsheakh': 2133,
    'esmaelia': 7896,
    'kina': 658741,
}


def func(dic):
    def show(citys, mess=''):
        for i in citys.keys():
            print(
                'The city is ( {} ) and population is ( {} )       {}'.format(i, dic[i], '({})'.format(mess) if mess != '' and len(citys.keys())-1 == list(citys.keys()).index(i) else ''))

    inp = input('what do wou want:\n1) Listing all cities and their information\n2) query the dictionary for a city\n3) add a new city\nYour choise is: ')
    if inp == "1":
        show(dic)
    elif inp == "2":
        inp = input('Enter a city: ')
        try:
            city = 'yor city ({}) with population ({})'.format(inp, dic[inp])
        except:
            city = "No Cities with this name"
        print(city)
    elif inp == "3":
        new_city = input('Enter a city: ')
        new_popu = input('Enter the population of it: ')
        dic[new_city] = new_popu
        print('the cities now are: ')
        show(dic, 'new')
    else:
        print('========================')
        print('select a valid choice!!')
        print('========================')
        func(dic)
    return dic


func(cities)

# print(list({5: '5', 3: '3'}.values()))
