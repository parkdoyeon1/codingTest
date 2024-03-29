import sys
import heapq
n = int(sys.stdin.readline())
heap = []

for i in range (n):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) ==0 :
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, data)