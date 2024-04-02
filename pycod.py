def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms in the Fibonacci sequence.
        
    Returns:
        list: Fibonacci sequence up to n terms.
    """
    fib_sequence = []
    a, b = 0, 1

    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
