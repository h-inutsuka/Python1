price = input('料金入力>>')
price = int(price)
number = input('人数入力>>')
number = int(number)
payment = price / number
payment = int(payment)
print('お支払いは' + str(payment) + '円です')