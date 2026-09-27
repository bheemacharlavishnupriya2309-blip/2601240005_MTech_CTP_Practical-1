# Backtracking

## 1. Objective

To solve a problem using the **Backtracking technique**, where possible solutions are built step by step and invalid choices are abandoned as soon as they are detected.

## 2. Algorithm

1. Start with an empty solution.
2. Select a possible choice for the current position.
3. Check whether the selected choice is valid.
4. If the choice is valid, add it to the current solution.
5. Recursively continue with the next position.
6. If a complete solution is obtained, store or display it.
7. If the current choice does not lead to a solution, remove it.
8. Try the next possible choice.
9. Continue until all possible choices are explored or the required solution is found.

## 3. Input

The input depends on the particular backtracking problem.

For example, for the **N-Queens problem**:

* An integer `N` representing the number of queens and the size of the chessboard.

## 4. Output

The program displays the valid solution(s) obtained using the backtracking technique.

For example, for N-Queens, the output represents the positions of `N` queens such that no two queens attack each other.

## 5. Time Complexity

The time complexity depends on the problem.

For the **N-Queens problem**, the worst-case time complexity is approximately:

**O(N!)**

This is because the algorithm may need to explore a large number of possible arrangements before finding valid solutions.

## 6. Space Complexity

The space complexity is approximately:

**O(N)**

for the recursion stack and storing the current solution.
