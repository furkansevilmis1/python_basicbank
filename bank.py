

bakiye = 500

while True:

    istek = input(' 1-Para Çek \n 2-Para Yatır \n 3-Bakiye Öğren \n 4-Çıkış Yap')


    if istek == '1':
        paracek = int(input('çekmek istediğiniz miktarı belirtiniz'))
        bakiye-=paracek
        print(f'yeni bakiyeniz {bakiye} TL') 


    elif istek == '2':
        parayatir = int(input('Yatırmak İstediğiniz miktarı belirtiniz'))
        bakiye+=parayatir
        print(f'yeni bakiyeinz {bakiye} TL')

    elif istek == '3':
        print(f'bakiyeniz{bakiye} TL')

    elif istek == '4':
        print('Başarıyla çıkış yaptınız')
        break
        