class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c, parent=None):
        self.left_m = left_m
        self.left_c = left_c
        self.boat = boat
        self.right_m = right_m
        self.right_c = right_c
        self.parent = parent

    def is_valid(self):
        if self.left_m < 0 or self.left_c < 0 or self.right_m < 0 or self.right_c < 0:
            return False
        if self.left_m > 3 or self.left_c > 3 or self.right_m > 3 or self.right_c > 3:
            return False
        if self.left_m < self.left_c and self.left_m > 0:
            return False
        if self.right_m < self.right_c and self.right_m > 0:
            return False
        return True

    def is_goal(self):
        return self.left_m == 0 and self.left_c == 0

    def __eq__(self, other):
        return self.left_m == other.left_m and self.left_c == other.left_c \
               and self.boat == other.boat and self.right_m == other.right_m \
               and self.right_c == other.right_c

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))

def successors(state):
    children = []
    if state.boat == 'left':
        for i in range(3):
            for j in range(3):
                if i + j <= 2 and i + j > 0:
                    new_state = State(state.left_m - i, state.left_c - j, 'right', state.right_m + i, state.right_c + j, state)
                    if new_state.is_valid():
                        children.append(new_state)
    else:
        for i in range(3):
            for j in range(3):
                if i + j <= 2 and i + j > 0:
                    new_state = State(state.left_m + i, state.left_c + j, 'left', state.right_m - i, state.right_c - j, state)
                    if new_state.is_valid():
                        children.append(new_state)
    return children

def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = [initial_state]
    explored = set()
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None

def print_solution(solution):
    if not solution:
        print("No solution found.")
        return
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(f"Step {t}: {state.left_m}M {state.left_c}C {state.boat} || {state.right_m}M {state.right_c}C")

if __name__ == "__main__":
    solution = breadth_first_search()
    print("Solution:")
    print_solution(solution)
