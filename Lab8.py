# %% [markdown]
# # Lab 8
# **Upload one file** to Gradescope: 
# * `Lab8.py` (which will be autograded)
# 
# **IMPORTANT**: Before uploading, be sure to comment out any code that might result in an error.
# ___

# %% [markdown]
# ### Huffman Codes
# ```
# HUFFMAN(C)
# n = |C|
# Q = C
# for i = 1 to n-1
#     allocate a new node z
#     z.left = x = EXTRACT-MIN(Q)
#     z.right = y = EXTRACT-MIN(Q)
#     z.freq = x.freq + y.freq 
#     INSERT(Q, z)
#     
# return EXTRACT-MIN(Q)
# ```
# 
# **Example**: 
# 
# |Characters | a | b | c | d | e | f |  
# |:--|:--:|:--:|:--:|:--:|:--:|:--:|  
# | Frequency | 45 | 13 | 12 | 16 | 9 | 5 |   
# 
# Given the 6 letters from `a` to `f` and their frequencies shown above, the HUFFMAN algorithm would produce these variable-length codes, shown in an ordered list:
# ```
# ['0', '101', '100', '111', '1101', '1100']
# ```
# 
# **Exercise**:
# 
# | Characters | T | U | V | W | X | Y | Z |  
# |:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|  
# | Frequency | 24 | 10 | 31 | 12 | 7 | 16 | 20 |   
# 
# * Apply the HUFFMAN algorithm (by hand) to find optimal variable-length codes for the letters `T` to `Z`. Their frequencies are shown above. Store the codes as strings in an ordered list called **`huff_codes`**.
# * Calculate **`huff_bit_ct`**, the total number of bits required to encode the text using `huff_codes`.
# * Calculate **`fixed_bit_ct`**, the number of bits required if a fixed-length binary code is used instead.

# %%
huff_codes = ['00', '1101', '10', '010', '1100', '011', '111']
huff_bit_ct = 322
fixed_bit_ct = 360

# %% [markdown]
# ### Generators
# Read the file `Generators.html` in Canvas Modules to learn about Python generators, then complete the following exercises.

# %% [markdown]
# **Create a generator function** called **`seq1(n)`** that returns the `n` terms in the finite sequence $a_1 = 1$, $a_n = 2a_{n-1}+5$, one at a time.
# ```
# seq1_gen = seq1(10)
# print(next(seq1_gen))
# print(next(seq1_gen))
# print(next(seq1_gen))
# print(next(seq1_gen))
# ```
# displays
# ```
# 1
# 7
# 19
# 43
# ```

# %%


# %%
# def seq1_rec(n):
#     if n ==1:
#         return 1
#     else:
#         return 2*seq1_rec(n-1) + 5

# def seq1(n):
#     k = 1
#     while k <= n:
#         yield seq1_rec(k)
#         k+=1


# %%
def seq1(n):
    yield 1
    k = 1
    j=1
    while j <= n:
        yield 2*k + 5
        k = 2*k +5
        j+=1

# %%


# %%
seq1_gen = seq1(10)
print(next(seq1_gen))
print(next(seq1_gen))
print(next(seq1_gen))
print(next(seq1_gen))

# %% [markdown]
# **Create a generator function** called **`seq2()`** that returns the terms in the infinite sequence $a_1 = 1$, $a_n = \left(a_{n-1}^2 - 2a_{n-1}+10 \right) \pmod {2003}$, one at a time.
# 
# $$\{1, 9, 73, 1187, \ldots \}$$

# %%
def seq2():
    yield 1
    k = 1
    while True:
        yield (k**2 - 2*k + 10) % 2003
        k = (k**2 - 2*k + 10) % 2003

# %%
seq2_gen = seq2()
print(next(seq2_gen))
print(next(seq2_gen))
print(next(seq2_gen))
print(next(seq2_gen))
seq2_gen.close()



# %% [markdown]
# **Create a generator function** called **`seq3()`** that returns the terms in the infinite sequence $a_1 = 1$, $a_2 = 2$, $a_n = a_{n-1} + 3a_{n-2}$, one at a time. 
# 
# $$\{1, 2, 5, 11, 26, \ldots \}$$

# %%
def seq3():
    yield 1
    yield 2
    j=1
    k = 2
    while True:
        yield k + 3*j
        j,k = k, k + 3*j
        


# %%
seq3_gen = seq3()
print(next(seq3_gen))
print(next(seq3_gen))
print(next(seq3_gen))
print(next(seq3_gen))
print(next(seq3_gen))
seq3_gen.close()

# %%



