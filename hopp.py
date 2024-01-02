while True:
    n = input("Enter 0 <= n <= 10 (enter 'Q' to quit): ")
    if n.upper() == 'Q':
        break
    n = int(n)
    m = input("Enter the value for 'm': ")
    m = int(m)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            if result % m == 0:
                print('H', end='\t')
            else:
                print(result, end='\t')

        print()


