len

implement a recursive function to calculate the factorial of a given numbers
Sure! Here's a recursive function in Python to calculate the factorial of a given number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

In this function, if the input number `n` is 0 or 1, the factorial is 1. Otherwise, it recursively calls the `factorial` function with `n-1` as the input and multiplies it by `n` to calculate the factorial.