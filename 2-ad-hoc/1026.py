while True:
    try:
        l, r = list(map(int, input().split()))
        print(l ^ r)
    except EOFError:
        break
