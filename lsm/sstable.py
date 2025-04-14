import os
import json
from typing import Optional

class SSTable:
    def __init__(self, directory: str = "data"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)
        self.counter = len(os.listdir(self.directory))

    def write(self, data: dict) -> None:
        path = os.path.join(self.directory, f"sstable_{self.counter}.json")
        with open(path, 'w') as f:
            json.dump(data, f)
        self.counter += 1

    def read(self, key: str) -> Optional[str]:
        files = sorted(os.listdir(self.directory), reverse=True)
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(self.directory, file), 'r') as f:
                    data = json.load(f)
                    if key in data:
                        return data[key]
        return None

