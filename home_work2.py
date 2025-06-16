inp = int(input('ENTER: '))

if 0 <= inp < 8640000:
    day = inp // (24 * 60 *60)
    hour = (inp // 3600) % 24
    mins = inp // 60 % 60
    sec = inp % 60

    if day == 1:
        day_word = 'день'
    elif 2 <= day % 10 <= 4 and not 12 <= day % 100 <= 14:
        day_word = 'дні'
    else:
        day_word = 'днів'

    print(f'{day} {day_word} {hour:02}:{mins:02}:{sec:02}')

else:
    print('number must be between 0 and 8639999')




