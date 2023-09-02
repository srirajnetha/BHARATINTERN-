import os

# Define the directory to store content
content_directory = "content/"

# Ensure the content directory exists
if not os.path.exists(content_directory):
    os.makedirs(content_directory)

def add_content(title, text):
    """Add new content to the tool."""
    filename = os.path.join(content_directory, title + ".txt")
    with open(filename, "w") as file:
        file.write(text)
    print(f"Content '{title}' added.")

def list_content():
    """List all available content."""
    content_files = os.listdir(content_directory)
    if content_files:
        print("Available content:")
        for filename in content_files:
            print(os.path.splitext(filename)[0])
    else:
        print("No content available.")

def delete_content(title):
    """Delete content by title."""
    filename = os.path.join(content_directory, title + ".txt")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Content '{title}' deleted.")
    else:
        print(f"Content '{title}' not found.")

# Main loop
while True:
    print("\nContent Management Tool")
    print("1. Add Content")
⬤
