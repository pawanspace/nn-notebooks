import numpy as np
import matplotlib.pyplot as plt


def kmeans_clustering(data, k):
    # Initialize the centroids as the first k data points
    centroids = data[:k]
    print('init centroids', centroids)

    # Repeat until convergence
    while True:
        # Assign data points to clusters
        clusters = assign_clusters(data, centroids)

        # Update centroids
        new_centroids = update_centroids(data, clusters, k)

        # Stop if centroids do not change
        if np.array_equal(centroids, new_centroids):
            break

        # Update centroids
        centroids = new_centroids

    return clusters, centroids


def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        print("point", point)
        # Find the closest centroid
        closest_centroid_index = find_closest_centroid(point, centroids)

        # Add the point to the cluster
        clusters.append(closest_centroid_index)

    return np.array(clusters)


def find_closest_centroid(point, centroids):
    closest_index = 0
    closest_dist = float('inf')
    for i, centroid in enumerate(centroids):
        dist = np.linalg.norm(point - centroid)
        if dist < closest_dist:
            closest_dist = dist
            closest_index = i

    return closest_index

def update_centroids(data, clusters, k):
    centroids = np.zeros((k, 2))
    for i in range(k):
        # Get all points in the cluster
        cluster = data[clusters == i]

        # Compute the mean
        centroid = np.mean(cluster, axis=0)

        # Add to centroids
        centroids[i] = centroid

    return centroids


data = np.array([[5, 10], [20, 30], [25, 40], [30, 50], [35, 60], [40, 70], [45, 80], [10, 20]])
k = 2

print("data", data)

clusters, centroids = kmeans_clustering(data, k)
print("clusters", clusters)
print("centroids", centroids)

#Plot the data
plt.scatter(data[:, 0], data[:, 1], c=clusters, s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=200, marker='x')
plt.show()