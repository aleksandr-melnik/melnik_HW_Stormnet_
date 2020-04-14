import json
from product import Product
from store import Store
class Manager:
    store = None
    @staticmethod
    def create_product():
        title = input('Название товара: ')
        price = input('Цена за единицу товара: ')
        try:
            return Product(title=title, price=price)
        except EnterError:
            print("Неверно указана цена! Требуется повторить ввод")
            return Manager.create_product()
    @staticmethod
    def create_store():
        if Manager.store is None:
            store_title = input('Введите название магазина: ')
            Manager.store = Store(title=store_title)
        return Manager.store
    @staticmethod
    def create_add_to_store_products():
        need_to_create_a_product = True
        while need_to_create_a_product:
            answer = input('Требуется создать продукт? Y/N: ')
            if answer.lower() == 'y':
                need_to_create_a_product = True
                product = Manager.create_product()
                product_count = int(input('Количество едениц продукта %s: ' % product.title))
                Manager.store.add_product(product=product, number_of_products=product_count)
            else:
                need_to_create_a_product = False
    @staticmethod
    def dump_data_to_file():
        store_product_list = open("store_product_list.txt", "w")
        data_dict = {
            'store_title': Manager.store.title,
            'storage': []
        }
        for product, mumber_of_products in Manager.store.storage.items():
            product_title = product.title
            product_price = product.price
            product_count = mumber_of_products
            data_dict['storage'].append((product_title, product_price, product_count))
        json.dump(data_dict, store_product_list)

    @staticmethod
    def load_data_from_file():
        store_product_list = open("store_product_list.txt", "r")
        data = json.load(store_product_list)
        Manager.store = Store(title=data['store_title'])

        for record in data['storage']:
            product = Product(title=record[0], price=record[1])
            Manager.store.add_product(product=product, number_of_products=record[2])
        print('Список товаров успешно создан!')
        Manager.store.showcase()

