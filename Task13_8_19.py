tickets = int(input('Ввести количество билетов: '))
price = []
for i in range(1,tickets + 1):
    age = int(input(f"Ввести возраст {i} клиента: "))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
    sale = int(sum(price) - sum(price)/100 * 10)
    print('При покупке более 3 билетов, общая стоимость со скидкой 10% составляет: ', sale)
else:
    sale = int(sum(price))
    print('Общая стоимость составляет: ', sale)