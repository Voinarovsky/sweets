def exchange(lst):
    if not isinstance(lst[0], int) or not isinstance(lst[1], int):
        return "invalid elements"
    lst_copy = lst.copy()
    lst[0], lst[1] = lst_copy[0] // 10 * 10 + lst_copy[1] % 10, lst_copy[1] // 10 * 10 + lst_copy[0] % 10
    return abs(lst[0] - lst[1])


print(exchange([55, 63])) # должно вернуть 30
print(exchange([1, 0])) # должно вернуть 1
print(exchange(['hello', 'bye'])) # должно вернуть invalid elements
