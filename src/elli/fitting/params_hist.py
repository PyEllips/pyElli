"""ParmsHist provides a wrapper around lmfit.Parameters
to keep track of the changes made to the parameters."""
# Encoding: utf-8
import copy
from typing import List
from lmfit import Parameters


class ParamsHist(Parameters):
    """A wrapper around lmfit.Parameters to keep track of the changes made to the parameters."""

    def __init__(self) -> None:
        super().__init__()
        self._history = []
        self._max_length = 50

    @property
    def history(self) -> List[Parameters]:
        """Gets the entire history

        Returns:
            List[Parameters]: The history
        """
        return self._history

    def clear_history(self) -> None:
        """Clears the parameters history"""
        self._history = []

    @property
    def history_len(self) -> int:
        """The current length of the history

        Returns:
            int: The length of the history
        """
        return len(self._history)

    @property
    def max_history_len(self) -> int:
        """The maximum length of the history

        Returns:
            int: The maximum length of the history
        """
        return self._max_length

    @max_history_len.setter
    def max_history_len(self, history_len: int) -> None:
        """Sets the maximum history length. If the current
        history length is greater than the new history length the history
        gets truncated.

        Args:
            history_len (int): The new history length

        Raises:
            ValueError: If history_len is not an int or < 1.
        """
        if not isinstance(history_len, int):
            raise ValueError('History length has to be an integer')

        if history_len < 1:
            raise ValueError('History length must be greater than 0')

        self._history = self._history[-history_len:]
        self._max_length = history_len

    def revert(self, hist_pos: int) -> None:
        """Reverts to an older history version and keeps the entire history.

        Args:
            hist_pos (int): The history position to revert to.
        """
        if len(self._history) > (hist_pos % len(self._history)):
            self.update(self._history[hist_pos])

    def pop(self):
        """Gets to the previous history version and deletes the current element."""
        if len(self._history) > 0:
            curr_params = self.copy()
            self.update(self._history[-1])
            self._history = self._history[:-1]

            return curr_params
        return None

    def update_value(self, key: str, value: float) -> None:
        """Updates a parameter and keeps track of the change in history

        Args:
            key (str): The key to be updated
            value (float): The value the key should be updated to
        """
        self.commit()
        super().__getitem__(key).value = value

    def update_params(self, parameters) -> None:
        """Updates the current paramters from a lmfit parameters object.

        Args:
            parameters (lmfit.Parameters):
                The lmfit paramters object to update the values from.
        """
        self.commit()
        self.update(parameters)

    def tracked_add(self, *args, **kwargs) -> None:
        """Adds a parameter and keeps track of the change in history"""
        self.commit()
        super().add(*args, **kwargs)

    def commit(self) -> None:
        """Saves the current parameter set to history."""
        if len(self._history) >= self._max_length:
            self._history = self._history[1:]
        clone = copy.deepcopy(self)
        self.history.append(clone)
