def sum_total(obj, field):
    total = sum(getattr(i, field, 0) for i in obj)
    return total