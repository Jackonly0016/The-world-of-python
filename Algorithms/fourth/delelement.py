def delete_list(L, i):
    L_lenght = len(L)
    if i < 0 or i > L_lenght-1:
        return False
    if i >= 0 and i <= L_lenght-1:
        del L[i]
        for k in range(i, L_lenght-2):
            L[k] = L[k+1]
    print(L)

L = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
delete_list(L, 5)
