def greedy_algorithm(items: dict, budget: int) -> tuple:
    """
    Find the optimal combination of items to maximize the total calories within the given budget.

    :param items: dict - dictionary of items with their calories and cost
    :param budget: int - the maximum budget

    :return: tuple - list of chosen items and total calories

    Time complexity: O(n log n)
    """

    # Create a list of tuples with the name of the item and the cost per calorie
    cost_per_calorie = [(name, item['calories'] / item['cost']) for name, item in items.items()]

    # Sort the list in descending order of cost per calorie
    cost_per_calorie.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    chosen_items = []

    for name, _ in cost_per_calorie:
        item_cost = items[name]['cost']
        if budget >= item_cost:
            budget -= item_cost
            total_calories += items[name]['calories']
            chosen_items.append(name)

    return chosen_items, total_calories

def dynamic_programming(items: dict, budget: int) -> tuple:
    """
    Find the optimal combination of items to maximize the total calories within the given budget.

    :param items: dict - dictionary of items with their calories and cost
    :param budget: int - the maximum budget

    :return: tuple - list of chosen items and total calories

    Time complexity: O(n * budget)
    """

    # Create a list of tuples with the name of the item and the cost per calorie
    dp = [0] * (budget + 1)

    for name, info in items.items():
        cost = info['cost']
        calories = info['calories']
        # Update the dp array for each item
        for current_budget in range(budget, cost - 1, -1):
            dp[current_budget] = max(dp[current_budget], dp[current_budget - cost] + calories)

    # Find the chosen items based on the dp array and the budget
    chosen_items = []
    current_budget = budget
    for name, info in items.items():
        cost = info['cost']
        calories = info['calories']
        if current_budget >= cost and dp[current_budget] == dp[current_budget - cost] + calories:
            chosen_items.append(name)
            current_budget -= cost

    return chosen_items, dp[budget]

if __name__ == "__main__":
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

    budget = 100
    print("Greedy Algorithm Output:")
    chosen_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print("Chosen Items:", chosen_items_greedy, "Total Calories:", total_calories_greedy)

    print("\nDynamic Programming Output:")
    chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
    print("Chosen Items:", chosen_items_dp, "Total Calories:", total_calories_dp)