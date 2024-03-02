def is_valid_assignment(adjacency_list, assignment, node, color):
    for neighbor in adjacency_list[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(adjacency_list, colors, assignment, node):
    if node not in assignment:
        for color in colors:
            if is_valid_assignment(adjacency_list, assignment, node, color):
                assignment[node] = color

                next_node = get_unassigned_node(adjacency_list, assignment)
                if next_node is None or backtrack(adjacency_list, colors, assignment, next_node):
                    return True

                del assignment[node]

    return False

def get_unassigned_node(adjacency_list, assignment):
    for node in adjacency_list:
        if node not in assignment:
            return node
    return None

def map_coloring(adjacency_list, colors):
    assignment = {}
    start_node = get_unassigned_node(adjacency_list, assignment)
    backtrack(adjacency_list, colors, assignment, start_node)
    return assignment

# Example usage:
# Create an adjacency list representing the map
# Each key is a region, and the corresponding value is a list of adjacent regions
adjacency_list = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Define the available colors
colors = ['Red', 'Green', 'Blue']

# Solve the map coloring problem
solution = map_coloring(adjacency_list, colors)

# Print the solution
for region, color in solution.items():
    print(f"{region}: {color}")