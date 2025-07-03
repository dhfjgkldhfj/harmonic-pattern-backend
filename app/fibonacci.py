def fib_retracement(start, end, ratio):
    return start + (end - start) * ratio

def fib_extension(start, end, ratio):
    return end + (end - start) * ratio
