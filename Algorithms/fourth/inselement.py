def insert_list(L, i, element):
    L_lenght = len(L)
    if i < 0 or i > L_lenght-1:
        return False
    if i >= 0 and i <= L_lenght-1:
        for k in range(i-1, L_lenght)[::-1]:
            L[k+1:k+2] = [L[k]]
        L[i] = element
    print(L)
    return True

L = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
insert_list(L, 2, 0)
