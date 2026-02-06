def fractionalknapsack(W, arr, n):
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    current_weight = 0.0

    for i in range(n):
        item_value = arr[i][0]
        item_weight = arr[i][1]

        if current_weight + item_weight <= W:
            current_weight = current_weight + item_weight
            total_value = total_value + item_value
        else:
            remaining_capacity = W - current_weight
            fraction = remaining_capacity / item_weight
            total_value = total_value + (item_value * fraction)
            break

    return total_value
