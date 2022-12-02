from abc import ABC, abstractmethod


class DataSetupMixin(ABC):
    @abstractmethod
    def set_up_data(self, **kwargs):
        raise NotImplementedError


class ScrapperDataSetupMixin(DataSetupMixin):
    scrapper_class = None

    def set_up_data(self, **kwargs):
        return self.scrapper_class(**kwargs).data


class SubAdapterDataSetupMixin(DataSetupMixin):
    def set_up_data(self, **kwargs):
        return kwargs.get("data")


class AbstractAdapter(DataSetupMixin, ABC):
    model_class = None

    def __init__(self, **kwargs):
        self.data = self.set_up_data(**kwargs)

    @abstractmethod
    def to_dict(self) -> {}:
        raise NotImplementedError()

    def to_model(self):
        return self.model_class(self.to_dict())
