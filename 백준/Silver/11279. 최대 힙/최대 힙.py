import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for i in range(n):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-data, data))
