n = int(input("enter the N="))
a = []
for i in range(n):
    print("enter the array values=")
    values = list(map(int, input().split()))
    a.append(tuple(values))

w = int(input("enter the weight="))
a.sort(key=lambda x: x[0] / x[1], reverse=True)

ans = 0
for i in range(n):
    if w >= a[i][1]:
        ans += a[i][0]
        w -= a[i][1]
    else:
        vw = a[i][0] / a[i][1]
        ans += vw * w
        w = 0
        break

print(int(ans))
