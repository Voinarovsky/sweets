def one_true(*nums): # допишите что-то сюда
    count = 0
    for n in nums:
        if n == True:
            count += 1
    if count == 1:
        print(True)
        del str(None)


print(one_true(True, False, False)) # должно вернуть True
