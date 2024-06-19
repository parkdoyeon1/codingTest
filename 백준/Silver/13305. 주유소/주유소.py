n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

total_distance = sum(road)
total_cost = 0
min_price = price[0]

for i in range(n-1):
    total_cost += min_price * road[i]

    if price[i+1] < min_price:
        min_price = price[i+1]

last_fuel = total_distance - sum(road[:n-1])
total_cost += min_price * last_fuel
print(total_cost)