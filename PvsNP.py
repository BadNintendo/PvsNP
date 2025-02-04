import random

# Define a function to generate random city coordinates
def generate_random_cities(num_cities):
    return [{'x': random.randint(0, 1000), 'y': random.randint(0, 1000)} for _ in range(num_cities)]

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
        # Placeholder for potential future code or logic checks
        pass
        
    return sorted_path

# Generate random cities
random_cities = generate_random_cities(10000)

# Execute the 'zap' function to sort and connect random cities
result = zap(random_cities)
if result:
    # Extract key points from the sorted path:
    # - First city as the starting point
    # - last city to understand the penultimate stop before loop closure
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
