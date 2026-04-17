import numpy as np
import pandas as pd

# Load data
df = pd.read_csv('cities.csv', header=None)
points = df.values

k = 3

# Initialize randomly
np.random.seed(42)
centers = points[np.random.choice(len(points), k, replace=False)]

def assign_clusters(points, centers):
    clusters = [[] for _ in range(k)]
    
    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]
        idx = np.argmin(distances)
        clusters[idx].append(p)
    
    return clusters

# Newton update = direct mean
def newton_update(clusters, centers):
    new_centers = []
    
    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            cluster = np.array(cluster)
            mean = np.sum(cluster, axis=0) / len(cluster)  # Newton formula
            new_centers.append(mean)
        else:
            new_centers.append(centers[i])
    
    return np.array(new_centers)

# Iterate (only cluster assignment needs repeating)
for _ in range(100):
    clusters = assign_clusters(points, centers)
    new_centers = newton_update(clusters, centers)
    
    if np.allclose(centers, new_centers):
        break
    
    centers = new_centers

# Output
print("Final Airport Locations:")
for i, c in enumerate(centers):
    print(f"A{i+1}: {c}")

# Cost
cost = 0
for i in range(k):
    for p in clusters[i]:
        cost += np.sum((p - centers[i])**2)

print("\nFinal Cost:", cost)