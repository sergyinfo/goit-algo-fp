import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(n: int) -> dict:
    """
    Simulate rolling two dice n times and return the counts of each sum.

    :param n: int - number of dice rolls

    :return: dict - dictionary containing the counts of each sum

    Time complexity: O(n)
    """
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    return sum_counts

def calculate_probabilities(sum_counts: dict, n: int) -> dict:
    """
    Calculate the probabilities of each sum occurring.

    :param sum_counts: dict - dictionary containing the counts of each sum
    :param n: int - number of dice rolls

    :return: dict - dictionary containing the probabilities of each sum

    Time complexity: O(1)
    """
    probabilities = {k: v / n for k, v in sum_counts.items()}
    return probabilities

def plot_probabilities(probabilities: dict, analytical_probs: dict) -> None:
    """
    Plot the probabilities of each sum occurring.

    :param probabilities: dict - dictionary containing the probabilities of each sum
    :param analytical_probs: dict - dictionary containing the analytical probabilities of each sum

    :return: None
    """
    fig, ax = plt.subplots()
    labels = list(probabilities.keys())
    monte_carlo_probs = [probabilities[key] for key in labels]
    analytical_values = [analytical_probs[key] for key in labels]
    
    ax.bar([x - 0.15 for x in labels], monte_carlo_probs, width=0.3, color='b', label='Monte Carlo')
    ax.bar([x + 0.15 for x in labels], analytical_values, width=0.3, color='r', label='Analytical')
    
    ax.set_xlabel('Sum of dice')
    ax.set_ylabel('Probability')
    ax.set_title('Dice Roll Probability Comparison')
    ax.legend()
    plt.xticks(labels)
    plt.show()

# Simulation parameters
num_rolls = 1000000

# Analytical probabilities for the sum of two dice
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Simulate dice rolls and calculate probabilities
sum_counts = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sum_counts, num_rolls)

# Visualize the probabilities
plot_probabilities(probabilities, analytical_probabilities)
