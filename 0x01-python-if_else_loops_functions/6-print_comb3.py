#!/usr/bin/python3
for i in range(10):
    for num in range(10):
        if i < num:
            if i == 8 and num == 9:
                print('{:d}{:d}'.format(i, num), end='\n')
            else:
                print('{:d}{:d},'.format(i, num), end=' ')
