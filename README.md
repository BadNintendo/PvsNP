# P vs NP Testing with Random City Coordinates

This repository contains a Python script that generates random city coordinates and sorts them based on their x and y values. The sorted list forms a loop, connecting the cities in a way that can be used for P vs NP problem testing.

## Overview

The P vs NP problem is one of the most significant unsolved problems in computer science. It revolves around determining whether every problem whose solution can be quickly verified (NP) can also be quickly solved (P). The provided script generates random city coordinates and sorts them based on specific criteria to create an object array that can be used for testing purposes.

## Code Explanation

The script consists of two main functions:

1. `generate_random_cities(num_cities)`: Generates a list of random city coordinates.
2. `zap(cities)`: Sorts the cities based on their x and y values and connects them to form a loop.

### `generate_random_cities(num_cities)`

This function generates a specified number of random city coordinates. Each city is represented as a dictionary with 'x' and 'y' values.

```python
import random

def generate_random_cities(num_cities):
    return [{'x': random.randint(0, 1000), 'y': random.randint(0, 1000)} for _ in range(num_cities)]
```

### `zap(cities)`

This function sorts the given list of cities based on their x and y values and connects them to form a loop. The sorted path is returned as a list.

```python
def zap(cities):
    """Sort and connect cities based on the least x and y values."""
    if not cities:
        print("No cities to process. Please check the input data.")
        return []

    # Sort cities by x, then y in ascending order
    cities_sorted = sorted(cities, key=lambda city: (city['x'], city['y']))
    sorted_path = []
    current_city = cities_sorted[0]
    sorted_path.append(current_city)
    remaining_cities = cities_sorted[1:]  # List of cities left to visit
    while remaining_cities:
        # Find the closest city by comparing x then y
        closest_city = min(remaining_cities, key=lambda city: (city['x'], city['y']))
        # Check if the closest city is in the remaining cities before trying to remove it
        if closest_city not in remaining_cities:
            # This shouldn't happen with correct data, skip this iteration
            continue
        # Attempt to remove the closest city
        index = remaining_cities.index(closest_city)
        sorted_path.append(closest_city)
        del remaining_cities[index]
        current_city = closest_city
        # If we've processed all remaining cities, break out of the loop
        if not remaining_cities:
            break

    # Ensure the first city is also placed at the end to form a loop
    if sorted_path:
        sorted_path.append(sorted_path[0])
        
    return sorted_path
```

### Execution

The script generates 10,000 random cities, sorts them, and logs the results for analysis.

```python
# Generate random cities
random_cities = generate_random_cities(10000)

# Execute the 'zap' function to sort and connect random cities
result = zap(random_cities)
if result:
    # Extract key points from the sorted path:
    # - First city as the starting point
    # - Last city to understand the penultimate stop before loop closure
    first_city = result[0]
    last_city = result[-1]

    # Log the results for analysis:
    # - 'result' reflects the sorted and connected path of cities
    # - Length check ensures we're aware of how many stops are included in this path
    print(f"Array Sorted: {result} Length Of: {len(result)}")
    # Detail the starting point of the travel path
    print(f"First starting point: {first_city}")
    # The last city gives insight into the path's structure before returning to the start
    print(f"Last starting point: {last_city}")
```

## Purpose

The purpose of this script is to create an object array for P vs NP testing. By generating random city coordinates and sorting them, the script provides a way to test algorithms and heuristics that attempt to solve NP-complete problems efficiently. This can be a useful tool for researchers and developers working on the P vs NP problem.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
