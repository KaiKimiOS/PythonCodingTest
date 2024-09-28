leftMoney = 1000 - int(input())

count = 0
coins = [500,100,50,10,5,1]
for i in coins:
    count += leftMoney // i
    leftMoney %= i
    
    
    

print(count)