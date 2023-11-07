def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']

    # Sort the items in non-increasing order of value-to-weight ratio
    items.sort(key=lambda x: x['value_per_weight'], reverse=True)

    total_value = 0.0  # Initialize the total value to zero
    knapsack = []  # Initialize an empty knapsack

    for item in items:
        if capacity >= item['weight']:
            # Take the whole item if there is enough capacity
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            # Take a fraction of the item to fill the capacity
            fraction = capacity / item['weight']
            item['fraction'] = fraction
            knapsack.append(item)
            total_value += item['value'] * fraction
            break  # The knapsack is now full

    return knapsack, total_value


# Example usage:
items = [
    {'name': 'Item1', 'value': 10, 'weight': 5},
    {'name': 'Item2', 'value': 5, 'weight': 3},
    {'name': 'Item3', 'value': 15, 'weight': 5},
    {'name': 'Item4', 'value': 7, 'weight': 7},
    {'name': 'Item5', 'value': 6, 'weight': 1}
]
knapsack, total_value = fractional_knapsack(items, 15)

print("Items in the knapsack:")
for item in knapsack:
    if 'fraction' in item:
        print(f"{item['name']} (Fraction: {item['fraction']:.2f})")
    else:
        print(item['name'])

print(f"Total value in the knapsack: {total_value}")