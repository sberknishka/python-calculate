# calculator.py
class Calculator:
    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность двух чисел (a - b)."""
        # БАГ ДЛЯ СТУДЕНТОВ: Неверный порядок вычитания
        return b - a

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        # БАГ ДЛЯ СТУДЕНТОВ: Захардкоженный результат
        return 4.0

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное от деления a на b.
        При делении на ноль должен выбрасывать ValueError.
        """
        # БАГ ДЛЯ СТУДЕНТОВ: Вместо исключения возвращаем 0
        if b == 0:
            return 0.0
        return a / b
