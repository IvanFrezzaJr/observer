from interface import Observer, Observable
from observable import InputObservable
from command import Main


class EntryObserver(Observer):
    def __init__(self, element):
        self.element = element

    def update(self, observable: Observable) -> None:
        if isinstance(observable, InputObservable):
            self.element.delete(0, "end")
            self.element.insert(0, observable.uiobject.get())


class TextBoxObserver(Observer):
    def __init__(self, element):
        """element is the UI part. you can use things like textBox, label ..."""
        self.element = element

    def update(self, observable: Observable) -> None:
        """receive object that have been observed. In thats case will be Main

        It can be just a value and in the command.py file you can replace:
        def notify(self) -> None:
            for observer in self.__observers:
                observer.update(self)

        by

        def notify(self, <some_value>) -> None:
        for observer in self.__observers:
            observer.update(<some_value>)

        """
        if isinstance(observable, Main):
            # apply specific rules from the observed object.

            self.element.insert("end", f"processing ... {str(observable.step)} \n")
            self.element.update_idletasks()
