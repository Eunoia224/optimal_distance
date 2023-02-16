from sys import maxsize

# this variable contains the distance from every building to each other
# we have for example building and each building has its distances from its neighboring building
edges = 4

# define a function that takes in the
def delivery_route_optimization(b, s):
    path = []
    for i in range(edges):
        if i != s:
            path.append(i)

    min_path = maxsize
    # pattern = []
    # Loop until our "new_path" finds a lesser value than those that it already had
    while True:
        current_distance = 0
        k = s
        for i in range(len(path)):
            current_distance += b[k][path[i]]
            k = path[i]
        current_distance += b[k][s]
        min_path = min(min_path, current_distance)
        if not new_path(path):
            break
    return f"minimum path is {min_path}, with starting building {path}"


def new_path(l):
    length = len(l)
    i = length - 2

    while i >= 0 and l[i] > l[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = i + 1
    while j < length and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    # our direction
    go_left = i + 1
    go_right = length - 1
    # compare our values with each direction
    while go_left < go_right:
        l[go_left], l[go_right] = l[go_right], l[go_left]
        go_left += 1
        go_right -= 1
    return True

# our data
# while the 0 in the data are the buildings themselves that means if we are already at that building it has a distance 
# of 0
buildings = [[0, 36, 30, 42], [36, 0, 63, 24], [30, 63, 0, 52], [42, 24, 52, 0]]
start = 0
optimal_distance = delivery_route_optimization(buildings, start)
print(optimal_distance)
