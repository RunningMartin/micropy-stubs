
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def set_debug(val: Any) -> None: ...
class PollEventLoop(EventLoop):
    def __init__(self, runq_len: smallint=16, waitq_len: smallint=16) -> None: ...
    def add_reader(self, sock: Any, cb: Any, *args) -> None: ...
    def remove_reader(self, sock: Any) -> None: ...
    def add_writer(self, sock: Any, cb: Any, *args) -> None: ...
    def remove_writer(self, sock: Any) -> None: ...
    def cancel_io(self, sock: Any) -> None: ...
    def wait(self, delay: Any) -> None: ...
class StreamReader:
    def __init__(self, polls: Any, ios: Any=None) -> None: ...
    def read(self, n: int=-1) -> Any: ...
        #   0: return res
        # ? 0: return res
    def readexactly(self, n: int) -> Any: ...
        #   0: return buf
        # ? 0: return buf
    def readline(self) -> Any: ...
        #   0: return buf
        # ? 0: return buf
    def aclose(self) -> None: ...
    def __repr__(self) -> str: ...
class StreamWriter:
    def __init__(self, polls: Any, ios: Any=None, extra: Any=None) -> None: ...
    def awrite(self, buf: Any, off: Any=0, sz: Any=-1) -> None: ...
    def awritestr(self, s: str) -> None: ...
    def awriteiter(self, iterable: Any) -> None: ...
    def aclose(self) -> None: ...
    def get_extra_info(self, name: str, default: Any=None) -> Any: ...
        #   0: return self.extra.get(name,default)
        # ? 0: return self.extra.get(str, default)
    def __repr__(self) -> str: ...
def open_connection(host: Any, port: Any, ssl: Any=bool) -> Tuple[Any, Any, Any, Any]: ...
def start_server(client_coro: Any, host: Any, port: Any, backlog: Any=10, ssl: Any=None) -> None: ...
