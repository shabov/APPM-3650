# %% [markdown]
# # HW 5
# 
# **Upload one file** to Gradescope: 
# * `HW5.py` (which will be autograded)
# 
# ___

# %%
import random
import numpy as np
import operator

# %% [markdown]
# ### Postfix Notation

# %% [markdown]
# In *postfix notation* (also called *reverse Polish notation*), mathematical expressions are written with the operators following the operands (numbers). Postfix notation has these advantages over the standard infix notation:
# * It eliminates the need for parentheses and operator precedence rules.
# * It can be evaluated easily using a stack.
# 
# Below are examples of expressions written in infix and postfix notation. When converting from infix to postfix, the numbers remain in the same order but the operators are moved so that they immediately follow their operands.
# 
# |Infix|Postfix|  
# |:--|:--|  
# |`4 - 7`|`4 7 -`|  
# |`4 - (7 + 5)` | `4 7 5 + -` |  
# |`(7 - 5) * (4 + 10)`|`7 5 - 4 10 + *`|  
# |`(45 - 7 * 5 + 3)`|`45 7 5 * - 3 +`|  
# 
# Here is how postfix expressions are evaluated. The operators are processed one at a time, beginning with the leftmost operator and moving right. Each operator is applied to the previous two values. The result may be used by the next operator.
# 
# |Postfix|Evaluation| |Value|  
# |:--|:--|:--|:--|  
# |`4 7 -`| | |`-3`|  
# |`4 7 5 + -`|`4 12 -` | |`-8`|   
# |`7 5 - 4 10 + *`|`2 14 *` | |`28`|  
# |`45 7 5 * - 3 +`|`45 35 - 3 +` | `10 3 +` | `13`|
# 
# 
# 
# 
# 

# %% [markdown]
# **Convert these infix expressions to postfix** by hand, observing the standard operator precedence rules. Write your answers in the form of a string with spaces separating the numbers and operators.

# %%
infix1 = '10 - 6 + 3 * 8'
infix2 = '10 - (6 + 3 - 8)'
infix3 = '10 - (6 + 3) * 8'

# %%
postfix1 = '10 6 - 3 8 * +'
postfix2 = '10 6 3 + 8 - - '
postfix3 = ' 10 6 3 + 8 * -'

# %% [markdown]
# **Determine the numerical values of these postfix expressions** by hand.

# %%
postfix4 = '10 6 3 8 + - +'
postfix5 = '10 6 3 / + 8 *'
postfix6 = '10 6 * 3 + 8 -'

# %%
postfix4_value = 5
postfix5_value = 96
postfix6_value = 55

# %% [markdown]
# ### Postfix Evaluator
# Write a function **`eval_postfix(expr)`** that takes a postfix expression in string format, evaluates it, and returns its numerical value. The possible operators are `+`, `-`, `*`, and `/`. Assume that all numbers are non-negative integers. You may assume that `expr` is a valid postfix expression with spaces separating the numbers and operators.
# 
# The function should use the `Stack` class defined below to process `expr` as follows:
# * Each number in the string should be pushed onto a stack.
# * Each operator in the string should be applied to the top two numbers on the stack. The result of the operation should be pushed onto the stack.
# 
# *Hint:* You may wish to make use of these functions from the `operator` module: `operator.add`, `operator.sub`, `operator.mul`, and `operator.truediv`. When applied to two arguments, they return the same values as `+`, `-`, `*`, and `/`, respectively.
# 
# Example:<br>
# `eval_postfix('4 7 5 + -')` returns `-8`<br>
# `operator.add(7, 5)` returns `12`

# %%
class Stack:
    '''Create a stack using a list'''
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        '''Return the element at the top of the stack if possible. Otherwise print an error message and return None'''
        try:
            return self.items.pop()
        except:
            print('ERROR: Empty Stack')
            return None

    def size(self):
        return len(self.items)
        
    def peek(self):
        try:
            return self.items[-1]
        except:
            print('ERROR: Empty Stack')
            return None

    def empty(self):
        if self.size()==0:
            return True
        else:
            return False

