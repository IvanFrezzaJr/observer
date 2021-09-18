from interface import Observable, Observer
from typing import List
from command import Main

# ConcreteObservable
class InputObservable(Observable):
    __observers = []

    def __init__(self, uiobject):
        self.uiobject = uiobject

    def subscribe(self, observers: List[Observer]) -> None:
        for observer in observers:
            if observer in self.__observers:
                return
            self.__observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self.__observers:
            del self.__observers[observer]

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)
