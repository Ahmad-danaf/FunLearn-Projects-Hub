# Day 02 – Permissions & Ownership

## Commands Reviewed

- `chmod` – change file permissions
- `chown` – change file owner
- `chgrp` – change file group

---

## Understanding `ls -l` Output

Example:
```
-rw-r--r-- 1 ahmad ahmad 123 May 3 04:00 file.txt
```

Breakdown:
- `-rw-r--r--` → permissions:
  - `-` = file (or `d` for directory)
  - `rw-` = user permissions (read/write)
  - `r--` = group permissions (read-only)
  - `r--` = others permissions (read-only)
- `1` → number of hard links
- `ahmad` → owner (user)
- `ahmad` → group
- `123` → file size in bytes
- `May 3 04:00` → last modified time
- `file.txt` → filename

---

### chmod Number Mapping

- `r` (read)  = 4
- `w` (write) = 2
- `x` (execute) = 1

Each digit in `chmod` is the sum of these values.

For example:
- `7` = 4 + 2 + 1 = `rwx`
- `5` = 4 + 0 + 1 = `r-x`

### Symbolic vs Shorthand

- `chmod u+x script.sh` → adds execute permission **only to the file owner**
- `chmod +x script.sh` → adds execute permission **to everyone** (same as `a+x`)

## chmod Quick Sheet (Octal Mode)

| Digit | Binary | Permissions | Symbolic |
|-------|--------|-------------|----------|
| 7     | 111    | rwx         | read, write, execute |
| 6     | 110    | rw-         | read, write          |
| 5     | 101    | r-x         | read, execute        |
| 4     | 100    | r--         | read only            |
| 0     | 000    | ---         | no permissions       |

**Examples:**
- `chmod 755 script.sh` → user: rwx, group: r-x, others: r-x
- `chmod 600 notes.txt` → user: rw-, group/others: ---
- `chmod 444 public.log` → all: read-only

---

## Ownership with `chown` and `chgrp`

Change file owner:
```bash
sudo chown username file.txt
```

Change owner and group:
```bash
sudo chown username:groupname file.txt
```

Change only group:
```bash
sudo chgrp groupname file.txt
```

> Note: `sudo` is required unless you're the file's owner and not changing ownership to another user.
