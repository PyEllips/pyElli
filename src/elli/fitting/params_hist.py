"""ParmsHist provides a wrapper around lmfit.Parameters
to keep track of the changes made to the parameters."""
# Encoding: utf-8
import copy
from lmfit import Parameters

class ParamsHist(Parameters):
    """A wrapper around lmfit.Parameters to keep track of the changes made to the parameters."""
    _history = []
    _max_length = 50

    def _clone_and_append(self):
        if len(self._history) >= self._max_length:
            self._history = self._history[1:]
        clone = copy.deepcopy(self)
        self.history.append(clone)

    @property
    def history(self) -> list:
        """Gets the entire history

        Returns:
            list[Parameters]: The history
        """
        return self._history

    def clear_history(self):
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
    def max_history_len(self, history_len:int):
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

    def revert(self, hist_pos:int):
        """Reverts to an older history version

        Args:
            hist_pos (int): The history position to revert to.
        """
        self.update(self._history[hist_pos])

    def update_value(self, key:str, value:float):
        """Updates a parameter and keeps track of the change in history

        Args:
            key (str): The key to be updated
            value (float): The value the key should be updated to
        """
        self._clone_and_append()
        super(ParamsHist, self).__getitem__(key).value = value

    def tracked_add(self, *args, **kwargs):
        """Adds a parameter and keeps track of the change in history"""
        self._clone_and_append()
        super(ParamsHist, self).add(*args, **kwargs)

    def commit(self):
        """Saves the current parameter set to history."""        
        self._clone_and_append()
