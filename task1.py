import timeit
coins=[50, 25, 10, 5, 2, 1]

def find_coins_greedy(goal):
    result={}
    for coin in coins: # У циклі намагаємося використати найбільшу за номіналом монету
        if goal>=coin: # якщо монета менша або дорівнює  залишку
            amnt_coins=goal//coin # кількість монет - цілочисельне ділення
            result[coin]=amnt_coins # додаємо номінал і необхідну кількість монет до результату
            goal=goal%coin # залишок - залишок цілочисельного ділення
    return result

print("Greedy coins: ")
print(find_coins_greedy(113))

def find_min_coins(goal):
    # будуємо таблицю монет для суми менше за goal для кожної монети
    K=[]
    r_coins=coins[:]
    r_coins.reverse()
    K = [[(0,{})  for i in range(goal + 1)]  for c in r_coins]
    for id, coin in enumerate(r_coins): # для монет
        for i in range(goal+1): # для сум решти < goal
            
            if i != 0:
                amnt_coins = i // coin
                rest = i % coin
                if rest !=0:
                    rest_coins=K[id-1][rest]
                    coins_list=dict(rest_coins[1])
                    if amnt_coins != 0:                        
                        coins_list[coin]= amnt_coins
                        sum_coins=amnt_coins * coin + rest_coins[0]
                    else:
                        sum_coins=rest_coins[0]
                    K[id][i]=(sum_coins,coins_list)
                else:
                    K[id][i]=(i,{coin : amnt_coins})
    
    return K[len(r_coins)-1][goal]

print("Dynamic coins")
print(find_min_coins(113)[1])


execution_time = timeit.timeit(lambda: find_coins_greedy(113), number=1)
print(f"| find_coins_greedy         | {execution_time:22e} |")
execution_time = timeit.timeit(lambda: find_min_coins(113), number=1)
print(f"| find_min_coins            | {execution_time:22e} |")

execution_time = timeit.timeit(lambda: find_coins_greedy(1113), number=1)
print(f"| find_coins_greedy         | {execution_time:22e} |")
execution_time = timeit.timeit(lambda: find_min_coins(1113), number=1)
print(f"| find_min_coins            | {execution_time:22e} |")