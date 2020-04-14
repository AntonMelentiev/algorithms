def is_sorted(a: list):
    """
    Check if elements in list in sorted order.
    Iimplies all list items are compatible to each other.
    :param a: list
    :return: bool
    """
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True
