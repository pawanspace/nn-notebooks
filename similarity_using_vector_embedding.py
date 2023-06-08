def get_similar_data(data, vector_embeddings, k):
    """Gets the most similar data to a given data point.

    Args:
        data: The data point to find similar data for.
        vector_embeddings: The vector embeddings of the data.

    Returns:
        A list of the most similar data points.
    """

    # Calculate the dot product of the data point with all other data points.
    dot_products = []
    for i in range(len(data)):
        dot_products.append(dot_product(data[i], vector_embeddings[i]))

    print(dot_products)

    # Sort the data points by their dot product values.
    sorted_data = sorted(range(len(data)), key=lambda i: dot_products[i])

    # Return the first k data points.
    return sorted_data[:k]

def dot_product(v1, v2):
    """Calculates the dot product of two vectors.

    Args:
        v1: The first vector.
        v2: The second vector.

    Returns:
        The dot product of v1 and v2.
    """

    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]

    return result



data = [[1, 2, 3], [4, 5, 6]]
vector_embeddings = [[19, 20, 21], [22, 23, 24], [25, 26, 27], [4, 5, 6], [28, 29, 30], [31, 32, 33], [34, 35, 36], [37, 38, 39], [40, 41, 42],[7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

similar = get_similar_data(data, vector_embeddings, 15)
print(similar)
