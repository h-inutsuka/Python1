japanese = int(input('国語の点数を入力してください>>'))
arithmetic = int(input('算数の点数を入力してください>>'))
science = int(input('理科の点数を入力してください>>'))
socialstudies = int(input('社会の点数を入力してください>>'))
english= int(input('英語の点数を入力してください>>'))
scores = {japanese,arithmetic,science,socialstudies,english,}
total = sum(scores)
avg = total / int(len(scores))
print(f'合計{total}点、平均{avg}点')