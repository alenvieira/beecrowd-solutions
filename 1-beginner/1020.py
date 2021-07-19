days = int(input())
years = int(days / 365)
days =  days % 365
months = int(days / 30)
days = days % 30
print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))
