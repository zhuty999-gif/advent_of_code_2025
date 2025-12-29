# Finding All Divisors Using Prime Factorization

**Key fact:** Every positive integer has exactly one prime factorization (*Fundamental Theorem of Arithmetic*).

---

## Step 1: Find the Prime Factorization

Repeatedly divide by the smallest prime that goes in evenly, until you reach 1.

**Example with 60:**

```
60 ÷ 2 = 30  
30 ÷ 2 = 15  
15 ÷ 3 = 5  
5 ÷ 5 = 1  
```

So,  
```
60 = 2² × 3 × 5
```

---

## Step 2: Generate All Divisors

A divisor cannot contain more of any prime than the original number has.  
So each divisor is formed by choosing, for each prime, how many copies to include (from 0 up to the max).

For \(60 = 2^2 \times 3 \times 5\):

- Pick 0, 1, or 2 twos
- Pick 0 or 1 three
- Pick 0 or 1 five

Multiply your choices together to get a divisor.

---

## Counting Divisors

Multiply together (exponent + 1) for each prime factor.

For 60:  
\[
(2+1) \times (1+1) \times (1+1) = 12\ \text{divisors}
\]

---

# Jupyter Notebook Tips

## Auto-reload Modules
When working in a notebook and modifying external `.py` files, use this magic command to auto-reload changes without restarting the kernel:

```python
%load_ext autoreload
%autoreload 2
```

---

# Python Tips

## Finding the Largest Character in a String
You can use `max()` directly on a string to find the character with the highest value (based on ASCII/Unicode value). For strings of digits, this effectively finds the largest digit.

```python
digits = "3295"
largest = max(digits)  # Returns "9" (as a string)
```

---

# Day 5: Recursion & Ranges

## Recursion Pitfalls: Wrapper vs. Helper
When writing a recursive function that requires a "helper" or "worker" step inside a loop (e.g., merging ranges until stable), be careful not to call the **wrapper** function recursively with the same data.

**Incorrect (Infinite Recursion):**
```python
def process_data(data):
    # This just calls itself with the same data -> Infinite Loop
    new_data = process_data(data) 
    # ...
```

**Correct (Iterative Wrapper):**
Call the helper function that performs the actual unit of work.
```python
def process_data(data):
    # Call the HELPER function to make progress
    new_data = helper_function(data) 
    if new_data != data:
        # Recurse or loop with the NEW data
        return process_data(new_data)
    return data
```

## Python `any()` function
The `any()` function is a concise way to check if *at least one* element in an iterable is Truthy. It stops evaluating as soon as it finds a True value (short-circuiting).

```python
# Check if ID is in ANY of the ranges
is_fresh = any(id in r for r in ranges)
```

## One-liner Generator Expressions
You can chain iterators to parse complex data structures efficiently in one line.

```python
# Parses "1-3\n5-7" into ((1, 3), (5, 7))
ranges = tuple(tuple(map(int, line.split('-'))) for line in raw_lines)
```