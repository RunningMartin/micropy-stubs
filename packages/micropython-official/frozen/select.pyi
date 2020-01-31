
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Epoll:
    def __init__(self, epfd: Any) -> None: ...
    def register(self, fd: Any, eventmask: Any=EPOLLIN|EPOLLPRI|EPOLLOUT, retval: Any=) -> None: ...
    def unregister(self, fd: Any) -> None: ...
    def poll_ms(self, timeout: Any=-) -> Any: ...
        #   0: return res
        # ? 0: return res
    def poll(self, timeout: Any=-) -> Any: ...
        #   0: return self.poll_ms(- if timeout==- else timeout* )
        # ? 0: return self.poll_ms(Optional[Any])
    def close(self) -> None: ...
def epoll(sizehint: Any=) -> Any: ...
    #   0: return Epoll(fd)
    # ? 0: return Epoll(fd)
