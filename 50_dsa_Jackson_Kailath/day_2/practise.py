"""
1) Understand the problem -> print 321123
2) Identify subproblem -> print 2112 
3) Trust | Faith 
4) Link 1 & 2 -> print 3 2112 3
5) Base condition -> for 0, return

Psuedocode 

function seq(n) 
{
if n == 0: return 
print(n)
seq(n-1)
print(n) 
}
seq(3)

If it work for n, it will work for n-1 as well --> recursive leap of faith.
"""

def seq(n):
    if n == 0: return
    print(n, end='')
    seq(n-1)
    print(n, end='')

seq(3)
print("\ndone.\n")
"""
Factorial : 
5 ! = 5 * 4 * 3 * 2 * 1

"""
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(5) )
"""
Psuedocode:
function(n):
{
if n is equal to 1: return 1 
return function(n-1) * n
}
function(5)
LIFO 
F(5) --> 24 * 5 --> 120 
|
F(4) --> 6 * 4 
|
F(3) --> 2 * 3
|
F(2) --> 1 * 2
|
F(1) --> 1

"""

"""
Difference between Iteration and Recursion: 
--> Things done recursively can also be done Iteratively 
--> Does not use Recursive call stack space [better space complexity]
--> Recursion --> uses more auxillary space.
--> Recursion --> Ascending phase (calling phase) --> Descending phase (returning phase)
--> But Iteration has only Ascending phase no descending. 

Ways to write Base condition:
when to stop recursively calling itself and start returning 
|-> Last Valid Input |-> First invalid input |

Recurrence Relation: 
Expresses the solution of a problem as a function of the solutions of the smaller instance of the same problem. 
eg. for finding factorial of positive integer n 
  F(n) = n * F(n-1)
"""