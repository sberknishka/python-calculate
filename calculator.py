# calculator.py
class Calculator:
    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность двух чисел (a - b)."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное от деления a на b.
        При делении на ноль должен выбрасывать ValueError.
        """
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b
