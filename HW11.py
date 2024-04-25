# %% [markdown]
# # HW 11
# 
# **Upload one file** to Gradescope: 
# * `HW11.py` (which will be autograded)
# 
# ___

# %%
from collections import Counter

# %% [markdown]
# ### Counting Frequencies
# An inefficient way to count the letter frequencies in a string is to call `.count()` for each letter of the alphabet.
# 
# A more efficient method is to use a `Counter` which is a subclass of `dict`. Documentation can be found here: https://docs.python.org/3/library/collections.html#collections.Counter.
# 
# Example:
# ```
# from collections import Counter
# ct = Counter()
# ct.update('banana')
# ct.update('bun')
# ct
# ```
# returns 
# ```
# Counter({'b': 2, 'a': 3, 'n': 3, 'u': 1})
# ```
# which can be used like a dictionary. To sort by most frequent to least frequent, call
# ```
# ct.most_common()
# ```
# which will return the list
# ```
# [('a', 3), ('n', 3), ('b', 2), ('u', 1)]
# ```

# %% [markdown]
# ### Flatland
# 
# The file `'flatland.txt'` contains the text of the book *Flatland* by Edwin A. Abbott, which is a satire about Victorian England. Its main characters are geometric shapes. **Calculate the frequencies** of the 26 letters of the alphabet in the text using a `Counter`. Save the result in **`flatland_freq`**.
# 
# * For space efficiency, **read the file line by line**. For example:
# ```
# with open('flatland.txt') as fp:
#     for line in fp:
#         ...
# ```
# * Use `.isalpha()` to distinguish letters from non-alphabetic characters.
# * Use `.lower()` to convert upper case characters to lower case.

# %%
alphabet = 'abcdefghijklmnopqrstuvwxyz' 
curr_str = ''

with open('flatland.txt') as fp:
    for line in fp:
        for char in line:
            if char.isalpha():
                curr_str += char.lower()

flatland_freq = Counter()

flatland_freq.update(curr_str)

# %% [markdown]
# ### Flatland Fixed-Length Encodings
# Suppose the letters in the alphabet are represented using fixed-length ternary (base 3) codes. **Calculate the total number of ternary digits needed** to encode the 26 letters in *Flatland* (converting upper case letters to lower case). Store the result in `flatland_digit_ct_fixed`.
# 
# For example, the first 5 letters of the alphabet can be represented as two-digit base 3 numbers: `a=00`, `b=01`, `c=02`, `d=10`, and `e=11`. Then the encoding for the word `aced` would require 8 digits: `00021110`.

# %%
flatland_digit_ct_fixed = 445932
#a=000 b=001 c=002 d=010 e=011 f=012 g=020 h=021 i=022 j=100 k=101 l=102 m= 110 n=111 o=112 p=120 q=121 r= 122 s = 200 t=201 u = 202 v=210 w=211 x=212 y=220 z=221

# %%
flatland_freq.values()

# %%
sum1 = 0
for i in list(flatland_freq.values()):
    sum1 += 3*i
sum1

# %% [markdown]
# ### Huffman Code
# 
# Write a function **`huffman(char_freq)`** that takes a Counter containing `ch: freq` key-value pairs representing letter frequencies, and **returns a dictionary** containing the ternary encodings for the characters. The dictionary keys will be the characters, and the values will be the base 3 encodings in string format. Assume that there are at least 3 characters in `char_freq`.
# 
# The algorithm will use a **ternary tree** (instead of a binary tree) composed of `HuffNode`s (defined below) with each node having up to 3 children. The children should be arranged from left to right in order of increasing frequency. (It is not necessary for the function to implement an efficient min-priority queue; it may call `sorted()`.)
# 
# **Note**: An optimal encoding can be found if the number of characters is odd. If there is an even number of characters, add a dummy character `'@'` with frequency 0. This will ensure that the root will have 3 children.
# 
# **Example**: 
# ```
# char_freq = Counter({'a': 45, 'b': 10, 'c': 18, 
#                      'd': 48, 'e': 22, 'f': 33})
# huffman(char_freq)
# 
# ```
# returns (in some order)
# ```
# {'b': '211', 'f': '22', 'a': '0', 'd': '1', 'c': '212', 'e': '20'}
# 
# ```

