import sys
from typing import Union, TextIO, Protocol
import os

class Writeable(Protocol):
    def write(self, content: Union[str, bytes]) -> None:
        ...

def write(data: str, output: Writeable) -> None:

    if isinstance(output ,str):
        file_exists = os.path.exists(output)
        mode = 'a' if file_exists else 'w'
        with open(output, mode) as file:
            file.write(data + '\n')
    else:
        output.write(data)
