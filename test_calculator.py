
import pytest

from calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Свежий экземпляр калькулятора для каждого теста."""
    return Calculator()


def test_add(calc: Calculator) -> None:
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0


def test_subtract(calc: Calculator) -> None:
    assert calc.subtract(5.0, 3.0) == 2.0
    assert calc.subtract(1.0, 5.0) == -4.0


def test_multiply(calc: Calculator) -> None:
    assert calc.multiply(3.0, 3.0) == 9.0
    assert calc.multiply(-2.0, 4.0) == -8.0


def test_divide(calc: Calculator) -> None:
    assert calc.divide(10.0, 2.0) == 5.0


def test_divide_by_zero(calc: Calculator) -> None:
    # Тест ожидает ошибку ValueError при делении на ноль
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)


# ---------------------------------------------------------------------------
# Новые тесты с параметризацией (требование лабораторной работы)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1.5, 0.5, 3.0),        # дробные числа
        (-9.0, 3.0, -3.0),      # отрицательное делимое
        (7.5, -2.5, -3.0),      # отрицательный делитель
        (0.0, 5.0, 0.0),        # нулевое делимое (граничное значение)
        (1.0, 3.0, 1 / 3),      # периодическая дробь
        (1e12, 1e4, 1e8),       # очень большие числа
        (1e-6, 1e-3, 1e-3),     # очень маленькие числа
    ],
)
def test_divide_parametrized(calc: Calculator, a: float, b: float, expected: float) -> None:
    """Параметризованная проверка деления (в т.ч. дробных чисел)."""
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("method", "a", "b", "expected"),
    [
        ("add", 0.1, 0.2, 0.3),        # классическая проблема float
        ("add", -5.0, -7.0, -12.0),
        ("subtract", 0.0, 0.0, 0.0),
        ("subtract", -3.0, -8.0, 5.0),
        ("multiply", 0.0, 123.456, 0.0),
        ("multiply", -1.5, -2.0, 3.0),
    ],
)
def test_basic_operations_parametrized(
    calc: Calculator, method: str, a: float, b: float, expected: float
) -> None:
    """Параметризованная проверка add/subtract/multiply, включая границы."""
    operation = getattr(calc, method)
    assert operation(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("b", [0, 0.0, -0.0])
def test_divide_by_zero_parametrized(calc: Calculator, b: float) -> None:
    """Любая форма нуля как делитель должна приводить к ValueError."""
    with pytest.raises(ValueError, match="Деление на ноль"):
        calc.divide(1.0, b)
