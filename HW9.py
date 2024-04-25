# %% [markdown]
# # HW 9
# 
# **Upload one file** to Gradescope: 
# * `HW9.py` (which will be autograded)
# 
# ___

# %%
import random
import numpy as np

# %% [markdown]
# ### Driving Routes
# Your local gym is located $m$ blocks south and $n$ blocks east of your current location. In addition,
# 
# * The streets in your town are arranged in a rectangular grid along the north-south and east-west directions.
# * You always travel south or east toward the gym, driving the minimum number of blocks.
# * One or more intersections in the grid may be blocked due to road maintenance projects. 
# 
# How many possible driving routes to the gym are there? Write a function **`driving_routes(m, n, blocked)`** that returns the number of possible routes to your destination where `blocked` is a list of `(i, j)` blocked intersections located $i$ blocks south and $j$ blocks east of your current location, $0 \le i \le m$, $0 \le j \le n$. **Use dynamic programming** to compute the answer. Use a **numpy array** to count the routes. (Assume that the upper left and lower right intersections are not blocked.)
# 
# Example:  
# `driving_routes(3, 5, [(0, 3), (2, 1)])` returns `31`. Shown below is one of the routes.
# 
# <img src="http://www.coloradomath.org/python/car_to_gym.jpg" width="349" height="232" />
# 

# %%
def driving_routes(m, n, blocked):
    blocks = np.ones((m+1,n+1), int)
    for i in blocked:
        blocks[i[0],i[1]] = 0
        if i[0] == 0:
            for k in range(i[1], n+1):
                blocks[i[0],k] = 0
        if i[1] == 0:
            for k in range(i[0], m+1):
                blocks[k, i[1]] = 0
    
    for j in range(1,n+1):
        for k in range(1,m+1):
            if blocks[k,j] == 0:
                pass
            else:
                blocks[k,j] = blocks[k-1, j] + blocks[k, j-1]

    return blocks[m,n]
            
            
        
    

# %%
driving_routes(3,5, [(0,3),(2,1)])

# %% [markdown]
# ### Bears in a Tube
# Winnie has a prized collection of teddy bears stored in a clear tube. She plans to sell one teddy bear a year, beginning next year, always selecting the leftmost or rightmost bear. The $i$ th bear will yield a profit of $p_i$ dollars if sold in 1 year. After that the bears will increase in value over time so that the profit of the $i$ th bear will be $y\cdot p_i$ dollars if sold after $y$ years.
# 
# Write a function **`teddy(profits)`** that takes a list of the (positive) profits for the individual bears and returns a tuple `(order, max_profit)` containing the order in which the bears should be sold and the maximum possible profit. The `order` will be represented as a string of `L`s and `R`s, indicating whether the leftmost or rightmost bear, respectively, should be sold, with the letter `X` used for the final single bear. The function should use a **dynamic programming** approach.
# 
# Example: Suppose Winnie has 5 bears with `profits = [2, 4, 6, 2, 5]`. Then `teddy(profits)` will return `('LRRLX', 64)` corresponding to the order Left-Right-Right-Left-Single, which will yield a max profit of $1\cdot 2+2\cdot 5+3\cdot 2+4\cdot 4+5\cdot 6=64$ dollars.

# %% [markdown]
# *Hints:* There are multiple ways to solve this problem using dynamic programming. You may wish to write a helper function that takes as input the indices for the subarray to be processed.

# %%
def teddy_helper(profits, left, right, year, memo):
    if left > right:
        return 0
    if memo[left][right][year] != -1:
        return memo[left][right][year]
  
    left_profit = profits[left] * year + teddy_helper(profits, left + 1, right, year + 1, memo)
    right_profit = profits[right] * year + teddy_helper(profits, left, right - 1, year + 1, memo)
    
    if left_profit > right_profit:
        memo[left][right][year] = left_profit
        return left_profit
    else:
        memo[left][right][year] = right_profit
        return right_profit

def teddy(profits):
    n = len(profits)
    memo = [[[-1] * (n + 1) for _ in range(n)] for _ in range(n)]
    max_profit = teddy_helper(profits, 0, n - 1, 1, memo)
    
    order = ''
    left, right = 0, n - 1
    year = 1

    while left < right: 
        left_profit = profits[left] * year + memo[left + 1][right][year + 1]
        right_profit = profits[right] * year + memo[left][right - 1][year + 1]
        if left_profit >= right_profit:
            order += 'L'
            left += 1
        else:
            order += 'R'
            right -= 1
        year += 1
    
    if left == right:
        order += 'X'
    
    return (order, max_profit)


# %%
teddy([2,4,6,2,5])

# %% [markdown]
# Calculate the result for `teddy(profits)` with `profits = [6, 3, 1, 6, 6, 5, 3, 1, 4, 5]`. The answer is `('RRRRLLLRLX', 237)`.

# %%
teddy([6, 3, 1, 6, 6, 5, 3, 1, 4, 5])[0] == 'RRRRLLLRLX'

# %%



