listprice = int(input('定価を入力してください>>'))
consumptiontaxrate = int(input('消費税率を入力してください>>'))
priceincludingtax = listprice * (consumptiontaxrate / 100 + 1)
print(listprice)
print(consumptiontaxrate)
print(priceincludingtax)