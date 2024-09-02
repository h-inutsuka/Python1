def leap_year(year):
    if year % 400 == 0:
        print(f'西暦{year}年は、うるう年です')
    elif year % 100 == 0:
        print(f'西暦{year}年は、うるう年ではありません')
    elif year % 4 == 0:
        print(f'西暦{year}年は、うるう年です')
year = int(input('現在の西暦>>'))
leap_year(year)
