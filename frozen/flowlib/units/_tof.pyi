
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Tof:
    def __init__(self, port: Any) -> None: ...
    def _register_char(self, register: Any, value: Any=None, buf: Any=bytearray(1)) -> Any: ...
        #   0: return buf[0]
        # ? 0: return buf[number]
        #   1: return self.i2c.writeto_mem(_ADDR,register,buf)
        # ? 1: return self.i2c.writeto_mem(_ADDR, register, buf)
    def _register_short(self, register: Any, value: Any=None, buf: Any=bytearray(2)) -> Any: ...
        #   0: return ustruct.unpack('>h',buf)[0]
        # ? 0: return ustruct.unpack(str, buf)[number]
        #   1: return self.i2c.writeto_mem(_ADDR,register,buf)
        # ? 1: return self.i2c.writeto_mem(_ADDR, register, buf)
    def _available(self) -> None: ...
    def _update(self) -> None: ...
    def deinit(self) -> None: ...
