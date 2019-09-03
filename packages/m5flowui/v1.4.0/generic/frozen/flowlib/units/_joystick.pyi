# make_stub_files: Tue 03 Sep 2019 at 17:05:43

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Joystick:
    def __init__(self, port: Any) -> None: ...
    def _available(self) -> None: ...
    def X(self) -> Any: ...
        #   0: return self.value[0]
        # ? 0: return self.value[number]
    def Y(self) -> Any: ...
        #   0: return self.value[1]
        # ? 0: return self.value[number]
    def InvertX(self) -> Any: ...
        #   0: return 255-self.X
        # ? 0: return number-self.X
    def InvertY(self) -> Any: ...
        #   0: return 255-self.Y
        # ? 0: return number-self.Y
    def Press(self) -> Union[Any, number]: ...
    def _update(self) -> None: ...
    def deinit(self) -> None: ...
