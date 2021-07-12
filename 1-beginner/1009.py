seller_name = input()
fixed_salary = float(input())
total_sale = float(input())
commission = total_sale * 0.15
total_salary = fixed_salary + commission
print('TOTAL = R$ {:.2f}'.format(total_salary))
