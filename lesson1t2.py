# Пользователь вводит время в секундах.Переведите время в часы, минуты и секунды и
# выведите в формате чч: мм:сс.Используйте форматирование строк.

time = int(input('Введите время в секундах: '))
print(f'{time // 3600:02d}:{time % 3600 // 60:02d}:{time % 60:02d}')
