import os
from typing import List

class WAL:
    def __init__(self, file_path: str = "wal.log"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()

    def log(self, entry: str) -> None:
        with open(self.file_path, 'a') as f:
            f.write(entry + "\n")

    def read(self) -> List[str]:
        with open(self.file_path, 'r') as f:
            return f.readlines()

    def clear(self) -> None:
        open(self.file_path, 'w').close()

