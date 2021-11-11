# Encoding: utf-8
import copy
from lmfit import Parameters

class ParamsHist(Parameters):
    _history = []
    _max_length = 50

    def _clone_and_append(self):
        if len(self._history) >= self._max_length:
            self._history = self._history[1:]
        clone = copy.deepcopy(self)
        self.history.append(clone)

    @property
    def history(self):
        return self._history

    def clear_history(self):
        self._history = []

    @property
    def history_len(self):
        return len(self._history)

    @property
    def max_history_len(self):
        return self._max_length

    @max_history_len.setter
    def max_history_len(self, val):
        if not isinstance(val, int):
            raise Exception('History length has to be an integer')

        if val < 1:
            raise Exception('History length must be greater than 0')

        self._history = self._history[-val:]
        self._max_length = val

    def revert(self, hist_pos):
        self.update(self._history[hist_pos])

    def update_value(self, key, value):
        self._clone_and_append()
        super(ParamsHist, self).__getitem__(key).value = value

    def tracked_add(self, *args, **kwargs):
        self._clone_and_append()
        super(ParamsHist, self).add(*args, **kwargs)

    def commit(self):
        self._clone_and_append()
