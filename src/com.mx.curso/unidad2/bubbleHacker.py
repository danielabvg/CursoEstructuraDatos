def countswaps(a):
    n = len(a)
    swaps = 0

    #i de 0 a n-1, j de 0 a n-2
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    if n > 0:
        print(f"First Element: {a[0]}")
        print(f"Last Element: {a[-1]}")
    else:
        print("First Element: ")
        print("Last Element: ")

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    countswaps(a)



