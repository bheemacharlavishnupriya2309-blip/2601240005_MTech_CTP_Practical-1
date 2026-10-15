
n = int(input("Enter number of applications: "))
W = int(input("Enter resource capacity: "))

wt, val = [], []

for i in range(n):
    wt.append(int(input(f"Resources for App {i+1}: ")))
    val.append(int(input(f"Revenue for App {i+1}: ")))

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]

        if wt[i - 1] <= w:
            dp[i][w] = max(
                dp[i][w],
                val[i - 1] + dp[i - 1][w - wt[i - 1]]
            )

selected = []
w = W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(i)
        w -= wt[i - 1]

selected.reverse()

print("\nMaximum Revenue:", dp[n][W])
print("Selected Applications:", selected)

print("\nDP Table:")
for row in dp:
    print(row)

print("\nTime Complexity: O(n * W)")
print("Space Complexity: O(n * W)")

