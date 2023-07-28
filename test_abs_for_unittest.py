# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

# Suppose this is foo.py

# Объяснение как работает if __name__ == "__main__"
# print("before import")
# import math
#
# print("before function_a")
# def function_a():
#     print("Function A")
#
# print("before function_b")
# def function_b():
#     print("Function B {}".format(math.sqrt(100)))
#
# print("before __name__ guard")
# if __name__ == '__main__':
#     function_a()
#     function_b()
# print("after __name__ guard")

# Изменили тест выше, что бы запустить его с помощью unittest

import unittest
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual (abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")