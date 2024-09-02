for i in range(9):
    for j in range(9):
        if i % 2 == 0:
            print(f'{(i+1)*(j+1)}\t', end='')
            if (i+1)*(j+2) > 50:
                break
    print('')