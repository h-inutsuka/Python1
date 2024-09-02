def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
        return names

before_names = ['松田', '浅木', '工藤']
copied_names = list()
for n in before_names:
    copied_names.append(n)
after_names = add_suffix(copied_names)
print('さん付の後:' + after_names[0])
print('さん付の前:' + before_names[0])
