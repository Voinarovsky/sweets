print('''Hello stupid men
It\'s my first cafe.''')

coffee = ['espresso','tea','americano','rath'] #список
volume = [['100ml', 3000], ['39009ml',324234], ['324234ml', 34.23]] #список в списке
print('Мы можем предложить утопится вам в:')
for i in coffee[0:-1]:
    print(i, end=', ')
print(coffee[-1], end='.\n')

while True:
    user_coffee = input()  #пока правда всегда спрашивает у юзера значение
    if user_coffee == 'exit': #выходим если не хотим что то брать
        break
    if user_coffee not in coffee:
        print('Sorry. Нету такого блять')
    else:
        print('какой те объем блять?')
        for i in volume:
            print(i[0], end=', ') #обращаемся к списку i и списку 0
        print(volume[-1][0], end='.\n')

        check = True
        while check:
            user_volume = input() + 'ml'  # пока правда всегда спрашивает у юзера значение #правда это в бьллоке if
            for i in volume:
                if user_volume == i[0]:
                    print('you should pay: '+ str(i[1]) + ' рублей сука') #
                    check = False
                    break
            else:
                print('по русски сука говори')
        break