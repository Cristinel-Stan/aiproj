# Import the functions from custom modules
from exhaustive import breadth_first_search, least_cost_search
from a_star import a_star_search


# Function to read the distances between cities
def read_distances():
    # Define the cities and distances
    cities = ["A", "B", "C", "D"]  # List of cities
    distances = {  # Dictionary representing distances between cities
        "A": {
            "B": 10,
            "C": 15,
            "D": 20
        },  # Distances from city A to other cities
        "B": {
            "A": 10,
            "C": 35,
            "D": 25
        },  # Distances from city B to other cities
        "C": {
            "A": 15,
            "B": 35,
            "D": 30
        },  # Distances from city C to other cities
        "D": {
            "A": 20,
            "B": 25,
            "C": 30
        }  # Distances from city D to other cities
    }
    return cities, distances  # Return the cities and distances


# Main function to execute the program
def main():
    cities, distances = read_distances()  # Read cities and distances

    # Perform Breadth-First Search
    print("Breadth-First Search")
    bfs_path, bfs_cost = breadth_first_search(
        cities, distances)  # Execute BFS algorithm
    print(f"Path: {bfs_path}, Cost: {bfs_cost}")  # Print BFS path and cost

    # Perform Least-Cost Search
    print("\nLeast-Cost Search")
    lcs_path, lcs_cost = least_cost_search(cities,
                                           distances)  # Execute LCS algorithm
    print(f"Path: {lcs_path}, Cost: {lcs_cost}")  # Print LCS path and cost

    # Perform A* Search
    print("\nA* Search")
    astar_path, astar_cost = a_star_search(cities,
                                           distances)  # Execute A* algorithm
    print(f"Path: {astar_path}, Cost: {astar_cost}")  # Print A* path and cost


# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to execute the program
