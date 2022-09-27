def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# Driver code
val = []
wt = []
W = int(input("Enter capacity of knapsack "))
WT = int(input("Enter number of weights "))
for i in range(WT):
    x = int(input("Enter Weight "))
    y = int(input("Enter Profit "))
    wt.append(x)
    val.append(y)
    
n = len(val)
print("\nMaximum Profit in knapsack can be ", knapSack(W, wt, val, n))