# Week 03 Homework - More Practice with NumPy and Pandas

In class we saw ways to leverage the NumPy and Pandas packages to speed up our calculations. To use these libraries and their data structures effectively,
we often need to abandon the purely "Pythonic" way of doing things (usually with for-loops) and use the bespoke approaches provided by these libraries instead.

This week's homework will give you more practice refactoring code to take advantage of these approaches.

## Files in this Directory


- `poisson_solver.py`: the main numerical code. This file builds the problem, assembles the matrix, solves it, and returns the result.
- `poisson_demo.py`: a small script that runs the solver and visualizes the results.

Please put your answers to the assignment below in `answers.md`. Be sure to commit and push all changes to the files in this directory.

## Assignment

For this homework, you'll need a Linux command line with your `hpc-python` environment loaded.

### NumPy Practice

In this week's workbook, you got some practice refactoring a list-based program to use NumPy arrays.
This homework builds on that theme, asking you to refactor a NumPy-based program that could use
NumPy more effectively.

1. A warmup: Python 3.5 introduced the `@` operator to the usual set of math operations (`+`, `-`, `*`, `/`, `**` and the like). In a Python interpreter or Jupyter notebook, create the following arrays: `A = np.arange(25).reshape(5,5)` and `b = np.arange(5)`. What's the difference between `A * b` and `A @ b`?
2. We'll be revisiting the 2D Poisson sovler from your first homework. In that assignment, you hopefully identified the `solve_dense_system` functions as the slowest part of the code. Rewrite this function to remove for-loops over `j` and instead use NumPy array slicing. Hint: in eliminating these loops, you may find that you are multiplying together a matrix and a vector just like in question 1. How many times faster is this refactor?
3. Are we paying the "NumPy array creation time tax" with this refactor? Why or why not? How does this explain our speed gains?
4. You could attempt to employ more clever NumPy tricks to further remove `if` statements and `for` loops, but we should really take a step back and think about the goal `solve_dense_system` is trying to achieve. Recall that `solve_dense_system` is an implementation of the Gaussian elimination algorithm. 
    1. What is this algorithm trying to achieve? Are there tools in NumPy (perhaps the [linear alegbra](https://numpy.org/doc/stable/reference/routines.linalg.html) module) that could maybe do it better? 
    2. In the `solve_poisson_problem` function, replace the call to `solve_dense_system` with your chosen NumPy routine. How many times faster is this version compared to the original? Compared to our slice refactor?
    3. Why is this NumPy routine so much faster? You might want to read more about the `linalg` module for answers.

### Pandas Practice

This week's workbook introduced Panda's `apply` for applying complex functions to Pandas arrays.
Using `apply` is neater than iterative over rows (either using a `for` loop or the Pandas `iterrows`
and `itertuples` methods) but can at time be slower. While it was faster for the least squares example
from the workbook, it is slower for the example in this homework set.

1. Time the current version of the code, which uses `apply()`.
2. What kind of data object is `order`, the sole argument of `discounted_total`?
3. Instead of operating row by row with `apply`, the calculation in `discounted_total` is simple enough that we can *vectorize* it using entire columns, quite like we can operate with NumPy arrays.
4. In class, we used `apply` to perform ordinary least squares on each row. Do you think you could replace the use of `apply` with vectorized column operations? Would you want to? What circumstances might change your mind?

## Instructor's AI Disclosure

I used VS Code Copilot to preview a possible refactor for question 2, which is what lead to the development of question 1. I then double checked that there weren't any more easy/obvious refactors possible to encourage you to explore before asking question 4.

For the Pandas section, I asked Copilot for advice on common Pandas mistakes/misuses because I am only an occasional Pandas user. I used these ideas to have it generate the example data and code in the repository.