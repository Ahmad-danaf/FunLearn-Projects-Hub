# Day 04 – Input/Output in Bash

## Key Concepts

### Input
```bash
read variable
read -p "Prompt: " variable
```

### Output
```bash
echo "Some text"
```

### Redirect output
```bash
echo "hello" > file.txt   # overwrite
echo "hello" >> file.txt  # append
```

### Redirect input
```bash
cat < file.txt
```

### Pipe
```bash
command1 | command2
```
The output of the first command is sent as input to the second.

### tr (translate)
```bash
echo "ABC" | tr 'A-Z' 'a-z'  # convert to lowercase
```

## String transformations

### Capitalize first letter
```bash
name="${name^}"
```

### Lowercase a string
```bash
command=$(echo "$command" | tr 'A-Z' 'a-z')
```

## Practice Summary

- Ask user: name, age, favorite command
- Capitalize name
- Lowercase command
- Save to `user_profiles.txt` in this format:
  ```
  [YYYY-MM-DD HH:MM] Name: Ahmad, Age: 21, Favorite Command: ls
  ```

## Pro Tip
Ensure folders exist before writing:
```bash
mkdir -p output
```
