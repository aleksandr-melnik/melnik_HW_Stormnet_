class Store:
    def __init__(self, title="Магазин на диване"):
        self.title = title
        self.storage = {}
    def add_product(self, product, number_of_products=1):
        if product in self.storage:
            self.storage[product] += int(number_of_products)
        else:
            self.storage[product] = int(number_of_products)
    def _product_details(self, product):
        message_template = " Количество товара % s: % s штук, стоимость: % s . Суммарная стоимость: % s  "
        product_count = self.storage[product]
        product_title = product.title
        product_price = product.price
        product_total_price = product_price * product_count
        rendered_message = message_template % (product_title, product_count, product_price, product_total_price)
        return rendered_message
    def showcase(self, product=None):
        if product:
            print(self._product_details(product))
        else:
            for product in self.storage.keys():
                print(self._product_details(product))
