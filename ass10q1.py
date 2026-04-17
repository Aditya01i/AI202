import numpy as np
import pandas as pd
import csv
# Load data
with open('cities.csv', 'r') as f:
    reader = csv.reader(f)
    points = np.array(list(reader), dtype=float)

k = 3  # number of airports

# Step 1: Initialize randomly
np.random.seed(42)
centers = points[np.random.choice(len(points), k, replace=False)]

def assign_clusters(points, centers):
    clusters = [[] for _ in range(k)]
    
    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]  # squared distance
        idx = np.argmin(distances)
        clusters[idx].append(p)
    
    return clusters

def update_centers(clusters, centers):
    new_centers = []
    
    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            new_centers.append(np.mean(cluster, axis=0))
        else:
            new_centers.append(centers[i])  # keep old if empty
    
    return np.array(new_centers)

# Gradient descent iterations
for _ in range(100):
    clusters = assign_clusters(points, centers)
    new_centers = update_centers(clusters, centers)
    
    if np.allclose(centers, new_centers):
        break
    
    centers = new_centers

# Final result
print("Final Airport Locations:")
for i, c in enumerate(centers):
    print(f"A{i+1}: {c}")

# Cost calculation
cost = 0
for i in range(k):
    for p in clusters[i]:
        cost += np.sum((p - centers[i])**2)

print("\nFinal Cost:", cost)