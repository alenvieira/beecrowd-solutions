n = int(input())
results = []
for _ in range(n):
    v1, v2, v3 = input().split(' ')
    results.append(((float(v1) * 2) + (float(v2) * 3) + (float(v3) * 5))/10)
for result in results:
    print('{:.1f}'.format(result))
