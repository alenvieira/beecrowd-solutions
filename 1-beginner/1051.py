salary = float(input())
msg = 'Isento'
if salary > 2000 and salary <= 3000:
    msg = 'R$ {:.2f}'.format((salary - 2000) * 0.08)
elif salary > 3000 and salary <= 4500:
    msg = 'R$ {:.2f}'.format(((salary - 3000) * 0.18) + 80)
elif salary > 4500:
    msg = 'R$ {:.2f}'.format(((salary - 4500) * 0.28) + 80 + 270)
print(msg)
