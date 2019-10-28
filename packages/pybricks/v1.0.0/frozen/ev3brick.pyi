
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class sound:
    def beep(cls: Any, frequency: int=500, duration: int=100, volume: int=30) -> None: ...
    def beeps(cls: Any, number: int) -> None: ...
    def file(cls: Any, file_name: str, volume: int=100) -> None: ...
class display:
    def clear(cls: Any) -> None: ...
    def image(cls: Any, file_name: str, alignment: Align=Align.CENTER, coordinate: Tuple[(int, int)]=None, clear: bool=bool) -> None: ...
    def text(cls: Any, text: str, coordinate: Tuple[(int, int)]=None) -> None: ...
class battery:
    def current(cls: Any) -> None: ...
    def voltage(cls: Any) -> None: ...
def buttons() -> None: ...
def light(color: Color) -> None: ...
