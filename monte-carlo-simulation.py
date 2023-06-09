import random

def simulate_factory_cost(size, land_cost, labor_cost):
    """
    Simulates the cost of building a factory.

    Args:
        size: The size of the factory.
        land_cost: The cost of land.
        labor_cost: The cost of labor.

    Returns:
        The cost of building the factory.
    """

    # Generate random values for the cost of land and labor.
    land_cost_random = random.uniform(land_cost[0], land_cost[1])
    labor_cost_random = random.uniform(labor_cost[0], labor_cost[1])

    # Calculate the cost of building the factory.
    cost = size * land_cost_random + labor_cost_random

    return cost

def monte_carlo_simulation(size, land_cost, labor_cost, num_iterations):
    """
    Performs a Monte Carlo simulation to estimate the cost of building a factory.

    Args:
        size: The size of the factory.
        land_cost: The cost of land.
        labor_cost: The cost of labor.
        num_iterations: The number of iterations to perform.

    Returns:
        The estimated cost of building the factory.
    """

    # Initialize the cost distribution.
    cost_distribution = []

    # Perform the Monte Carlo simulation.
    for i in range(num_iterations):
        cost = simulate_factory_cost(size, land_cost, labor_cost)
        cost_distribution.append(cost)

    # Calculate the estimated cost of building the factory.
    estimated_cost = sum(cost_distribution) / num_iterations

    return estimated_cost

if __name__ == "__main__":
    # Set the parameters of the simulation.
    size = 100000
    land_cost = (100000, 200000)
    labor_cost = (50000, 100000)
    num_iterations = 10000

    # Perform the Monte Carlo simulation.
    estimated_cost = monte_carlo_simulation(size, land_cost, labor_cost, num_iterations)

    # Print the estimated cost.
    print("The estimated cost of building the factory is: $", estimated_cost)