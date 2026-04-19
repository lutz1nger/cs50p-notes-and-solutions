x = input('What is the Answer to the Great Question of Life, the Universe and Everythink? ')

if x.replace(' ','') == '42' or x.lower().replace('-','').replace(' ','') == 'fortytwo':
    print('Yes')
else:
    print('No')
