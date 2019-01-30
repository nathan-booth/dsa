def is_prime(number):
    """Return True if *number* is prime.

    Precondition: number is expected to be an integer"""
    if not isinstance(number, int):
      return False

    elif number <= 1:
      return False

    for element in range(2, number - 1):
        # print("element: " + str(element) + "number: " + str(number))
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
