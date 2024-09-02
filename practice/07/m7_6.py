# (1)
print('数当てゲームを始めます。3桁の数を当ててください!')
# (2)
# answer = []
import random
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.sample(l, 3))
answer = random.sample(l, 3)
print(answer)
# (3)
go_on = 1
while go_on == 1:
    prediction = []
    prediction.append(int(input('1桁目の予想を入力(0~9>>)')))
    prediction.append(int(input('2桁目の予想を入力(0~9>>)')))
    prediction.append(int(input('3桁目の予想を入力(0~9>>)')))
    print(prediction)
# (4)
    hit = 0
    blow = 0
    for i in range(3):
        if answer[-1 + i] == prediction[-1 + i]:
            hit = hit + 1
        elif answer[-1 + i] in (prediction):
            blow = blow + 1
    print(f'{hit}ヒット！{blow}ボール！')
# (5)
    if hit == 3:
        print('正解です！')
# (6)
    else:
        go_on = int(input('「続けますか？1:続ける2:終了>>」'))
# (7)
    while go_on == 2:
        break