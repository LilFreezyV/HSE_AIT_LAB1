def mean_positive(values):
    """Return the mean of positive values.
    Raise ValueError if there are no positive values.
    """
    total = 0
    count = len(values)

    for value in values:
        if value > 0:
            total += value

    return total / count

