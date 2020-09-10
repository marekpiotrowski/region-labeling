from abc import ABC, abstractmethod


class MapNavigator(ABC):
    @abstractmethod
    def move_right_with_wrapping(self):
        pass

    @abstractmethod
    def get_neighborhood(self):
        pass

    @abstractmethod
    def update_current_element(self, val):
        pass

    @abstractmethod
    def reset(self):
        pass
