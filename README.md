# LSM-PY-DB

A simple key-value database implementation using Log-Structured Merge (LSM) tree in Python.

## Features

- In-memory MemTable for fast writes
- Write-Ahead Log (WAL) for durability
- Sorted String Tables (SSTables) for persistent storage
- Basic compaction support
- Thread-safe operations

## Architecture

The database consists of several components:

1. **MemTable**: An in-memory table that stores recent writes
2. **WAL**: Write-Ahead Log for durability
3. **SSTable**: Sorted String Tables for persistent storage
4. **Compaction**: Merges SSTables to maintain performance

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jyo561/LSM-DB.git
   cd LSM-DB
   ```

2. Run the project:
   ```
   python3 main.py
   ```

### Basic Operations

The CLI supports the following commands:

- `put <key> <value>` - Store a key-value pair
- `get <key>` - Retrieve a value by key
- 
- `delete <key>` - Remove a key-value pair
- `exit` - Exit the CLI

## Implementation Details

### MemTable

- Uses a map for O(1) lookups
- Tracks size for flush triggers
- Thread-safe with mutex

### WAL

- Binary format with length-prefixed records
- Appends-only for durability
- Used for recovery

### SSTable

- Sorted key-value pairs
- Index for fast lookups
- Binary format with length-prefixed records


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


