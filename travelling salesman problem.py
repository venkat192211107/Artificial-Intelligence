import itertools

def calculate_distance(points, order):
    total_distance = 0
    num_points = len(order)
    for i in range(num_points):
        point1 = points[order[i]]
        point2 = points[order[(i + 1) % num_points]]
        total_distance += ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    return total_distance

def traveling_salesman_brute_force(points):
    min_distance = float('inf')
    min_order = None
    num_cities = len(points)

    for order in itertools.permutations(range(num_cities)):
        distance = calculate_distance(points, order)
        if distance < min_distance:
            min_distance = distance
            min_order = order

    return min_order, min_distance

# Example usage:
if __name__ == "__main__":
    # Example cities represented as (x, y) coordinates
    cities = {
        'A': (0, 0),
        'B': (1, 2),
        'C': (3, 1),
        'D': (5, 3)
    }

    optimal_order, min_distance = traveling_salesman_brute_force(list(cities.values()))
    print("Optimal order:", optimal_order)
    print("Minimum distance:", min_distance)
