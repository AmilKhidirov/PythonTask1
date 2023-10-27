names = ['Amil', 'Tamerlan', 'Feyruz', 'Gulsare']

add = int(input('Ad daxil edin (1): '))

if add == 1:
    a = input('Ad daxil edin: ')
    names.append(a)
    print('Ad Bazaya ugurla elave olundu ')
    print(names)

if a == '':
    print('Ad daxil etmediniz')


elif len(a) > 15:
    print('Ad cox uzundur maksimum 15 herf')