# make_stub_files: Wed 19 Jun 2019 at 15:01:14

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def set_debug(val: Any) -> None: ...
def socket(af: Any=usocket.AF_INET) -> str: ...
def recv(s: str, n: int) -> Any: ...
    #   0: return s.recv(n)
    # ? 0: return str.recv(int)
def recvfrom(s: str, n: int) -> Any: ...
    #   0: return s.recvfrom(n)
    # ? 0: return str.recvfrom(int)
def sendto(s: str, buf: Any, addr: Any=None) -> None: ...
def close(s: str) -> None: ...
