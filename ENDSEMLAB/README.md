# Experiment 8: 0/1 Knapsack Using Dynamic Programming

## 1. Problem Statement

A cloud service provider has a limited amount of computing resources. Each application requires a specific amount of resources and generates a certain revenue. Each application can either be deployed completely or not deployed.

**Task:** Implement the 0/1 Knapsack Dynamic Programming algorithm to maximize revenue within the available resource capacity.

The program must display:

* Maximum revenue.
* Selected applications.
* Dynamic Programming (DP) table.
* Time complexity.
* Space complexity.

## 2. Aim

To implement the 0/1 Knapsack problem using Dynamic Programming to maximize the total revenue obtained from selected applications without exceeding the available computing resource capacity.

## 3. Algorithm

1. Start the program.
2. Read the number of applications and the available resource capacity.
3. Read the resource requirement and revenue of each application.
4. Create a DP table of size `(n + 1) × (capacity + 1)`, initialized with zeros.
5. Traverse each application and each possible resource capacity.
6. If the current application's resource requirement is less than or equal to the available capacity, calculate the maximum revenue by either:

   * Excluding the current application.
   * Including the current application.
7. Store the maximum of these two values in the DP table.
8. If the application requires more resources than the available capacity, copy the result from the previous row.
9. The last cell of the DP table gives the maximum revenue.
10. Trace back through the DP table to identify the selected applications.
11. Display the maximum revenue, selected applications, DP table, time complexity, and space complexity.
12. Stop the program.

## 4. Python Code

```python
def knapsack(resources, revenues, capacity):
    n = len(resources)

    # Create the DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if resources[i - 1] <= w:
                include = revenues[i - 1] + dp[i - 1][w - resources[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected applications
    selected = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            selected.append(i)
            remaining_capacity -= resources[i - 1]

    selected.reverse()

    # Display results
    print("\n========== 0/1 KNAPSACK RESULTS ==========")

    print("\nMaximum Revenue:", dp[n][capacity])

    print("\nSelected Applications:")

    if selected:
        for i in selected:
            print(
                f"Application {i} - Resources: {resources[i - 1]}, "
                f"Revenue: {revenues[i - 1]}"
            )
    else:
        print("No applications selected.")

    total_resources = sum(resources[i - 1] for i in selected)

    print("\nTotal Resources Used:", total_resources)
    print("Available Resource Capacity:", capacity)

    # Display the DP table
    print("\nDynamic Programming Table:")

    print("       ", end="")
    for w in range(capacity + 1):
        print(f"{w:3}", end="")
    print()

    for i in range(n + 1):
        if i == 0:
            label = "App 0"
        else:
            label = f"App {i}"

        print(f"{label:<8}", end="")

        for w in range(capacity + 1):
            print(f"{dp[i][w]:3}", end="")
        print()

    # Display complexity
    print("\nTime Complexity: O(n × W)")
    print("Space Complexity: O(n × W)")


# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of applications: "))
    capacity = int(input("Enter the available resource capacity: "))

    resources = []
    revenues = []

    print("\nEnter resource requirement and revenue for each application:")

    for i in range(n):
        print(f"\nApplication {i + 1}")

        resource = int(input("Resources: "))
        revenue = int(input("Revenue: "))

        if resource <= 0:
            raise ValueError("Resource requirements must be positive.")

        if revenue < 0:
            raise ValueError("Revenue cannot be negative.")

        resources.append(resource)
        revenues.append(revenue)

    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    knapsack(resources, revenues, capacity)
```


## 5. Input

Example input:

```text
Enter the number of applications: 4
Enter the available resource capacity: 7

Enter resource requirement and revenue for each application:
Application 1 - Resources: 1
Application 1 - Revenue: 1
Application 2 - Resources: 3
Application 2 - Revenue: 4
Application 3 - Resources: 4
Application 3 - Revenue: 5
Application 4 - Resources: 5
Application 4 - Revenue: 7
```

## 6. Output

```text
========== 0/1 KNAPSACK RESULTS ==========

Maximum Revenue: 9

Selected Applications:
Application 2 - Resources: 3, Revenue: 4
Application 3 - Resources: 4, Revenue: 5

Total Resources Used: 7
Available Resource Capacity: 7

Dynamic Programming Table:
          0  1  2  3  4  5  6  7
App 0:    0  0  0  0  0  0  0  0
App 1:    0  1  1  1  1  1  1  1
App 2:    0  1  1  4  5  5  5  5
App 3:    0  1  1  4  5  6  6  9
App 4:    0  1  1  4  5  7  8  9

Time Complexity: O(n × W)
Space Complexity: O(n × W)
```

Here, `n` represents the number of applications and `W` represents the available resource capacity.

## 7. Time and Space Complexity

### Time Complexity: O(n × W)

The algorithm processes every application for each possible resource capacity. Therefore, the total number of operations is proportional to `n × W`.

### Space Complexity: O(n × W)

The algorithm stores the results in a two-dimensional DP table containing `(n + 1) × (W + 1)` entries.

Where:

* `n` = Number of applications.
* `W` = Available resource capacity.

## 8. Conclusion

The 0/1 Knapsack problem was successfully implemented using Dynamic Programming. The algorithm determines the combination of applications that produces the maximum revenue without exceeding the available computing resource capacity. The DP table avoids repeated calculations and helps identify the optimal selection of applications.

## 9. Viva Questions and Answers

### 1. What is the 0/1 Knapsack problem?

The 0/1 Knapsack problem is an optimization problem in which each item is either selected completely or rejected. The objective is to maximize the total value without exceeding the available capacity.

### 2. Why is Dynamic Programming used in the Knapsack problem?

Dynamic Programming stores previously calculated results and avoids solving the same subproblems repeatedly.

### 3. What is the time complexity of the 0/1 Knapsack algorithm?

The time complexity is O(n × W), where `n` is the number of applications and `W` is the resource capacity.

### 4. What does the DP table represent?

Each entry `dp[i][w]` represents the maximum revenue obtainable using the first `i` applications with a resource capacity of `w`.

### 5. How are the selected applications identified?

The algorithm traces backward through the DP table. If the current value differs from the value in the previous row at the same capacity, the corresponding application is selected, and its resource requirement is subtracted from the remaining capacity.
