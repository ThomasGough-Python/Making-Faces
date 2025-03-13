# Replace Faces - Emoji Converter

## Description
This Python script replaces basic text-based emoticons with their corresponding emoji equivalents. It scans the input text for predefined emoticons and replaces them accordingly.

## Features
- Converts `:)` to 🙂
- Converts `:(` to 🙁

## How It Works
1. The script defines a dictionary of emoticons and their corresponding emoji.
2. It loops through the dictionary and replaces occurrences of the emoticons in the given text.
3. The script prompts the user to input text.
4. The processed text with emoji replacements is displayed as output.

## Usage
### Running the Script
1. Ensure you have Python installed (Python 3.x recommended).
2. Save the script as `replace_faces.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `replace_faces.py`.
5. Run the script using:
   ```sh
   python replace_faces.py
   ```
6. Enter text containing `:)` or `:(` and see them replaced with their emoji counterparts.

## Example
**Input:**
```
Hello there! :)
```
**Output:**
```
Hello there! 🙂
```

## Customization
You can add more emoticons to the `faces` dictionary to extend functionality. For example:
```python
faces = {
    ":)": "🙂",
    ":(": "🙁",
    ":D": "😀",
    ";)": "😉"
}
```

## License
This script is open-source and can be modified and distributed freely.
