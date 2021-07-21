a, b = [int(value) for value in input().split(' ')]
msg = "Nao sao Multiplos"
if a % b == 0 or b % a == 0:
    msg = "Sao Multiplos"
print(msg)
