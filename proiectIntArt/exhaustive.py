from collections import deque
from itertools import permutations


# Function to perform breadth-first search
def breadth_first_search(cities, distances):
    start = cities[0]  # Starting city
    queue = deque([(start, [start], 0)])  # Initialize queue with starting node
    min_cost = float('inf')  # Initialize minimum cost
    best_path = []  # Initialize best path

    # Continue until queue is empty
    while queue:
        current_city, path, cost = queue.popleft()  # Dequeue the node

        # If all cities are visited, calculate the cost to return to start
        if len(path) == len(cities):
            cost += distances[current_city][start]
            # Update minimum cost and best path if the current path is better
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue  # Move to the next iteration

        # Explore all possible next cities
        for next_city in cities:
            if next_city not in path:  # If next city is not visited
                next_cost = cost + distances[current_city][next_city]
                queue.append((next_city, path + [next_city],
                              next_cost))  # Enqueue the next city

    return best_path, min_cost  # Return the best path and minimum cost


# Function to perform least-cost search
def least_cost_search(cities, distances):
    start = cities[0]  # Starting city
    queue = [(0, start, [start])
             ]  # Initialize priority queue with starting node
    min_cost = float('inf')  # Initialize minimum cost
    best_path = []  # Initialize best path

    # Continue until priority queue is empty
    while queue:
        queue.sort()  # Sort the priority queue based on cost
        cost, current_city, path = queue.pop(
            0)  # Pop the node with minimum cost

        # If all cities are visited, calculate the cost to return to start
        if len(path) == len(cities):
            cost += distances[current_city][start]
            # Update minimum cost and best path if the current path is better
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue  # Move to the next iteration

        # Explore all possible next cities
        for next_city in cities:
            if next_city not in path:  # If next city is not visited
                next_cost = cost + distances[current_city][next_city]
                queue.append((next_cost, next_city,
                              path + [next_city]))  # Enqueue the next city

    return best_path, min_cost  # Return the best path and minimum cost
