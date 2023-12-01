import os
import pathlib

def get_file_content(fname: str, line_mode=True) -> str:
   data_path = pathlib.Path(os.path.dirname(__file__)) / "resources"
   with open(data_path / fname, "r") as f:
       return f.readlines() if line_mode else f.read()