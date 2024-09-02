def eat(breakfast, lunch='ラーメン', dinner='カレー', *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

eat('トースト','パスタ','カレー',('アイス','チョコ','パフェ'))
