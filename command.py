from interface import Observer
from typing import List
import time


class Main:
    step = 0
    __observers = []

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

    def run(self):
        for i in range(0, 10):
            time.sleep(0.1)

            self.step = i

            self.notify()

            print("processing ... ", self.step)
