def replace_faces(text):
    # Emoji Dictionary
    faces = {
        ":)": "🙂",
        ":(": "🙁"
    }
    
    for face, emoji in faces.items():
        text = text.replace(face, emoji)
    
    return text

# Main program
if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Please enter text: ")
    
    # Result
    result = replace_faces(user_input)
    print(result)
