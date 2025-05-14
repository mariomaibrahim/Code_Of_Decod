# Morse Code Converter

A simple Python script to **encrypt** plain text into Morse code and **decrypt** Morse code back into readable text.  
This tool supports:
- English letters (A-Z, case-insensitive)
- Numbers (0-9)
- Spaces between words
- Basic error handling for unsupported characters

## Features

- **Encryption**: Converts normal text into Morse code.
- **Decryption**: Converts Morse code (using `*` and `-` symbols) back into readable text.
- **Word Separation**: Uses `|` to separate words when encrypting or decrypting.
- **Input Validation**: Warns the user if unsupported characters or Morse codes are used.

## Morse Code Reference

Example encodings used in this script:

| Character | Morse Code |
|-----------|------------|
| A         | *-         |
| B         | -***       |
| C         | -*-*       |
| ...       | ...        |
| 0         | -----      |
| 1         | *----      |
| ...       | ...        |
| 9         | ----*      |
| Space     | \|         |

> Note: The script uses `*` instead of the traditional `.` to make it more readable in console output.

## How to Use

1. **Run the script**.
2. Choose either `encrypt` or `decrypt` when prompted.
3. Enter the desired input.

### Example 1 - Encryption

```bash
Enter <encrypt> or <decrypt>: encrypt
Enter your text: hello 123
Morse Code:
**** * *-** *-** --- | *---- **--- ***--
