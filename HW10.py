# %% [markdown]
# # HW 10
# 
# **Upload one file** to Gradescope: 
# * `HW10.py` (which will be autograded)
# 
# ___

# %%
import numpy as np

# %% [markdown]
# ### Hops
# 
# Bubbs Bunny is hopping up and down a set of stairs, one step at a time. Suppose Bubbs starts on the ground, makes `n` hops and ends back on the ground, always staying on or above the ground. How many distinct sequences of hops will produce this result?
# 
# Write a function **`count_hop_seq(n)`** that uses **dynamic programming** to count the number of up-down sequences of length $n$ that begin and end on the ground. Assume that `n` is a positive integer.
# 
# Example: `count_hop_seq(6)` returns `5`. The sequences are UUUDDD, UUDDUD, UDUUDD, UUDUDD, and UDUDUD.

# %%
def count_hop_seq(n):
    if n % 2 != 0:
        return 0
    else:
        i = j = n // 2 
        arr1 = np.zeros((i+1,j+1), int)
        for m in range(1,i+1):
            arr1[0,m] = 1
        arr1[1,1] = 1
        for k in range(1,i+1):
            for m in range(2,j+1):
                arr1[k,m] = arr1[k, m-1] + arr1[k-1, m]
    
    return arr1[-2,-1]
    

# %%
arr1 = np.zeros((4,4))
for m in range(1,4):
    arr1[0,m] = 1
arr1[1,1] = 1
arr1

# %%
count_hop_seq(4), count_hop_seq(6), count_hop_seq(8)

# %%
6//2 + 1

# %% [markdown]
# ### Spelling Correction
# Suppose you type `blder` into a search engine. It will try to match your entry to common search terms. Perhaps you actually meant to type `boulder` or `bold` or `baller`. The search engine might guess the word you intended by calculating the fewest number of changes needed to convert your entry into a common search term. It can then ask 'Did you mean ...?'. For example, the calculations would find that
# 
# * To convert `blder` into `boulder`, one can insert `o` and `u`, a total of 2 changes.
# * To convert `blder` into `bold`, one can insert `o` and omit `e` and `r`, a total of 3 changes.
# * To convert `blder` into `baller`, one can insert `a`, replace `d` with `l`, a total of 2 changes.
# 
# Use dynamic programming to write a function **`string_convert(str1, str2)`** that takes two strings `str1` and `str2` and returns the minimum number of changes needed to convert `str1` to `str2` using the following operations:
# * **insert** which adds a character from `str2` to `str1`
# * **omit** which omits a character from `str1`
# * **replace** which replaces a character in `str1` with a character in `str2`
# * **`match`** which does not entail any changes. 
# 
# The function also should print the operations that correspond to the minimum number of changes.
# 
# Example:<br>
# `string_convert('bffflooo', 'buffalo')` might print
# ```
# match   b
# replace u
# match   f
# match   f
# insert  a
# match   l
# match   o
# omit    o
# omit    o
# ```
# and return `4`. There are other solutions with 4 moves.

# %%
def LCS_helper(x,y):
    m = len(x)
    n= len(y)
    b = np.ones((m+1,n+1))
    c = np.zeros((m+1,n+1))
    for i in range(1,m+1):
        c[i,0] = 0
    for j in range(1,n+1):
        c[0,j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i,j] = c[i-1,j-1] + 1
                b[i,j] = 9 #NWArrow = 9
            elif c[i-1, j] >= c[i, j-1]:
                c[i,j] = c[i-1,j]
                b[i,j] = 2 #UpArrow = 2
            else:
                c[i,j] = c[i,j-1]
                b[i,j] = 8 #'LeftArrow' = 8
    return c,b

# def print_lcs_helper(b, x, i, j):
#     if i ==0 or j == 0:
#         return ''
#     if b[i,j] == 9:
#         return x[i-1] + print_lcs_helper(b, x, i-1, j-1)
#     elif b[i,j] == 2:
#         return print_lcs_helper(b,x,i-1,j)
#     else:
#         return print_lcs_helper(b,x,i,j-1)

def print_lcs_helper(b, x, y, i, j, change_count = 0):
    if i ==0 or j == 0:
        return change_count
    if b[i,j] == 2 and b[i-1,j] == 8:
        print(f'Replace {x[i-1]} with {y[j-1]}')
        return print_lcs_helper(b,x,y, i-1, j-1, change_count + 1)
    elif b[i,j] == 9:
        print(f'Match {x[i-1]}')
        return print_lcs_helper(b, x, y, i-1, j-1, change_count)
    elif b[i,j] == 2:
        print(f'Omit {x[i-1]}')
        return print_lcs_helper(b,x,y,i-1,j, change_count + 1)
    else:
        print(f'Insert {y[j-1]}')
        return print_lcs_helper(b,x,y,i,j-1, change_count + 1)

def string_convert(str1, str2):
    return print_lcs_helper(LCS_helper(str1, str2)[1], str1, str2, len(str1), len(str2))
    

# %%
LCS_helper('bffflooo', 'buffalo')

# %%
string_convert('bffflooo', 'buffalo')

# %%
LCS_helper('Algorithm', 'Altruistic')

