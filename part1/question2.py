def swapper(t):
    x, y = t
    return (y, x)

# Asigna la función `swapper` a la variable `swapper`
swapper = swapper

def run_swapper(list_of_tuples):
    return list(map(swapper, list_of_tuples))
