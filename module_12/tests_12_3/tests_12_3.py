import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('')     # Создаем объект Runner с произвольным именем
        for i in range(10):     # Вызываем метод walk 10 раз
            runner.walk()
        self.assertEqual(runner.distance, 50)       # Проверяем, что distance равно 50

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('')     # Создаем объект Runner с произвольным именем
        for i in range(10):     # Вызываем метод run 10 раз
            runner.run()
        self.assertEqual(runner.distance, 100)      # Проверяем, что distance равно 100

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print({i: runner.name for i, runner in i.items()})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(list(results.values())[-1] == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(list(results.values())[-1] == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tournament = Tournament(90, self.runner2, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(list(results.values())[-1] == self.runner3)


if __name__ == "__main__":
    unittest.main()