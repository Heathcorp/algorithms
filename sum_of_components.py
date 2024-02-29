# given a number, find the products and constants whos absolute values sum to the smallest value, examples:
# not sure of the scope of this, as I realise this is actually really hard
# Okay, I am going to restrict it to positive summands only, as I don't think it restricts the possibilites and makes things far less complex
# 1: 1
# 2: 2
# 3: 3
# 4: 4 or 2 * 2
# 5: 5
# 6: 2 * 3
# 7: 2 * 3 + 1
# 8: 4 * 2 or 2 * 2 * 2
# 9: 3 * 3
# 10: 2 * 5 or 3 * 3 + 1
# 11: 2 * 5 + 1 or 3 * 4 - 1
# 12: 3 * 4
# 13: 3 * 4 + 1
# 14: 2 * 7 or 3 * 4 + 2 or 3 * 5 - 1 this is not found by the algorithm due to complexity
# 15: 3 * 5
# 16: 4 * 4 etc
# 17: 4 * 4 + 1 etc

# 46: 
# 47: 3 * 4 * 2 - 1 ?

import math
from typing import Union

def sum_of_components(n):
  # 0: sum; 1: either a constant or the first factor; 2: second factor;  3: constant
  prev: list[Union[tuple[int, int], tuple[int, int, int, int]]] = []
  for i in range(n + 1):
    if i < 6:
      # base case, except this isn't recursion for optimisation reasons
      prev.append((i, i))
      continue

    best = (i, i)
    # dynamic programming to find the lowest cost option
    a_b_sum, a, b = factor_pairs(i)
    if a != 1 and b != 1:
      # use the lowest cost of the factors
      a_cost = min(a, prev[a][0])
      b_cost = min(b, prev[b][0])
      a_b_sum = a_cost + b_cost
      if a_b_sum < i:
        best = (a_b_sum, a, b, 0)

    # simple addition to previous answers
    for j in range(1, i):
      distance = i - j
      t = prev[j]
      if len(t) == 4:
        # j = a * b + c
        # s = cost(a) + cost(b) + c = cost(j)
        # I think my algorithm has a flaw, in that I'm not accounting for the possibility of simplifying the constant
        # Although I think this may be okay because it is accounted for in that the multiplicants can have constants in them
        # Actually no, I think this is only okay for the context of brainfuck constants (which is what this is all for), but in the context of the question it is incorrect
        (s, a, b, c) = t
        if s + distance < best[0]:
          best = (s + distance, a, b, c + distance)
    

    prev.append(best)
    print(f'{i} = {best}')
  
  return prev[-1][0]

def factor_pairs(n):
  # find the two numbers that multiply to n with the smallest sum
  # for primes this will be 1 * n
  # highly inefficient
  a = 1
  b = n
  shortest_sum = n + 1
  for i in range(2, math.ceil(math.sqrt(n))):
    if n % i == 0:
      # i is a factor
      new_a = i
      new_b = n // i
      new_sum = new_a + new_b
      if new_sum < shortest_sum:
        a = new_a
        b = new_b
        shortest_sum = new_sum

  return (shortest_sum, a, b)


if __name__ == "__main__":
  # for i in range(128):
  #   res = sum_of_components(i)
  #   print(f'{i} = {res}')
  sum_of_components(128)
