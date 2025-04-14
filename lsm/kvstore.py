from lsm.memtable import MemTable
from lsm.sstable import SSTable
from lsm.wal import WAL
from typing import Optional

class KVStore:
    def __init__(self):
        self.memtable = MemTable()
        self.sstable = SSTable()
        self.wal = WAL()
        self._load_from_wal()

    def _load_from_wal(self) -> None:
        entries = self.wal.read()
        for entry in entries:
            parts = entry.strip().split()
            if len(parts) >= 3 and parts[0] == "SET":
                key, value = parts[1], ' '.join(parts[2:])
                self.memtable.set(key, value)

    def set(self, key: str, value: str) -> None:
        self.wal.log(f"SET {key} {value}")
        self.memtable.set(key, value)

    def get(self, key: str) -> Optional[str]:
        value = self.memtable.get(key)
        if value is not None:
            return value
        return self.sstable.read(key)

    def flush(self) -> None:
        data = self.memtable.flush()
        self.sstable.write(data)
        # Clear WAL after flushing
        self.wal.clear()
