def fibonacci(n):
  """
  This function calculates the nth Fibonacci number recursively.

  Args:
    n: The index of the Fibonacci number to be calculated.

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Test cases
def test_fibonacci():
  assert fibonacci(0) == 0
  assert fibonacci(1) == 1
  assert fibonacci(2) == 1
  assert fibonacci(3) == 2
  assert fibonacci(5) == 5
  assert fibonacci(10) == 55
  print("All test cases passed!")

if __name__ == "__main__":
  test_fibonacci()
