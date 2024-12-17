# Let take list 
distances = [10, 25, 5, 30, 15, 40, 12]


shortest_distance = distances[4]
longest_distance = distances[5]
total_distance = distances[6]


for distance in distances:
    
    total_distance += distance        
    
    
    if distance < shortest_distance:
        shortest_distance = distance
    

    if distance > longest_distance:
        longest_distance = distance


print(f"Shortest route distance:  km")
print(f"Longest route distance:  km")
print(f"Total distance of all routes:  km")