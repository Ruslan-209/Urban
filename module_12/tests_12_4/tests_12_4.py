import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('noName', -5)     # Создаем объект Runner с произвольным именем
            for i in range(10):     # Вызываем метод walk 10 раз
                runner.walk()
            self.assertEqual(runner.distance, 50)       # Проверяем, что distance равно 50
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            runner = Runner(2)     # Создаем объект Runner с произвольным именем
            for i in range(10):     # Вызываем метод run 10 раз
                runner.run()
            self.assertEqual(runner.distance, 100)      # Проверяем, что distance равно 100
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner1 = Runner('1')       # Создаем два объекта Runner с разными именами
        runner2 = Runner('2')       # Создаем два объекта Runner с разными именами
        for i in range(10):         # 10 раз у объектов вызываются методы run и walk
            runner1.run()
            runner1.walk()
        for i in range(10):         # 10 раз у объектов вызываются методы run и walk
            runner2.run()
            runner2.walk()
        self.assertNotEqual(runner1, runner2)       # метод assertNotEqual, чтобы убедится в неравенстве результатов


if __name__ == "__main__":
    unittest.main()

