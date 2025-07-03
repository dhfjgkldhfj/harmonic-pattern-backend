# Utility helper functions (e.g. swing detection, ratio validation)

def is_within_tolerance(actual, expected, tolerance):
    return abs(actual - expected) <= tolerance
