# 問題１
n = int(input('数値を入力 >>'))
isError = n < 0 or n > 100
if isError == False and n < 100:
    print('条件成立')
# /問題１
# 問題２
number = int(input("数字を入力してください>>"))
if number % 2 == 0 :
    print('偶数！')
elif number % 2 == 1:
    print('奇数！')
# /問題２

# 問題３
greeting = input('こんにちは>>')
if greeting == 'こんにちは':
    print('こうこそ！')
elif greeting == '景気は？':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で！')
else:('どうしました？')
# /問題３