import numpy as np

def coin_changing(coins, total):
        
    T = [0 if idx == 0 else float("inf") for idx in range(total +1)]
    R = [-1 for _ in range(total + 1)]
    
    for j in range(len(coins)):
        for i in range(1, total+1):
            coin = coins[j]
            
            if i >= coin:
                if T[i] > 1 + T[i - coin]:
                    T[i] = 1 + T[i - coin]
                    R[i] = j
     
    print_coins(R, coins)                       
    
    
def print_coins(R, coins):
    
    result = []
    start = len(R) - 1
    
    if R[start] == "-1":
        print("No Solution!!")
        return
    
    while start > 0:
        coin = coins[R[start]]
        result.append(coin)
        start -= coin
        
    print(*result)