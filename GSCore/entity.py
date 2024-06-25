from abc import ABC
from datetime import datetime


class CompositeEntity(ABC):
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception(f"Cannot compare {type(self)} instance with {type(other)}")
        for key, value in self.__dict__.items():
            if key not in other.__dict__.keys():
                return False
            else:
                other_value = other.__dict__[key]
                if value != other_value:
                    return False
        return True


class NetEntity(CompositeEntity, ABC):
    _commissioning_date = None
    _evaluation_data = None
    _info_data = None

    @property
    def comissioning_date(self):
        return self._commissioning_date

    @comissioning_date.setter
    def comissioning_date(self, value):
        if value is None:
            self._commissioning_date = None
        else:
            if not isinstance(value, datetime):
                raise ValueError(f"{value} is not an instance of datetime")
            self._commissioning_date = value

    def __str__(self):
        return (f"ComDate: {self.commissioning_date}\n "
                f"EvaluatorData:\n{self.evaluation_data}\n"
                f"InfoData:\n{self.info_data}")
