import heapq


# Function to compute the minimum spanning tree (MST) heuristic cost
def mst_heuristic(remaining_cities, distances):
    # If there are no remaining cities, MST cost is 0
    if not remaining_cities:
        return 0

    mst_cost = 0  # Initialize MST cost
    visited = set()  # Initialize set to keep track of visited cities
    edges = [(0, remaining_cities[0])
             ]  # Initialize priority queue with first city

    # Iterate until all cities are visited or there are no more edges
    while edges and len(visited) < len(remaining_cities):
        cost, city = heapq.heappop(edges)  # Pop the edge with minimum cost
        if city not in visited:  # If city is not visited
            visited.add(city)  # Mark city as visited
            mst_cost += cost  # Add edge cost to MST cost
            # Iterate over neighboring cities
            for next_city in remaining_cities:
                if next_city != city and next_city not in visited:
                    # Add edge to priority queue
                    heapq.heappush(edges,
                                   (distances[city][next_city], next_city))

    return mst_cost  # Return MST cost


# Function to perform A* search
def a_star_search(cities, distances):
    start = cities[0]  # Starting city
    queue = [(0, start, [start], 0)
             ]  # Initialize priority queue with starting node
    min_cost = float('inf')  # Initialize minimum cost
    best_path = []  # Initialize best path

    # Continue until priority queue is empty
    while queue:
        queue.sort()  # Sort the priority queue based on priority
        _, current_city, path, cost = heapq.heappop(
            queue)  # Pop the node with minimum cost

        # If all cities are visited, calculate the cost to return to start
        if len(path) == len(cities):
            cost += distances[current_city][start]
            # Update minimum cost and best path if the current path is better
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue  # Move to the next iteration

        # Generate remaining cities
        remaining_cities = [city for city in cities if city not in path]
        # Explore all possible next cities
        for next_city in remaining_cities:
            next_cost = cost + distances[current_city][next_city]
            # Compute heuristic (MST) cost
            h = mst_heuristic(remaining_cities, distances)
            # Add the next city to the priority queue
            heapq.heappush(
                queue,
                (next_cost + h, next_city, path + [next_city], next_cost))

    return best_path, min_cost  # Return the best path and minimum cost