# %%
def eval_postfix(expr):
    #expr = expr.replace(' ', '')
    expr1 = expr.split(' ')
    num_stack = Stack()
    for i in expr1:
        try:
            num_stack.push(int(i))
        except:
            b = num_stack.pop()
            a = num_stack.pop()
            op_dict = {'+': operator.add(a,b), '-': operator.sub(a,b), '/': operator.truediv(a,b), '*':operator.mul(a,b)}
            num_stack.push(op_dict[i])

    return num_stack.peek()



# %%
eval_postfix('4 7 5 + -')

# %%
str1 = '7 5 - 4 10 + *'
str1.split(' ')

# %%
lst = list(' 7 5 - 4 10 + *')
lst

# %%
eval_postfix('4 7 -'), eval_postfix('7 5 - 4 10 + *')

# %% [markdown]
# ___
# 
# ### Nodes
# Below is a class `Node` that will store a key and data, along with links to neighboring nodes in a `DLinkedList`. 

# %%
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

# %% [markdown]
# ### DLinkedList
# Use the `DLinkedList` class (defined in a previous assignment) with the  attribute:
# * **`head`** 
# 
# and the  methods:
# * **`insert`**, **`delete`**, **`search`**, **`keys`**.

# %%
class DLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, node):
        if node.next == None and node.prev == None:
            self.head = None
        elif node.next == None:
            node.prev.next = None
        elif node.prev == None:
            node.next.prev = None
            self.head = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def search(self, value):
        if self.head == None:
            return None
        node = self.head
        while node.next != None:
            if node.key == value:
                return node
            else:
                node = node.next
        if node.key == value:
            return node
        else:
            return None


    def keys(self):
        key_lst = []
        if self.head == None:
            return None
        node = self.head
        while node.next != None:
            key_lst.append(node.key)
            node = node.next
        key_lst.append(node.key)
        return key_lst        


# %% [markdown]
# ### Free Ski Pass Giveaway
# 
# A free ski pass will be awarded to a lucky CU student. Students who sign up for this free giveaway will be arranged in a line. Then every $k$th student will be eliminated, one at a time, until the lucky winner is left. For example, suppose $k=3$ and there are 10 students named A, B, ..., J. Then eliminating every 3rd student (with wraparound) produces this result with student D as the winner.
# ```
# A B C D E F G H I J
# A B   D E   G H   J
# A     D E     H   J
#       D E         J
#       D           J
#       D                   
# ```
# 
# Write a function **`giveaway(participants, k)`** that takes a list of participant names, simulates this procedure for a positive integer `k`, and returns the name of the winner. The function should store the names as keys in a `DLinkedList`, then eliminate the participants by removing their corresponding nodes, one at a time.
# 
# Example:<br>
# `giveaway(list('ABCDEFGHIJ'), 3)` returns `'D'`.

# %%
def if_last(node, linklst):
    if node.next == None:
        return linklst.head
    else:
        return node.next

# %%
def giveaway(participants, k):
    ct = 0
    part_linklst = DLinkedList()
    for n in range(len(participants)-1, -1,-1):
        j = Node(participants[n], n)
        part_linklst.insert(j)
    #print(part_linklst.keys())
    curr_node = part_linklst.head
    while len(part_linklst.keys()) > 1:
        for i in range(k-1):
            curr_node = if_last(curr_node, part_linklst)
        #print(f'Curr = {curr_node.key}')
        part_linklst.delete(curr_node)
        curr_node = if_last(curr_node, part_linklst)
        ct+=1
        # print(f'{ct}')
        #print(f'{part_linklst.keys()}')
    return (part_linklst.keys()[0])


        

# %%
giveaway(list('ABCDEFGHIJ'),4)

# %% [markdown]
# Read in the file **`giveaway_names.txt`** which contains the names of 100 participants, one name on each line. Store the names in a list called **`participant_names`**. Then `giveaway(participant_names, 7)` should return `'Lennox'`.

# %%
with open('giveaway_names.txt', 'r') as give:
    participant_names = give.read().split('\n')[:-1]
giveaway(participant_names, 7)

# %%



