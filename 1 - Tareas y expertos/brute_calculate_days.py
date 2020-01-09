def solve(scientifics, tasks):
    min = [1000000000]
    scientifics.sort()
    tasks.sort()
    # Invalid distribution of scientifics
    if scientifics[len(scientifics)-1] < tasks[len(tasks)-1]:
        return -1

    def Analiza(result, m, capacidad, tareas):
        max = 0
        count = [0] * m
        for i in range(n):
            if capacidad[result[i]] < tareas[i]:
                return
            count[result[i]] += 1
            if count[result[i]] > max:
                max = count[result[i]]

        if max < min[0]:
            min[0] = max

    def GetArray(x):
        result = [0] * x
        for i in range(x):
            result[i] = i
        return result

    def VariacionesConRepeticiones(a, variacion, pos, m, capacidad, tareas):
        if pos == len(variacion):
            Analiza(variacion, m, capacidad, tareas)
            return
        for i in range(len(a)):
            variacion[pos] = a[i]
            VariacionesConRepeticiones(
                a, variacion, pos + 1, m, capacidad, tareas)

    def GenerateAll(m, n, capacidad, tareas):
        exp = GetArray(m)
        result = [0] * n

        VariacionesConRepeticiones(exp, result, 0, m, capacidad, tareas)

    m = len(scientifics)
    n = len(tasks)

    GenerateAll(m, n, scientifics, tasks)
    return(min[0])
