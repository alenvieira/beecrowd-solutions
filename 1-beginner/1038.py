price_list = { 1 : 4.0, 2 : 4.5, 3 : 5.0, 4 : 2.0, 5 : 1.5}
values = input()
product_code, price_product = [int(value) for value in values.split(' ')]
print('Total: R$ {:.2f}'.format(price_list[product_code] * price_product))
