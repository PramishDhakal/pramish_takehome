import unittest

from main import Greeter


class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world, This is my take home assignment!')


if __name__ == '__main__':
    unittest.main()
