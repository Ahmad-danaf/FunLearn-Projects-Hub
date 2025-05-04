### Day 3: Your First Bash Script

---

#### Script Structure
```bash
#!/bin/bash   # Always start scripts with this line
```

---

#### Print to Terminal
```bash
echo "Your message here"
```

---

#### Variables
```bash
name="Ahmad"          # No spaces around '='
echo $name            # Access value
echo "Hi, $name!"     # Can be used inside double quotes
```

- Use `"$var"` when the value may contain spaces
- You can overwrite a variable by reassigning it

---

####  `read` Command (User Input)
```bash
read username         # Waits for user to input something
echo "Hello, $username"
```

With a prompt on the same line:
```bash
read -p "Enter name: " name
```

Silent input (e.g. password):
```bash
read -s password
```

---

####  Date Command (store current date)
```bash
today=$(date +%Y-%m-%d)
echo "Today's date is: $today"
```