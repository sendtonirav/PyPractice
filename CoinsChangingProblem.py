import sys


def getChange(coins, total):
    # print(coins, total)
    memo = {}
    memocoin = {}
    val = getChangeHelper(coins, total, memo, memocoin)
    
    if(total in memocoin):
        print memo[total]
        print memocoin[total]
    else:
        print("No way")

def getChangeHelper(coins, total, memo, memocoin):
    
    #print("getChangeHelper({})".format(total))
    
    if total <= 0 :
        return sys.maxsize
    
    if total in memo :
        #print("Retruning from memo[{}]={}".format(total, memo[total]))
        return memo[total]
        
    
    if total in coins :
        memo[total] = 1
        memocoin[total] = [total]
        # print memocoin
        return 1
    
    min = sys.maxsize
    mincoin = sys.maxsize
    
    
    for coin in coins :
        if(total-coin) > 0:
            temp = getChangeHelper(coins, total-coin, memo, memocoin)
            if temp < min:
                min = temp
                mincoin = coin

    # print total
    memo[total] = (min+1)
    # if(total not in memocoin):
    #     print ("in {}".format(total))
    #     memocoin[total] = []
    if mincoin < sys.maxsize:
        memocoin[total] = memocoin[total-mincoin] + [mincoin]
    
    # print(memocoin[total])
    return (min+1)
        
    
    
    
    
    
    
getChange([3,5], 6)
