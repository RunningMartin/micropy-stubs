
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def height() -> number: ...
def max_width() -> number: ...
def hmap() -> bool: ...
def reverse() -> bool: ...
def monospaced() -> bool: ...
def min_ch() -> number: ...
def max_ch() -> number: ...
def _chr_addr(ordch: Any) -> Any: ...
    #   0: return int.from_bytes(_index[offset:offset+2],'little')
    # ? 0: return int.from_bytes(_index[offset:offset+number], str)
def get_ch(ch: Any) -> Tuple[Any, number, Any]: ...
