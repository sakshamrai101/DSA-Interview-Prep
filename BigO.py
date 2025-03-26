def tricky(n):
    op = 0
    while n > 0:
        for i in range(n):
            op += 1
        n = int(n/2)
