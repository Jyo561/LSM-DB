import cmd
from lsm.kvstore import KVStore

class LSMKVShell(cmd.Cmd):
    intro = "🗃️  Welcome to the LSM KVStore shell. Type help or ? to list commands.\n"
    prompt = "kvstore> "

    def __init__(self):
        super().__init__()
        self.store = KVStore()

    def do_set(self, arg: str) -> None:
        "Set a key-value pair: set <key> <value>"
        parts = arg.strip().split()
        if len(parts) != 2:
            print("❌ Usage: set <key> <value>")
            return
        key, value = parts
        self.store.set(key, value)
        print(f"✅ Set key: {key}")

    def do_get(self, arg: str) -> None:
        "Get a value by key: get <key>"
        key = arg.strip()
        if not key:
            print("❌ Usage: get <key>")
            return
        value = self.store.get(key)
        if value is not None:
            print(f"🔍 {key} = {value}")
        else:
            print("❌ Key not found.")

    def do_flush(self, arg: str) -> None:
        "Flush MemTable to SSTable"
        self.store.flush()
        print("💾 Flushed MemTable to SSTable.")

    def do_exit(self, arg: str) -> bool:
        "Exit the shell"
        print("👋 Exiting KVStore.")
        return True

    def do_EOF(self, arg: str) -> bool:
        return self.do_exit(arg)

if __name__ == "__main__":
    LSMKVShell().cmdloop()

