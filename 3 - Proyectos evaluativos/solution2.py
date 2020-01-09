def solve(cost, delivery, party):
    disp = delivery.copy()
    ptr = 0
    for i in party:
        ptr = 0
        for e in delivery:
            if i < e:
                disp[ptr] = disp[ptr] - 1
            ptr = ptr + 1
    orden = []
    for i in range(0, len(cost)):
        orden.append(((cost[i] / delivery[i]), i))
        # disp[i] = disp[i]   #lo agregue
    orden.sort()
    remain = delivery[len(delivery) - 1] - len(party)
    print(orden)
    result = []
    sol = 0

    for _, i in orden:
        print("current: ", i)
        print("remain: ", remain)
        print("cost_i: : ", cost[i])
        if remain >= cost[i]:
            print("Pude con remain")
            if cost[i] <= disp[i]:
                print("Disponibilidad: ", disp[i])
                print("Pude su disponibilidad")
                result.append(cost[i])
                sol = sol + 1
                # disp[i] = disp[i] - (cost[i] + 1) # lo agregue
                print("disp del current: ", disp[i])
                remain = remain - (cost[i] + 1)
                print("Remain: ", remain)
                disp_aux = disp.copy()
                print("Disp_aux:", disp_aux)
                for x in range(len(delivery) - 1, -1, -1):
                    print("Actualizando: ", x)
                    if i == x:  # lo agregue
                        print("Estoy en el current")
                        disp[x] = disp_aux[x] - (cost[i] + 1)  # menos 1 o no
                        print(disp)
                        continue
                    if delivery[x] > delivery[i]:
                        print("Esta despues")
                        disp[x] = disp_aux[x] - (cost[i] + 1)  # quite + 1
                        print("Nueva disponibilidad: ", disp[x])
                    else:
                        print("Esta antes")
                        #remain_d = delivery[i] - delivery[x] - 1
                        print("Disponibilidad x: ", disp_aux[x])
                        print("Disponibilidad i: ", disp_aux[i])

                        remain_d = disp_aux[i] - disp_aux[x]
                        print("Remain_d: ", remain_d)
                        if remain_d < cost[i]:
                            print("No me es suficiente")
                            print("Prev_disp: ", disp[x])
                            print("Disp:", disp)
                            disp[x] = disp_aux[x] - \
                                (cost[i] - remain_d)  # puse -1
                            print("Nueva disponibilidad: ", disp[x])
                            print("Disp:", disp)
                print("Disp:", disp)
                print("Disp_aux:", disp_aux)
                disp_aux = disp.copy()
        print("~~~~~~~~~~~~~~~~~~end~~~~~~~~~~~~~~~~")

    print(sol)
    print(result)


# 5
c = [2, 2, 1, 1, 1, 1]
e = [3, 6, 8, 10, 11, 12]
f = [9]

# 4
c1 = [2, 3, 2, 2, 1, 1, 1]
e1 = [3, 5, 6, 7, 8, 9, 10]
f1 = []

# 2
c2 = [4, 3, 5, 3]
e2 = [5, 7, 9, 10]
f2 = [6, 8]

# 3
c3 = [4, 1, 3, 1]
e3 = [5, 7, 9, 11]
f3 = [6, 8, 10]

# 3
c4 = [4, 1, 3, 1]
e4 = [5, 7, 9, 11]
f4 = [6, 8, 10]

# 3
c5 = [1, 3, 1, 1]
e5 = [5, 6, 7, 12]
f5 = []

# 2
c6 = [12, 1, 11]
e6 = [20, 24, 27]
f6 = [23, 26]

# 2
e7 = [1, 9, 11]
c7 = [1, 6, 6]
f7 = [10]

# 1
e8 = [4, 6, 30]
c8 = [5, 20, 2]
f8 = [22]


if __name__ == '__main__':

    # solve(c,e,f)
    # solve(c1,e1,f1)
    # solve(c2,e2,f2)
    # solve(c3,e3,f3)
    # solve(c4,e4,f4)
    # solve(c5,e5,f5)
    # solve(c6,e6,f6)
    # solve(c7,e7,f7)
    solve(c8, e8, f8)
