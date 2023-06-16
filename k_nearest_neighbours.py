import torch
import numpy as np


def k_nearest_neighbours(k, x, y):
    distances = []
    indices = []
    indices_y = []
    for i in range(len(x)):
        indices.append(i)
        locals = []
        for j in range(len(y)):            
            indices_y.append(j)
            locals.append(euclidean_distance(x[i], y[j]))
        distances.append(sorted(locals)[0])
    return indices, indices_y, distances


def plot_nearest_neighbours_in_3d(x, y, z):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for i in range(len(x)):
        for j in range(len(y)):
            ax.plot([x[i], y[j]], [y[j], z[j]], [z[j], z[j]], c='b')
    plt.show()
        


def euclidean_distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


x = torch.randn(100, 2)
y = torch.randn(100, 2)
i, j, n = k_nearest_neighbours(2, x, y)
print(np.array(i).shape, np.array(j).shape, np.array(n).shape)

# plot_function_of_two_variables(np.array(i), np.array(i), np.array(n))

#plot_nearest_neighbours_in_3d(i, i, n)

def plot_euclidean_distance_function_in_3d(x, y):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, euclidean_distance(x, y), c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()



plot_euclidean_distance_function_in_3d(torch.randn(100), torch.randn(100))

# """
# ========================
# 3D plot projection types
# ========================

# Demonstrates the different camera projections for 3D plots, and the effects of
# changing the focal length for a perspective projection. Note that Matplotlib
# corrects for the 'zoom' effect of changing the focal length.

# The default focal length of 1 corresponds to a Field of View (FOV) of 90 deg.
# An increased focal length between 1 and infinity "flattens" the image, while a
# decreased focal length between 1 and 0 exaggerates the perspective and gives
# the image more apparent depth. In the limiting case, a focal length of
# infinity corresponds to an orthographic projection after correction of the
# zoom effect.

# You can calculate focal length from a FOV via the equation:

# .. math::

#     1 / \\tan (\\mathrm{FOV} / 2)

# Or vice versa:

# .. math::

#     \\mathrm{FOV} = 2 \\arctan (1 / \\mathrm{focal length})

# """

# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt


# fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})

# # Get the test data
# X, Y, Z = axes3d.get_test_data(0.05)
# print(Z)
# # Plot the data
# for ax in axs:
#     ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# # Set the orthographic projection.
# axs[0].set_proj_type('ortho')  # FOV = 0 deg
# axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)

# # Set the perspective projections
# axs[1].set_proj_type('persp')  # FOV = 90 deg
# axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)

# axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
# axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)

# plt.show()
