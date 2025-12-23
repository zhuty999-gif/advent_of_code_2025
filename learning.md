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