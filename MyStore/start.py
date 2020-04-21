from MyStore.manager import Manager
if __name__ == '__main__':
    print('Создаем магазин')
    Manager.create_store()
    print('Создаем список товаров')
    Manager.create_add_to_store_products()
    Manager.dump_data_to_file()
    Manager.load_data_from_file()
    print('Магазин %s успешно создан' % Manager.store.title)


