# make_stub_files: Tue 03 Sep 2019 at 17:05:43

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Encode:
    def __init__(self, addr: Any=94) -> None: ...
    def _available(self) -> None: ...
    def _update(self) -> None: ...
    def deinit(self) -> None: ...
    def setLed(self, pos: Any, color: Any) -> None: ...
    def clearValue(self) -> None: ...
    def getValue(self) -> Any: ...
        #   0: return self.encode_value
        # ? 0: return self.encode_value
    def getDir(self) -> Any: ...
        #   0: return self.dir
        # ? 0: return self.dir
    def getPress(self) -> Any: ...
        #   0: return self.press
        # ? 0: return self.press
