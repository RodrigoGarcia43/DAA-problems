
def f(capacidades, costos, tareas, k, m):
    tareas.sort()
    tareas.reverse()
    task = tareas.copy()
    caps = []
    for i in range(len(capacidades)):
        caps.append([capacidades[i], i])
    mont = 0
    t = 0
    while task:
        best = -1
        index = 0
        q = -1
        for c, i in caps:
            q += 1
            if c >= tareas[t]:  # si puede con su dificultad
                if best == -1 or costos[i] < best:
                    best = costos[i]
                    index = q
        if best != -1:
            if best + mont <= k:  # si el presupuesto me da
                mont += best
                for j in range(t, t + m):
                    if j == len(tareas):
                        return True
                    task.remove(tareas[j])
                caps.remove(caps[index])
                t += m
                continue
            else:
                return False  # si el q menos cobra no puede, nadie podra
        else:
            return False  # nadie puede con su complejidad
        tareas = task
    return True


def binary_greedy(capacidades, costos, tareas, k):
    lo = 1
    hi = len(tareas)
    solve = -1

    while(lo <= hi):
        m = int((lo + hi)/2)
        if f(capacidades, costos, tareas, k, m):
            hi = m - 1
            if solve == -1:
                solve = m
            else:
                solve = min(solve, m)
        else:
            lo = m + 1
    if solve == -1:
        return 0
    return solve
