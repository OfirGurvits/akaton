from abc import ABC, abstractmethod


class MouseInfo(ABC):
    def __init__(self, observing):
        self.observing = observing

    def notify_click(self):
        for observer in self.observing:
            observer.click()
