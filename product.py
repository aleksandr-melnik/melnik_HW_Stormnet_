class Product:
    def __init__(self, title, price):
        #assert int(price) > 1000, 'Ошибка'
        if int(price) > 1000 or int(price) <= 0:
            raise EnterError('Неверно указана цена! Повторите ввод.')
        self.title = title
        self.price = int(price)
