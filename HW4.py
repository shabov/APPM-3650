# %% [markdown]
# # HW 4
# 
# **Upload one file** to Gradescope: 
# * `HW4.py` (which will be autograded)
# 
# ___

# %%
import numpy as np

# %% [markdown]
# ### Polynomials
# A polynomial $P(x)$ can be represented by an array of coefficients in *increasing* degree order. Examples are shown in this table:
# 
# | &nbsp; &nbsp; &nbsp; Polynomial &nbsp; &nbsp; &nbsp;|Coefficients|  
# |:---------:|:--:|
# |$8 - 6x + x^2$|`array([8, -6, 1])`|
# |$8 + x^2$|`array([8, 0, 1])`|
# |$- 6x + x^2$|`array([0, -6, 1])`|
# |$8$|`array([8])`|
# 

# %% [markdown]
# **Use the `Polynomial` class defined below** for the following problems. 
# 
# **Add the following methods**:
# * **`__call__(x)`** evaluates the polynomial $P$ for a given value of $x$. It allows the use of the `P(x)` syntax. (You may use Horner's Method but it's not necessary.)
# * **`deriv()`** returns the derivative of $P(x)$ as a `Polynomial` with degree one less than $P$.
# 
# For example,
# ```
# poly = Polynomial([8, -6, 1])
# poly(-1)
# ```
# returns `15` and
# ```
# vars(poly.deriv())
# ```
# returns `{'coeffs': array([-6,  2]), 'degree': 1}`.
# 
# (*Optional:* You may add other methods to this class.)
# 
# 

# %%


# %%
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = np.array(coeffs)
        self.degree = self.coeffs.size - 1
        
    def __call__(self, x):
        result = 0
        for coef in reversed(self.coeffs):
            result  = coef + x*result
        return result

    def deriv(self):
        new_coeffs = []
        for k in range(len(self.coeffs)):
            new_coeffs.append(self.coeffs[k] * k)
        return Polynomial(new_coeffs[1:])
    
    def __repr__(self):
        string_rep =''
        for i in range(self.degree+1):
            if i == 0:
                string_rep += f'{self.coeffs[i]} '
                if self.coeffs[i+1] > 0:
                    string_rep+= '+ '
                else:
                    string_rep+='- '
            elif i ==1:
                string_rep+=f'{abs(self.coeffs[i])}x '
                try:
                    if self.coeffs[i+1] > 0:
                        string_rep += '+ '
                    else:
                        string_rep += '- '
                except:
                    string_rep+=' '
            else:
                string_rep+= f'{abs(self.coeffs[i])}x^{i} '
                try:
                    if self.coeffs[i+1] > 0:
                        string_rep+='+ '
                    else:
                        string_rep += '- '
                except:
                    string_rep+=' '
        return string_rep



# %%
poly = Polynomial([8,-6,1])
poly

# %%
j = np.array([8,-6,1])
j=np.array(j[1:])
len(j)

# %%
lst = [1,2,3,4,5]
lst[::-1]

# %% [markdown]
# ### Newton's Method for Polynomials

# %% [markdown]
# Newton's Method is an iterative algorithm for finding a root of a differentiable function $f(x)$. Given an initial guess of $x_0$, the method converges to a solution by repeatedly applying this formula: 
# 
# $$ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$
# 
# When Newton's Method converges, it usually does so quickly, however it does not always converge, for example, when $f'(x_n) = 0$.
# 
# Write an iterative function **`newton(poly, x0, tol=1e-4, max_iter=50)`** that uses Newton's Method to find a root of a `Polynomial` $P(x)$ given an initial guess `x0`. The method terminates when $\lvert P(x_n)\rvert$ is less than the tolerance `tol`. If the method has not converged after `max_iter` iterations, the function returns `None`.

# %%
def newton(poly, x0, tol=1e-4, max_iter = 50):
    f_x = poly
    f_x_deriv = f_x.deriv()
    x_n = x0
    iter_ct = 0
    while abs(f_x(x_n)) >= tol and iter_ct <= max_iter:
        if f_x_deriv(x_n) == 0:
            print(f'Deriviative equals 0')
            return None
        x_n = x_n - (f_x(x_n)/f_x_deriv(x_n))
        iter_ct+=1
    if iter_ct > max_iter:
        return None
    return x_n


# %%
newton(Polynomial([30,-11,-4,1]),10)

# %%
newton(Polynomial([-1,0,-1,1]),1,1e-4,3)

# %% [markdown]
# ### Recursive Newton's Method
# **Write a recursive version** of the previous function called **`newton_rec()`**.

# %%
def newton_rec(poly, x0,tol=1e-4, ):
    poly_deriv = poly.deriv()
    if abs(poly(x0)) <= tol:
        return x0
    else:
        return newton_rec(poly, x0 - (poly(x0)/poly_deriv(x0)),tol)


# %%
newton_rec(Polynomial([30,-11,-4,1]),10)

# %%
newton_rec(Polynomial([-1,0,-1,1]),5,1e-1)

# %% [markdown]
# ### Bisection Method for Polynomials
# The *bisection method* is an alternate way to find a root of a `Polynomial`. Write a function **`bisection(poly, interval, tol=1e-4, max_iter=50)`** that uses **binary search** to find a root of $P(x)$. Begin with a closed interval $[a, b]$ represented by a 2-element tuple `(a, b)`. If $P(a)$ and $P(b)$ are opposite signs, then a root is guaranteed to exist in interval $[a, b]$ because $P(x)$ is continuous. 
# 
# The method repeats these steps until a root is found (within the tolerance) or `max_iter` is reached:
# * Calculate the midpoint of the interval. If it corresponds to a root, return the root.
# * If the midpoint is not a root, repeat the process using either the left half or the right half of the interval.
# 
# The function returns `None` if $P(a)$ and $P(b)$ are not opposite signs.
# 
# (*Hint:* You may wish to use `np.sign(val)` which returns 1, 0, or -1, depending on whether `val` is positive, zero, or negative, respectively.)

# %%
def bisection(poly, interval, tol=0.0001, max_iter=50):
    #print(f'int ={interval}, iter={max_iter}')
    if np.sign(poly(interval[0])) == np.sign(poly(interval[1])) and max_iter !=0:
        return None
    mid = (interval[0]+interval[1])/2
    #print(f'mid ={mid}, val= {abs(poly(mid))}')
    if abs(poly(mid)) < tol:
        return mid
    elif np.sign(poly(interval[0])) != np.sign(poly(mid)):
        return bisection(poly, (interval[0], mid), tol, max_iter= max_iter-1)
    elif np.sign(poly(mid)) != np.sign(poly(interval[1])):
        return bisection(poly, (mid,interval[1]), tol, max_iter = max_iter-1)
    #print(f'{interval}, {max_iter},{mid}, {abs(poly(mid))}')

# %%
bisection(Polynomial([-2,-1,0,1]),(-2,10))

# %%



