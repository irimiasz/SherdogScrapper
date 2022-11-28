from abc import ABC, abstractmethod


class AbstractAdapter(ABC):
    scrapper_class = None
    model_class = None

    def __init__(self, **kwargs):
        if self.scrapper_class:
            self.data = self.scrapper_class(**kwargs).data
        else:
            self.data = kwargs.get('data')

    @abstractmethod
    def to_dict(self) -> {}:
        raise NotImplementedError()

    def to_model(self):
        return self.model_class(self.to_dict())
