
import matplotlib.pyplot as plt
import numpy as np


def calculate_probabilities(data, max_value):
    # Determine the number of positions in the longest list
    length = max(len(sublist) for sublist in data)

    # Initialize a 2D array to hold counts of each value at each position
    counts = np.zeros((length, max_value + 1))

    # Fill the counts array
    for sublist in data:
        for index, value in enumerate(sublist):
            if value <= max_value:
                counts[index, value] += 1

    # Convert counts to probabilities
    probabilities = counts / np.sum(counts, axis=1, keepdims=True)

    return probabilities


def plot_distribution(data):
    # Observe max value
    max_value = 0
    for a in data:
        lm = max(a)
        if lm > max_value:
            max_value = lm

    # Calculate probabilities
    probabilities = calculate_probabilities(data, max_value)

    # Create meshgrid for plotting
    x = np.arange(probabilities.shape[0])
    y = np.arange(max_value + 1)
    X, Y = np.meshgrid(x, y, indexing="ij")
    Z = probabilities[X, Y]

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis")

    ax.set_xlabel("Position in List")
    ax.set_ylabel("Number")
    ax.set_zlabel("Probability")

    plt.show()
