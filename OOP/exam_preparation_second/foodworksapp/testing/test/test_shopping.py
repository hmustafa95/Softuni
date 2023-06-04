from OOP.exam_preparation_second.foodworksapp.testing.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shoppingcart = ShoppingCart('Walmart', 500)
        self.shoppingcart.products = {'toy': 10}

    def test_correct_init(self):
        self.assertEqual('Walmart', self.shoppingcart.shop_name)
        self.assertEqual(500.00, self.shoppingcart.budget)
        self.assertEqual({'toy': 10}, self.shoppingcart.products)

    def test_shop_name_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.shop_name = '3'
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ve.exception))

    def test_shop_name_setter_correct(self):
        self.shoppingcart.shop_name = 'Boo'
        self.assertEqual('Boo', self.shoppingcart.shop_name)

    def test_add_to_cart_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.add_to_cart('ball', 110.00)
        self.assertEqual("Product ball cost too much!", str(ve.exception))

    def test_add_to_cart_correct(self):
        result = self.shoppingcart.add_to_cart('ball', 10)
        self.assertEqual({'toy': 10, 'ball': 10}, self.shoppingcart.products)
        self.assertEqual("ball product was successfully added to the cart!", result)

    def test_remove_from_cart_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.remove_from_cart('ball')
        self.assertEqual("No product with name ball in the cart!", str(ve.exception))

    def test_remove_from_cart_correct(self):
        result = self.shoppingcart.remove_from_cart('toy')
        self.assertEqual({}, self.shoppingcart.products)
        self.assertEqual("Product toy was successfully removed from the cart!", result)

    def test_add(self):
        other_instance = ShoppingCart('CBA', 300)
        result = self.shoppingcart.__add__(other_instance)
        self.assertEqual("WalmartCBA", result.shop_name)
        self.assertEqual(800.00, result.budget)
        self.assertEqual({'toy': 10}, result.products)
        self.assertEqual(result, result)

    def test_buy_products_error(self):
        self.shoppingcart.budget = 5
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.buy_products()
        self.assertEqual('Not enough money to buy the products! Over budget with 5.00lv!', str(ve.exception))

    def test_buy_products_correct(self):
        result = self.shoppingcart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 10.00lv.', result)


if __name__ == '__main__':
    main()
