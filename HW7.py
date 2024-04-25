# %% [markdown]
# # HW 7
# 
# **Upload two files** to Gradescope: 
# * `HW7.ipynb` (run all cells to make sure that outputs are visible, especially plots)
# * `HW7.py` (which will be autograded)
# 
# ___

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# ### Binary Search Tree
# The code below defines the class **`BST`** which represents a binary search tree containing **`BSTNode`** objects. A `BST` object has the attribute
# * `root` which points to the `BSTNode` located at the root of the tree
# 
# and a `BSTNode` object has the attributes
# * `key`
# * `data`
# * `parent`
# * `left`
# * `right`.

# %%
class BSTNode:
    '''A node in a binary search tree'''
    def __init__(self, key, satellite):
        self.key = key
        self.data = satellite
        self.parent = None
        self.left = None
        self.right = None
    
    def keys(self):
        key_lst = []
        def inorder_walk(x):
            if x != None:
                inorder_walk(x.left)
                key_lst.append(x.key)
                inorder_walk(x.right)
        inorder_walk(self)
        return key_lst
            
    def search(self, key):
        if self == None or key == self.key:
            return self
        if int(key[4:]) < int(self.key[4:]):
            return self.left.search(key)
        else:
            return self.right.search(key)
        
class BST:
    '''Binary search tree containing BSTNodes'''
    def __init__(self, node):
        self.root = node
    
    def insert(self, node):
        prev = None
        curr = self.root
        while curr != None:
            prev = curr
            if node.key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        node.parent = prev
        if prev == None:
            self.root = node
        elif node.key < prev.key:
            prev.left = node
        else:
            prev.right = node


# %% [markdown]
# Add these `BSTNode` methods:
# * **`keys()`** returns a list of the keys in the BST (or subtree) in order starting with the given node. (Do not call a sort routine.)
# * **`search(key)`** returns the node corresponding to `key` or returns `None` if `key` is not found. The search begins with the given node and extends to its subtree.
# 

# %% [markdown]
# Add this `BST` method:
# * **`insert(node)`** inserts a new `BSTNode` into the tree in an appropriate position. No value is returned.
# 
# Example:<br>
# ```
# ralph = BSTNode('buff8039', 'Ralphie')
# pyth = BSTNode('pyth2022', 'Guido Von Rossum')
# marie = BSTNode('macu1234', 'Marie Curie')
# 
# tree = BST(ralph)
# tree.insert(pyth)
# tree.insert(marie)
# tree.root.keys(), pyth.search('macu1234').data
# ```
# returns
# ```
# (['buff8039', 'macu1234', 'pyth2022'], 'Marie Curie')
# ```
# 

# %%
ralph = BSTNode('buff8039', 'Ralphie')
pyth = BSTNode('pyth2022', 'Guido Von Rossum')
marie = BSTNode('macu1234', 'Marie Curie')

tree = BST(ralph)
tree.insert(pyth)
tree.insert(marie)

tree.root.keys(), pyth.search('macu1234').data

# %% [markdown]
# Add these `BSTNode` methods:
# * **`min()`** returns the node corresponding to the smallest key in the tree or subtree. The given node is the root.
# * **`max()`** returns the node corresponding to the largest key in the tree or subtree. The given node is the root.
# 
# Add the `BST` method:
# * **`successor(node)`** returns the successor to the given node.
# 

# %%
class BSTNode(BSTNode):

    def min(self):
        x = self
        while x.left != None:
            x = x.left
        return x
    
    def max(self):
        x = self
        while x.right != None:
            x = x.right
        return x

class BST(BST):

    def successor(self, node):
        k = node
        if node.right != None:
            return node.right.min()
        parent = node.parent
        while parent != None and k == parent.right:
            k = parent
            parent = parent.parent
        return parent

# %%
BSTNode(6,1).key

# %%
tree2 = BST(BSTNode(15,1))
tree2.insert(BSTNode(6,1))
tree2.insert(BSTNode(3,1))
tree2.insert(BSTNode(2,1))
tree2.insert(BSTNode(4,1))
tree2.insert(BSTNode(7,1))
tree2.insert(BSTNode(13,1))
tree2.insert(BSTNode(9,1))
tree2.insert(BSTNode(18,1))
tree2.insert(BSTNode(17,1))
tree2.insert(BSTNode(20,1))

# %%
tree2.root.min().key, tree2.root.max().key

# %%
tree2.successor(tree2.root).key

