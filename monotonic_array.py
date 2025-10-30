def monotonic_array(array):
    if len(array) <= 1:
        return True

    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False
        if array[i] > array[i - 1]:
            decreasing = False

    return increasing or decreasing
