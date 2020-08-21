from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def open(self, url):
        pass

    @abstractmethod
    def click(self, selector):
        pass

    @abstractmethod
    def type(self, selector, text):
        pass

    @abstractmethod
    def maximize_window(self):
        pass

    @abstractmethod
    def element_with_text(self, text):
        pass
