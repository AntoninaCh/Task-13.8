price = [0, 990, 1390] #Прайс на биллеты
ticket_price = []   #Цены на биллеты в соостветствии с указанным возрастом

while True:
    ticket = int(input('Введите желаемое количество билетов _'))
    if ticket > 0:
        for i in range(1, ticket + 1):
            age = int(input(f'Введите возраст участника Билета №{i} - '))
            if age < 18 :
                ticket_price.append(price[0])
            elif 18 <= age < 25:
                ticket_price.append(price[1])
            elif age > 25:
                ticket_price.append(price[2])

        def total(ticket):
                if ticket <= 3:
                    return sum(ticket_price)
                else:
                    return int(sum(ticket_price) - sum(ticket_price) * 10 / 100)

        print()
        print(f'Сумма к оплате за {ticket} биллета(ов) составляет : {total(ticket)} руб.')
        break
    else:
        print()
        print('!Количество биллетов должно быть больше нуля!')
        print()




