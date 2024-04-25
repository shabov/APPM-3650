# %% [markdown]
# # HW 3
# 
# **Upload one file** to Gradescope: 
# * `HW3.py` (which will be autograded)
# 
# ___

# %%
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# %% [markdown]
# ### Function Threshold
# 
# Suppose `func(n)` is a monotonically increasing function. Write a function **`exceed_func3(func, thresh, start, end)`** that **uses binary search** to find the largest `n` between positive integers `start` and `end`, inclusive, such that `func(n)` is less than or equal to a given threshold. If there is no such `n`, return `None`.

# %% [markdown]
# Find largest $n$ such that $func(n) \leq$ thresh

# %%
# def exceed_func3(func, thresh, start, end):
#     range_vals = [n for n in range(start, end+1)]
#     if func(start) > func(end):
#         return None
#     else:
#         left = range_vals[:len(range_vals)//2]
#         right = range_vals[len(range_vals)//2+1:]
#         if func(range_vals[len(range_vals)//2]) >= thresh:
#             return range_vals[(len(range_vals)//2)-1]
#         else:
#             if func(left[len(left)//2]) > func(range_vals[len(range_vals)//2]):
#                 exceed_func3(func, thresh, start, left[-1])
#             elif func(right[len(right)//2]) > func(range_vals[len(range_vals)//2]):
#                 exceed_func3(func, thresh, right[0], end)
        


# %%
# def exceed_func3(func, thresh, start, end):
#     range_vals = [n for n in range(start, end+1)]
#     if func(start) > func(end):
#         return None
#     else:
#         if func(range_vals[len(range_vals)//2]) >= thresh:
#             return range_vals[len(range_vals)//2]
#         if func(range_vals[len(range_vals)//2]) < thresh:
#           return exceed_func3(func, thresh, range_vals[len(range_vals)//2]+1, end)
#         else:
#              return exceed_func3(func, thresh, start, range_vals[len(range_vals)//2]-1)

# %%
def exceed_func3(func, thresh, start,end):
    if start> end:
        return None
    else:
        mid = (start+end)//2
        if start == end:
            return mid - 1
        if func(end) < thresh:
            return exceed_func3(func,thresh,mid+1,end)
        if func(end) > thresh and func(mid) < thresh:
            return exceed_func3(func,thresh,mid+1,end)
        if func(mid) > thresh:
            return exceed_func3(func,thresh, start, mid)
        else:
            return mid

# %%
func_n = lambda n: n**3

# %%
exceed_func3(func_n, 10**6, 50,105)

# %%


# %% [markdown]
# ### Max SubList Problem
# Given a list of numbers, find a contiguous sublist with the largest sum. If there is more than one sublist with the same max sum, return any of them. Assume that the list contains both positive and negative numbers.
# 
# * Write a function **`max_sublist1(nums, start, end)`** that implements the brute-force (exhaustive search) solution, examining every possible sublist. It returns a 3-element tuple containing the indices that correspond to the first and last elements of the max sublist (inclusive), and the max sum.
# 
#   Example:<br>
#   `max_sublist1([1, -4, 13, -5, 7], 0, 4)` returns `(2, 4, 15)` which corresponds to the max sum of $13-5+7 = 15$ and the starting and ending indices of $2$ and $4$.
# 
# * Write a function **`max_sublist2(nums, start, end)`** that implements the divide-and-conquer solution. Recall that this is a $\Theta(n \log n)$ algorithm.
# 
# * Find a linear time algorithm for the max sublist problem. Write a function **`max_sublist3(nums, start, end)`** that implements this $\Theta(n)$ algorithm. (*Hint:* Given a starting index, as long as the accumulated sum is positive, keep adding elements. If the sum becomes negative, reset the starting index.)

# %%
def max_sublist1(nums, start, end):
    max_sum = sum(nums)
    start_idx = 0
    end_edx = 0
    for i in range(start,end+1):
        for j in range(1,end+2):
            if sum(nums[i:j]) > max_sum:
                max_sum = sum(nums[i:j])
                start_idx = i
                end_edx = j
    return (start_idx,end_edx-1,max_sum)
            

    

# %%
max_sublist1([1,-4,13,-5,7], 0,4)

# %%
def max_sublist_crossing(nums, start, mid, end):
    left_sum = -math.inf
    tot_sum = 0
    max_left=0
    for i in range(mid,start+1,-1):
        tot_sum += nums[i]
        if tot_sum > left_sum:
            left_sum = tot_sum
            max_left = i
    right_sum = -math.inf
    tot_sum = 0
    max_right = 0
    for j in range(mid+1, end+1):
        tot_sum += nums[j]
        if tot_sum > right_sum:
            right_sum = tot_sum
            max_right = j
    return (max_left, max_right, left_sum+right_sum)



# %%
nums = [1,-4,13,-5,7]

# %%
max_sublist_crossing(nums, 0,2,4)

# %%
def max_sublist2(nums,start,end):
    if start==end:
        return (start, end, nums[start])
    else:
        mid = math.floor((start+end)/2)
        (left_start, left_end, left_sum) = max_sublist2(nums, start, mid)
        (right_start, right_end, right_sum) = max_sublist2(nums, mid+1, end)
        (crossing_start, crossing_end, crossing_sum) = max_sublist_crossing(nums, start, mid, end)
        if left_sum >= right_sum and left_sum >= crossing_sum:
            return (left_start, left_end, left_sum)
        elif right_sum >= left_sum and right_sum >= crossing_sum:
            return (right_start, right_end, right_sum)
        else:
            return (crossing_start, crossing_end, crossing_sum)
        

# %%
max_sublist2([1,-4,13,-5,7], 0,4)

# %%
nums[0:0]

# %%
def max_sublist3(nums, start, end):
    i=start
    start_val = 0
    j=end
    index = 0

    max_sum = nums[start]
    for n in range(start,end+1):
        if index + nums[n] >= 0:
            index += nums[n]
            if index > max_sum:
               max_sum = index
               start_val = i
               j = n
        else:
            index = 0
            i = n+1

    return (start_val,j,max_sum)
    
    

# %%
max_sublist3(nums,0,4)

# %% [markdown]
# **Compare the runtimes for the 3 versions.**

# %%
# start = time.time()
# max_sublist1(nums,0,4)
# end= time.time()
# print(end-start)

# %%
# start = time.time()
# max_sublist2(nums,0,4)
# end= time.time()
# print(end-start)

# %%
# start = time.time()
# max_sublist3(nums,0,4)
# end= time.time()
# print(end-start)

# %%



