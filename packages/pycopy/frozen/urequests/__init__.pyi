# make_stub_files: Mon 02 Sep 2019 at 04:16:29

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Response:
    def __init__(self, f: Any) -> None: ...
    def close(self) -> None: ...
    def content(self) -> Any: ...
        #   0: return self._cached
        # ? 0: return self._cached
    def text(self) -> str(self.content, self.encoding): ...
    def json(self) -> Any: ...
        #   0: return ujson.loads(self.content)
        # ? 0: return ujson.loads(self.content)
def request(method: Any, url: Any, data: Any=None, json: Any=None, headers: Any={}, stream: Any=None, parse_headers: Any=bool) -> Any: ...
    #   0: return resp
    # ? 0: return resp
def head(url: Any, **kw) -> Any: ...
    #   0: return request('HEAD',url,None=kw)
    # ? 0: return request(str, url, None=kw)
def get(url: Any, **kw) -> Any: ...
    #   0: return request('GET',url,None=kw)
    # ? 0: return request(str, url, None=kw)
def post(url: Any, **kw) -> Any: ...
    #   0: return request('POST',url,None=kw)
    # ? 0: return request(str, url, None=kw)
def put(url: Any, **kw) -> Any: ...
    #   0: return request('PUT',url,None=kw)
    # ? 0: return request(str, url, None=kw)
def patch(url: Any, **kw) -> Any: ...
    #   0: return request('PATCH',url,None=kw)
    # ? 0: return request(str, url, None=kw)
def delete(url: Any, **kw) -> Any: ...
    #   0: return request('DELETE',url,None=kw)
    # ? 0: return request(str, url, None=kw)
