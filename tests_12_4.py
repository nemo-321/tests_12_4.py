import unittest
import logging
from rt_with_exceptions import Runner

# Настройка логирования
# level=logging.INFO` — устанавливает уровень логирования на INFO, что значит, что будут записываться все сообщения уровня INFO и выше.
#`filemode="w"` — создаёт новый файл для логов или перезаписывает существующий.
#`filename="runner_tests.log"` — имя файла, в который будут записываться логи.
#`encoding="UTF-8"` — кодировка файла.
#`format` — формат записываемых сообщений в лог.

logging.basicConfig(level=logging.INFO,filemode="w",filename="runner_tests.log",encoding="UTF-8",
                    format="%(asctime)s / %(levelname)s / %(message)s")

class RunnerTest(unittest.TestCase):

    # Тест метода `walk`
    # Этот метод тестирует функциональность метода `walk` класса `Runner`.
    # Создаётся объект `runner_walk` с именем `'Runner1'` и отрицательной скоростью `-5`.
    # Запускается цикл, который вызывает метод `walk()` 10 раз.
    # Проверяется, что после 10 вызовов расстояние (`distance`) равно 50.
    # Если возникает `ValueError`, например, из-за неверной скорости, это записывается в лог с уровнем WARNING.

    def test_walk(self):
        try:
            runner_walk = Runner('Runner1',-5)
            for i in range(10):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
    # Тест метода `run`
    # Этот метод тестирует функциональность метода `run`.
    # Создаётся объект `runner_run` с числом `123` в качестве имени.
    # Запускается цикл, который вызывает метод `run()` 10 раз.
    # Проверяется, что расстояние равно 100.
    # Если возникает `TypeError`, это также записывается в лог.

    def test_run(self):
        try:
            runner_run = Runner(123)
            for i in range(10):
                runner_run.run()
            self.assertEqual(runner_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)

if __name__ == '__main__':
    unittest.main()





