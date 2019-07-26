# make_stub_files: Fri 26 Jul 2019 at 02:36:14

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class bootrom(object):
    def __init__(self) -> None: ...
    def open(self, filename: str='', mode: Any='r') -> None: ...
    def close(self) -> None: ...
    def tell(self) -> Any: ...
        #   0: return self.__fpointer
        # ? 0: return self.__fpointer
    def seek(self, offset: Any, start: Any=0) -> Any: ...
        #   0: return self.__fpointer
        # ? 0: return self.__fpointer
    def get_size(self) -> Any: ...
        #   0: return self.__size
        # ? 0: return self.__size
    def read(self, size: Any=0) -> Union[Any, bytes]: ...
        #   0: return b''
        #   0: return bytes
        #   1: return self.BOOTROM[fpointer:self.__size]
        # ? 1: return self.BOOTROM[fpointer:self.__size]
        #   2: return self.BOOTROM[fpointer:self.__fpointer]
        # ? 2: return self.BOOTROM[fpointer:self.__fpointer]