# %%
# def test_LCS(x,y):
#     m = len(x)
#     n= len(y)
#     c = np.zeros((m+1,n+1))
#     for i in range(0,m):
#         c[i,0] = 0
#     for j in range(0,n):
#         c[0,j] = 0
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if x[i-1] == y[j-1]:
#                 c[i,j] = c[i-1,j-1] + 1
#             elif c[i-1, j] >= c[i, j-1]:
#                 c[i,j] = c[i-1,j]
#             else:
#                 c[i,j] = c[i,j-1]
#     return c
    

# %%
# test_LCS('bffflooo', 'buffalo')

# %%
# def test_LCS2(x,y):
#     m = len(x)
#     n= len(y)
#     b = np.ones((m+1,n+1))
#     c = np.zeros((m+1,n+1))
#     for i in range(0,m):
#         c[i,0] = 0
#     for j in range(0,n):
#         c[0,j] = 0
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if x[i-1] == y[j-1]:
#                 c[i,j] = c[i-1,j-1] + 1
#                 b[i,j] = 9 #NWArrow = 9
#             elif c[i-1, j] >= c[i, j-1]:
#                 c[i,j] = c[i-1,j]
#                 b[i,j] = 2 #UpArrow = 2
#             else:
#                 c[i,j] = c[i,j-1]
#                 b[i,j] = 8 #'LeftArrow' = 8
#     return c,b


# %%
# test_LCS2('Algorithm', 'Altruistic')

# %%
# b= np.array('')
# b

# %%
# test_LCS2('bffflooo','buffalo')[1]

# %%
# def print_lcs(b, x, i, j):
#     if i ==0 or j == 0:
#         return 
#     if b[i,j] == 9:
#         print(x[i-1], end = '')
#         print_lcs(b, x, i-1, j-1)
#     elif b[i,j] == 2:
#         print_lcs(b,x,i-1,j)
#     else:
#         print_lcs(b,x,i,j-1)

# %%
# def print_lcs(b, x, y, i, j):
#     if i ==0 or j == 0:
#         return ''
#     if b[i,j] == 2 and b[i-1,j] == 8:
#         print(f'Replace {x[i-1]} with {y[j-1]}')
#         return y[j-1] + print_lcs(b,x,y, i-1, j-1)
#     elif b[i,j] == 9:
#         print(f'Match {x[i-1]}')
#         return x[i-1] + print_lcs(b, x, y, i-1, j-1)
#     elif b[i,j] == 2:
#         print(f'Omit {x[i-1]}')
#         return '' + print_lcs(b,x,y,i-1,j)
#     else:
#         print(f'Insert {y[j-1]}')
#         return y[j-1]+ print_lcs(b,x,y,i,j-1)

# %%
# def print_lcs(b, x, y, i, j, change_count = 0):
#     if i ==0 or j == 0:
#         return change_count
#     if b[i,j] == 2 and b[i-1,j] == 8:
#         print(f'Replace {x[i-1]} with {y[j-1]}')
#         return print_lcs(b,x,y, i-1, j-1, change_count + 1)
#     elif b[i,j] == 9:
#         print(f'Match {x[i-1]}')
#         return print_lcs(b, x, y, i-1, j-1, change_count)
#     elif b[i,j] == 2:
#         if 
#         print(f'Omit {x[i-1]}')
#         return print_lcs(b,x,y,i-1,j, change_count + 1)
#     else:
#         print(f'Insert {y[j-1]}')
#         return print_lcs(b,x,y,i,j-1, change_count + 1)

# %%
# def print_lcs(b, x, y, i, j, change_count = 0):
#     if i ==0 or j == 0:
#         return change_count
#     # if b[i,j] == 2 and b[i-1,j] == 8:
#     #     print(f'Replace {x[i-1]} with {y[j-1]}')
#     #     return print_lcs(b,x,y, i-1, j-1, change_count + 1)
#     elif b[i,j] == 9:
#         print(f'Match {x[i-1]}')
#         return print_lcs(b, x, y, i-1, j-1, change_count)
#     elif b[i,j] == 2:
#         k = i - 1
#         while b[k,j] != 8:
#             k -= 1
#         print(f'Omit {x[i-1]}')
#         return print_lcs(b,x,y,i-1,j, change_count + 1)
#     else:
#         print(f'Insert {y[j-1]}')
#         return print_lcs(b,x,y,i,j-1, change_count + 1)

# %%
# print_lcs(test_LCS2('Algorithm','Altruistic')[1],'Algorithm','Altruistic', 9, 10)

# %%
# def print_lcs2(b,x,y,i,j):
#     change_ct = 0
#     m = n = 1
#     while m != i and n != j:
#         if b[m,n] == 9:
#             print(f'Match {x[i-1]}')
#             if b[]
            


# %%
# def print_lcs(b, x, y, i, j, change_count = 0):
#     if i ==0 or j == 0:
#         return change_count
#     if b[i,j] == 9:
#         return  print_lcs(b, x, y, i-1, j-1, change_count), 
#     elif b[i,j] == 2:
#         return  print_lcs(b,x,y,i-1,j, change_count + 1)
#     else:
#         return print_lcs(b,x,y,i,j-1, change_count + 1)

# %%


# %%
# test_LCS2('ABCBDAB', 'BDCABA')[1]

# %%
# print_lcs(test_LCS2('ABCBDAB', 'BDCABA')[1], 'ABCBDAB', 7, 6)

# %%
# print_lcs(test_LCS2('bffflooo','buffalo')[1], 'bffflooo', 'buffalo', len('bffflooo'), len('buffalo'))

# %%



