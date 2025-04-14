from typing import Dict, Optional

class MemTable:
    def __init__(self):
        self.table: Dict[str, str] = {}

    def set(self, key: str, value: str) -> None:
        self.table[key] = value

    def get(self, key: str) -> Optional[str]:
        return self.table.get(key)

    def flush(self) -> Dict[str, str]:
        flushed = self.table.copy()
        self.table.clear()
        return flushed

