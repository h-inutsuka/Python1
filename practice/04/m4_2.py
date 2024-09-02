print('カレーを召し上がれ')
is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f'{count}皿のカレーを食べました')
    key = input('おかわりいかがですか？(y/n)>>')
    if key == 'n':
        is_awake = False
print('ごちそうさまでした')