"""CLI tool for successive approximation"""


class Bisect():
    """
    Tool to bisect problems
    Give only [lower, upper] to start bisecting in a range
    Give only current to start with finding a range, then bisect
    Everything else raises a ValueError
    """
    def __init__(self,
                 lower: float = None,
                 upper: float = None,
                 current: float = None) -> None:
        """
        Initialises the bisection
        """
        if current is None:
            if lower is None or upper is None:
                raise ValueError
        else:
            if lower is not None or upper is not None:
                raise ValueError

        if lower == upper and lower is not None:
            raise ValueError

        self._lower = lower
        self._upper = upper

        if current is None:
            self._bisect()
        else:
            self._current = current

    def Suggestion(self) -> float:
        return self._current

    def TooBig(self) -> None:
        if (self._lower, self._upper) != (None, None):
            self._upper = self._current
            self._bisect()
        elif self._current is not None:
            self._lower = 0
            self._upper = 2
            self._bisect()

    def TooSmall(self) -> None:
        if self._lower is not None and self._upper is not None:
            self._lower = self._current
            self._bisect()
        elif self._upper is None and self._current is not None:
            self._lower = self._current
            self._current *= 2
        # else: prevented by checks in the constructor.

    def _bisect(self) -> None:
        self._current = self._lower + (self._upper - self._lower) / 2
