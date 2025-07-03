def fib_retracement(start, end):
    """
    Calculate common Fibonacci retracement levels between start and end price.
    """
    diff = end - start
    levels = {
        "0.236": end - 0.236 * diff,
        "0.382": end - 0.382 * diff,
        "0.5": end - 0.5 * diff,
        "0.618": end - 0.618 * diff,
        "0.786": end - 0.786 * diff,
    }
    return levels

def fib_extension(start, end):
    """
    Calculate common Fibonacci extension levels between start and end price.
    """
    diff = end - start
    levels = {
        "1.272": end + 0.272 * diff,
        "1.618": end + 0.618 * diff,
        "2.0": end + 1.0 * diff,
    }
    return levels
