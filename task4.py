boy = float(input('Boyunuzu qeyd edin: '))
ceki = float(input('Cekinizi qeyd edin: '))

BKI = ceki / boy * boy

if BKI < 18.5:
    x = 'Zeif'

elif 18.5 <= BKI < 25:
    x = 'Normal'

elif 20 <= BKI < 30:
    x = 'Kilolu'

elif BKI > 30:
    x = 'Obez'

print(x)