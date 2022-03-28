stock_prices = [10,8,5,2,3,4,5,1,2,6]
n = len(stock_prices) 

i =0
max_profit =0
while i < n-1 :
    #find local minima
    while ((i<n-1) and (stock_prices[i+1]<=stock_prices[i])) :
        i =i+1
    if(i==n-1):
        break 
    local_minima = stock_prices[i]
    i = i+1
    #local maxima
    while ((i<n-1) and (stock_prices[i]>=stock_prices[i-1]) ):
        i=i+1
    if (i==n-1):
        local_maxima = stock_prices[n-1]
    else :
        local_maxima = stock_prices[i-1]
    curr_profit = local_maxima -local_minima 
    if curr_profit > max_profit :
        max_profit = curr_profit
print(max_profit)
