n = int(input())
implement_count = 0
for _ in range(n):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        implement_count += 1
print(implement_count)
