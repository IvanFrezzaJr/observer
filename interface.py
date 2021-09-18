from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(args: List[any]):
        ...


class Observable(ABC):
    @abstractmethod
    def subscribe(observers: List[Observer]) -> None:
        ...

    def unsubscribe(observer: Observer) -> None:
        ...

    def notify() -> None:
        ...
