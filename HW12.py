# %% [markdown]
# # HW 12
# 
# **Upload one file** to Gradescope: 
# * `HW12.py` (which will be autograded)
# ___

# %%
import math

# %% [markdown]
# ### Doublets 
# 
# The object of this puzzle (by Lewis Carroll 1879) is to convert a starting word into a target word, changing one character at a time, minimizing the number of changes and always forming a valid word with each letter change.
# 
# If the starting word is `PIG` and the target word is `STY`, a solution with 5 changes is 
# 
# PIG $\to$ BIG $\to$ BAG $\to$ SAG $\to$ SAY $\to$ STY.
# 
# Write a function **`doublet(start, target, wordlist)`** that returns a minimal solution, listing the words that lead to the target word. Assume that `start` and `target` have the same number of upper-case characters and no more than 5 characters. If there is no solution, return an empty list. If there is more than one minimal solution, return any of them. 
# 
# The function should use **breadth-first search**. Each valid word under consideration should be stored in a `WordNode` object (defined below) with the `word`, `parent`, and `dist` attributes set appropriately. The use of the `color` attribute is optional.
# 
# To check whether a word is valid, compare to the list of strings in `wordlist`. The list `wordlist` can be formed from the 3-letter words in `lexicon3_upper.txt`. A larger file containing 3-, 4-, and 5-letter words is `lexicon5_upper.txt`.
# 
# Example: `doublet('PIG', 'STY')` may return `['BIG', 'BAG', 'SAG', 'SAY', 'STY']`. There are other solutions such as `['PIN', 'PAN', 'PAY', 'SAY', 'STY']`.

# %%
class WordNode:
    def __init__(self, word):
        self.word = word
        self.parent = None
        self.color = 'white'
        self.dist = math.inf  # distance from source

# %%
with open('lexicon3_upper.txt', 'r') as fp:
    words_3 = fp.read().splitlines()



with open('lexicon5_upper.txt', 'r') as fp:
    words_5 = fp.read().splitlines()



# %%
words_3.sort()
words_5.sort()

# %%
def adj_word_lst(word, wordlist):
    word_lst = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(0, len(word)):
        for lttr in alpha:
            if word[:i] + lttr + word[i+1:] == word:
                pass
            elif word[:i] + lttr + word[i+1:] in wordlist:
                word_lst.append(word[:i] + lttr + word[i+1:])
            
    return word_lst

# %%
def doublet(start, target, wordlist):
    soln_lst = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    node_dict = {}

    source_node = WordNode(start)
    source_node.color = 'gray'
    source_node.dist = 0
    node_dict[start] = source_node

    queue = [start]
    
    
    #Loop to traverse all adjacent nodes
    while len(queue) != 0:
        #u = the next adjacent node in queue and removes it from queue
        
        u = queue.pop(0)
        #print(u)
        adj_u = adj_word_lst(u, wordlist)
        for i in adj_u:
            if i not in node_dict:
                new_node = WordNode(i)
                new_node.parent = node_dict[u]
                new_node.dist = node_dict[u].dist +1
                node_dict[i] = new_node
                queue.append(i)
                #print(len(queue), i)
        
    if target not in node_dict:
        return []
    else:     
        curr_node = node_dict[target]
        while curr_node.parent != None:
            soln_lst.append(curr_node.word)
            curr_node = curr_node.parent

    return soln_lst[::-1]

# %%
doublet('PIG', 'STY', words_3)

# %%