# %% [markdown]
# ### Insertion Sort
# Write a function **`insertion_sort(nums)`** that takes a list of numbers and uses the insertion sort algorithm to sort the numbers in place, modifying the `nums` argument. The function does not return a value.
# 
# For example,
# ```
# ints = [11, 13, 8, 7, 10]
# insertion_sort(ints)
# ints
# ```
# displays
# ```
# [7, 8, 10, 11, 13]
# ```

# %%
def insertion_sort(nums):
    for j in range(1,len(nums)):
        key = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i+1] = key

# %%
ints = [11,13,8,7,10]
insertion_sort(ints)
ints

# %% [markdown]
# ### Displaying Numbers as Bars
# Here is a sample bar chart with labels.

# %%
nums = [11, 13, 7, 8, 10, 16, 5, 6, 14, 3]
len(nums)

# %%
nums = [11, 13, 7, 8, 10, 16, 5, 6, 14, 3]

fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])

bars = ax.bar(range(len(nums)), nums)  
ax.bar_label(bars)
plt.show()

# %%
nums = [11, 13, 7, 8, 10, 16, 5, 6, 14, 3]
nums[5:]

# %%
nums = [11, 13, 7, 8, 10, 16, 5, 6, 14, 3]
fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])

fig, ax1 = plt.subplots()
ax1.set_xticks([])
ax1.set_yticks([])

bars = ax.bar(range(len(nums)), nums, color = 'gray')
# bars2 = ax.bar(range(0,5),nums[:5], color = 'b')  
bars3 = ax.bar(2,nums[2], color = 'y')
# bars4= ax.bar(5, nums[5], color = 'b')
ax.bar_label(bars)
# ax.bar_label(bars2)
# plt.show()
plt.show()

# %%
def insertion_sort_test(nums,j):
    key = nums[j]
    i = j - 1
    while i >= 0 and nums[i] > key:
        nums[i + 1] = nums[i]
        i -= 1
    nums[i+1] = key
    return key

# %%
ints = [11,13,8,7,10]
insertion_sort_test(ints,1)
ints

# %% [markdown]
# ### Insertion Sort Visualization
# Write a variation of `insertion_sort` called **`insertion_sort_viz(nums)`** which **displays the numbers as vertical bars** after each key is moved into its ordered position. The number of plots will match the number of elements in `nums`. Use one color for the sorted numbers on the left and a different color for the unsorted numbers on the right. The current `key` should be highlighted in a third color. Below is a sample plot after four iterations.
# 
# <img src = "http://www.coloradomath.org/python/insertion_sort_viz.jpg" width="450" height="300" />
# 

# %%
nums = [11, 13, 7, 8, 10, 16, 5, 6, 14, 3]

fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])

bars = ax.bar(range(len(nums)), nums, color = 'gray')  
ax.bar_label(bars)
ax.bar(1,13, color = 'b')
plt.show()

# %%
def insertion_sort_viz(nums):
    for j in range(0, len(nums)):
        insertion_sort_test(nums, j)
        plt.bar(j, nums[j], color = 'b') + plt.bar(range(j, len(nums)), nums[j:], color = 'gray')
        plt.show
        

# %%
def insertion_sort_viz2(nums):
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])

    bars = ax.bar(range(len(nums)), nums, color = 'gray')  
    ax.bar_label(bars)

    insertion_sort_test(nums, 1)
    #bars2 = 
    # for j in range(1,len(nums)):
    #     key = nums[j]
    #     i = j - 1
    #     while i >= 0 and nums[i] > key:
    #         nums[i + 1] = nums[i]
    #         i -= 1
    #     nums[i+1] = key
    #     bars2 = ax.bar(range(len(nums)), nums, color = 'b')  
    #     ax.bar_label(bars2)
    
    plt.show()

# %%
plt

# %% [markdown]
# **Run the visualization** on the `nums` list defined below.

# %%
nums = [25, 15, 30, 23, 10, 12, 27, 16]

# %%
insertion_sort_viz2(nums)

# %%
nums

# %%
insertion_sort_test(nums,0)
nums

# %%
[25, 15, 30, 23, 10, 12, 27, 16] == [15, 25, 30, 23, 10, 12, 27, 16]

# %%


# %%
nums = [25, 15, 30, 23, 10, 12, 27, 16]
for j in range(1, len(nums)):
    nums_prev = nums
    print(f'prev; {nums_prev}')
    insertion_sort_test(nums,j)
    print(f'{nums == nums_prev}')
    print(nums)
    

# %%
nums = [25, 15, 30, 23, 10, 12, 27, 16]
nums_prev = nums
nums_prev, insertion_sort_test(nums,4)
#print(nums == nums_prev)

# %%
nums

# %%
len(nums)

# %%
insertion_sort_viz(nums)

# %%



