# CMPS 2200 Assignment 5
## Answers

**Name:** Jack Zemke


Place all written answers from `assignment-05.md` here for easier grading.

**1a)** 
  - Start with the highest denomination of coin $\leq N$. Subtract this denomination from $N$ as many times as possible such that $N$ remains positive. Once $N \gt$ that denomination, go to the next largest denomination $\leq N$. Repeat this process until $N$ is 0.

**1b)** 
  - Because the coins are in powers of 2, they are all denominations of each other (for example, 2 is a denomination of 4, but 3 is not a denomination of 5). Because of this property, the greedy property will yield an optimal solution.
  - The greedy choice property essentially states that a locally optimal choice leads to a globally optimal solution. In other words, when employing a greedy strategy, at each step, one should choose the option that seems the best at that moment, and this should eventually lead to the best overall solution. 
  
    - In the case of the coins, we can prove its optimality through the greedy choice property. We will prove by contradiction. Assume that there is an optimal solution that does not follow the greedy choice property. That would mean that there is a solution such that a different sequence of denominations is more optimal. However, this is not possible. Because the coins are in denomniations of $2^n$, it will always be optimal to use the largest possible denominations at each step. Therefore, the greedy choice property holds. 

  - The optimal substructure property states that an optimal solution to the problem contains optimal solutions to subproblems. In this context, the optimal substructure property implies that if we find the optimal solution for the remaining amount after choosing the largest denomination at each step, the entire solution must be optimal for the original amount $N$.

    - Proof by contradiction: Assume that the greedy algorithm does not yield an optimal solution for $N$. This implies that there exists another solution requiring fewer coins than the solution obtained using the greedy algorithm. Now, let's consider the first step where the greedy algorithm differs from the "optimal" solution. Suppose the optimal solution chooses a smaller denomination at this step. This would yeild a less optimal solution, because it would reqiure more coins. Thus, we reach a contradiction. By finding the optimal solution for the remaining amount after choosing the largest denomination at each step, we have found an optimal solution to the total problem.

**1c)** 
  - Work: In the worst possible case, we require one denomination of every coin. In this case, the work would be $O(n)$
  - Span: Because this problem must be solved sequentially, it cannot be parallelized. Therefore, the span is the same as the work at $O(n)$

**2a)**
 - Say you want change for $7$. Fortuito national bank has the denominations $(1,3,4,5)$ The greedy approach to this problem would first pick a 5, followed by 2 x 1s. Therefore, the greedy approach yields a result with 3 coins. However, the optimal solution is to select a 3 and a 4, for a result using 2 coins. 

 **2b)**
  - The optimal substructure property states that an optimal solution to the problem contains optimal solutions to subproblems. This is different from the greedy choice property in that the greedy choice property is more concerned with the locally optimal solution whereas the optimal substructure property is more concerned with all of the optimal solutions to the subproblems and how they can be combined into the globally optimal solution.
 - This problem has the optimal substructure property because the globally optimal solution is made up of optimal solutions to the problem's subproblems. These subproblems are the remaining balance after a given denomination is subtracted from the running balance. By utilizing the optimal substructure property, a dynamic programming approach would return a solution for the problem in 2a using 2 coins because it would analyze all of the subproblems and select the optimal combination to yield a globally optimal solution. 

 **2c)** Utilizing a bottom up approach for the example in 2a, we will compute the optimal solutions for the balance of $1, then $2, then $3, etc. This will be done using "solution sharing." For example, we know that the optimal way to get $1 is to use 1 coin with value 1. To get the optimal solution for $2, we can select 1 coin of value $1, then for the remaining balance of $1, we found the optimal solution for that value previously, 1. So the optimal solution for $2 is 2. we will do this for all values up to 7. To prove that this returns the optimal solution, I will walk through the solution to $7. First we try the biggest coin, 5. We are left with a remaining balance of $2, and using a previously computed optimal solution for a balance of $2 we know that 2 more coins (2 x $1) will be required. We will store 3 coins as a solution. Next we consider the next subproblem where we try the next coin, 4. We are left with a remaining balance of $3, and using a previously computed optimal solution for a balance of $3 we know that only one more coin is required (1 x $3). This yeilds a solution using 2 coins, which will overwrite the previous solution which used 3 coins and thus yeild the most optimal solution. I only considered 2 cases for this example, but in practice the algorithm will compare all possible subproblems to find the globally optimal solution.
  - We know that the work of a dynamic programming algorithm is equal to the number of subproblems considered multiplied by the amount of work that each subproblem does. For this implimentation, there will be at most $kn$ subproblems for a problem producing change for a value of $n$. Each subproblem does constant work, so the work of this implimentation is $O(kn)$
  - The longest chain of dependancies in this DAG is of depth $O(n)$. Because each node does constant work, the span is $O(n)$.

