import collections
import os
import pathlib

def get_file_content(fname: str, line_mode=True) -> str:
   data_path = pathlib.Path(os.path.dirname(__file__)) / "resources"
   with open(data_path / fname, "r") as f:
       return f.readlines() if line_mode else f.read()

class _LazyDict(collections.defaultdict):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def __missing__(self, key):
        val = self.fn(key)
        self[key] = val
        return val

def make_lazy_dict(fn):
    return _LazyDict(fn)

def make_graph(neighbor_fn):
    def fn(key):
        return list(neighbor_fn(key))
    return make_lazy_dict(fn)