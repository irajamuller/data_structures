from abc import ABC, abstractmethod

class ADTQueue(ABC):
    DEFAULT_SIZE: int = 10
    
    @abstractmethod 
    def is_empty(self) -> bool: ...
    @abstractmethod 
    def is_full(self) -> bool: ...
    @abstractmethod 
    def enqueue(self, element: object) -> None: ...
    @abstractmethod 
    def dequeue(self) -> object: ...
    @abstractmethod 
    def peek(self) -> object: ...
    @abstractmethod 
    def size(self) -> int: ...    
