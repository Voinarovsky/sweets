def sorted_people(a):
    prev_tree = -1
    people = []
    for i in range(len(a)):
        if a[i] != -1:
            people.append(a[i])
    people.sort(reverse=True)
    current_human = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = people[current_human]
            current_human += 1
    return a


print(sorted_people([-1, 150, 190, 170, -1, -1, 160, 180, -1])) # должно вернуть [-1, 190, 180, 170, -1, -1, 160, 150, -1]
print(sorted_people([-1, -1, -1, -1, -1])) # должно вернуть [-1, -1, -1, -1, -1]
print(sorted_people([4, 2, 9, 11, 2, 16])) # должно вернуть [16, 11, 9, 4, 2, 2]