# %%
class HuffNode:
    def __init__(self, ch, freq):
        self.char = ch  # set to '' if internal node
        self.freq = freq
        self.parent = None
        self.left = None
        self.middle = None
        self.right = None

# %%
def extract_min(sorted_vals):
    min_val = sorted_vals[-1]
    sorted_vals.pop(-1)
    return min_val


# %%
def create_parent(sorted_vals):
    new_parent = HuffNode('',0)
    x = extract_min(sorted_vals)
    y = extract_min(sorted_vals)
    z = extract_min(sorted_vals)

    new_parent.left = x[0]
    new_parent.middle = y[0]
    new_parent.right = z[0]
    new_parent.freq = x[1] + y[1] + z[1]

    sorted_vals.append((new_parent, new_parent.freq))
    sorted_vals = sorted(sorted_vals, key = lambda x: x[1], reverse = True)

# %%
def node_children(node):
    char_nodes = []
    children_node = []

    if type(node.left) == str:
        char_nodes.append((node.left, 'L'))
    else:
        children_node.append((node.left, 'L'))
    if type(node.middle) == str:
        char_nodes.append((node.middle, 'M'))
    else:
        children_node.append((node.middle, 'M'))

    if type(node.right) == str:
        char_nodes.append((node.right, 'R'))
    else:
        children_node.append((node.right, 'R'))
    
    return (children_node, len(children_node) == 0), (char_nodes, len(char_nodes) == 0)
    


# %%
def tree_search(node):
    running = node_children(node)[0][1]
    huff_encoding = '0'
    lst1 = []
    not_visted = []
    while running == False:
        chars = node_children(node)[1][0]
        children = node_children(node)[0][0]
        for ch in chars:
            if ch[0] == '@':
                pass
            else:
                if ch[1] == 'L':
                    lst1.append((ch[0], int(huff_encoding)))
                if ch[1] == 'M':
                    lst1.append((ch[0], int(huff_encoding)+1))

                if ch[1] == 'R':
                    lst1.append((ch[0], int(huff_encoding)+2))

        running = node_children(node)[0][1]
        if len(children) == 1:
            node = children[0][0]
            last_en = children[0][1]
            if last_en == 'R':
                huff_encoding = str(int(huff_encoding) + 2) + '0'
            elif last_en == 'M':
                huff_encoding = str(int(huff_encoding)+1) + '0'
            else:
                huff_encoding += '0'
        else:
            running = True
    
    dict_freq = {}
    for i in lst1:
        dict_freq[i[0]] = i[1]
    return dict_freq

            
    

# %%
# def two_node_helper(node_lst, huff_encoding):
#     node1 = node_lst[0][0]
    
    
    

# %%
def huffman(char_freq):
    if len(char_freq) % 2 == 0:
        sorted_vals = char_freq.most_common() + [('@',0)]
    else:
        sorted_vals = char_freq.most_common()
    N = len(sorted_vals)
    for i in range(0, N//2):
       create_parent(sorted_vals)
       sorted_vals = sorted(sorted_vals, key = lambda x: x[1], reverse = True)
    return  tree_search(extract_min(sorted_vals)[0])

# %%
char_freq = Counter({'a': 45, 'b': 10, 'c': 18, 'd': 48, 'e': 22, 'f': 33})
huffman(char_freq)


# %% [markdown]
# 

# %% [markdown]
# ### Flatland Encodings
# Call `huffman(flatland_freq)` and store the result in `flatland_huffman_codes`.

# %%
flatland_huffman_codes = {'e': 0,
 't': 1,
 'o': 20,
 'a': 21,
 'i': 220,
 'n': 221,
 's': 2220,
 'r': 2221,
 'h': 22220,
 'l': 22221,
 'd': 222220,
 'u': 222221,
 'c': 2222220,
 'm': 2222221,
 'f': 22222220,
 'y': 22222221,
 'g': 222222220,
 'w': 222222221,
 'p': 2222222220,
 'b': 2222222221,
 'v': 22222222220,
 'k': 22222222221,
 'x': 222222222220,
 'q': 222222222221,
 'j': 2222222222220,
 'z': 2222222222221}
flatland_huffman_codes

# %% [markdown]
# **Calculate the number of ternary digits needed** to encode the letters in *Flatland* (converted to lower case) using `flatland_huffman_codes`. Store the result in `flatland_digit_ct_huffman`.

# %%
flatland_digit_ct_huffman = 592314

# %%



