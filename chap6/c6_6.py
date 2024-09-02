scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print(f'scores1の先頭要素は{scores1[0]}')
print(f'scores2の先頭要素は{scores2[0]}')
scores1 = scores2
scores1[0] = 90
print(f'scores1の先頭要素は{scores1[0]}')
print(f'scores2の先頭要素は{scores2[0]}')