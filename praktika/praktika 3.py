def palindrome(word):
    if len(word) <= 1: #1.мадам из 5 букв значит не подходит #2.тепенрь тут ада и т.д. №будет только д
        return 'It is a palindrome!'
    if word[0] != word[-1]: #первая и последняя совпадают значит идем дальше #когда тут д то он скажет что это полиндром
        return 'это не полидром'
    return palindrome(word[1:-1]) #убираем 1 и последнюю букву и возвращает это слово наверх
print(palindrome('мадам'))

def square(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/square(x,-n)
    if n%2 == 1:
        return square(x, n-1)*x
    return square(x, n//2)*square(x, n//2)

print(square(7, 5))

def print_level(list_numb, level=1):
    print(f'\nLevel is:{level}, elements:')
    for i in list_numb:
        if type(i) != list:
            print(i, end='')
    for i in list_numb:
        if type(i) == list:
            print_level(i, level+1)
print_level([1,2,3,[4,5,32,[4,4]]])