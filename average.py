def mean_positive(values):
    """Return the mean of positive values.
    Raise ValueError if there are no positive values.
    """
    total = 0
    count = 0

    for value in values:
        if value > 0:
            total += value
            count += 1

    if count == 0:
        raise ValueError("No positive values")

    return total / count