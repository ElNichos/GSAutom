from abc import ABC


class CompositeEntity(ABC):
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception(f"Cannot compare {type(self)} instance with {type(other)}")
        for key in self.__dict__:
            if key not in other.__dict__:
                return False
            else:
                if self.__dict__[key] != other.__dict__[key]:
                    return False
        return True


class NetEntity(CompositeEntity, ABC):
    _commissioning_date = None
    _evaluation_data = None
    _info_data = None

    def __str__(self):
        return (f"ComDate: {self.commissioning_date}\n "
                f"EvaluatorData:\n{self.evaluation_data}\n"
                f"InfoData:\n{self.info_data}")
