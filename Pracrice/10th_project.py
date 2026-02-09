# Perfect! 🎉 You’ve now reached Hour 12: Final Project + Review — this is where everything you’ve learned comes together in a real-world Python project.

# ✅ Hour 12: Final Project + Python Review

# 🔷 What You've Learned So Far:
# | Topic                  | Skills Mastered                    |
# | ---------------------- | ---------------------------------- |
# | Variables + Data Types | Numbers, strings, lists, etc.      |
# | Operators              | Arithmetic, comparison, logical    |
# | Functions              | `def`, parameters, return          |
# | Strings & Lists        | Indexing, slicing, methods         |
# | File Handling          | `read`, `write`, `with`, `open()`  |
# | Error Handling         | `try`, `except`, `finally`         |
# | Modules & Libraries    | Built-in and external module usage |


# 🧩 Final Project: Personal Notes Manager (File-based App)

# 🧠 Objective:
# A command-line tool where you can:
# ✍️ Add new notes
# 📄 View existing notes
# ❌ Delete all notes
# ✅ Each note saved in a .txt file
# 📅 Timestamp each note

# 🔧 Tools Used:
# functions (to organize logic)
# file handling (open, read, write)
# datetime module (for timestamps)
# loop & condition to create menu


from datetime import datetime

FILENAME = "mynotes.txt"

def add_note():
    note = input("Write your note: ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, "a") as file:
        file.write(f"[{time}] {note}\n")
    print("✅ Note saved!")

def view_notes():
    try:
        with open(FILENAME, "r") as file:
            content = file.read()
            if content:
                print("\n📝 Your Notes:\n" + content)
            else:
                print("📂 No notes yet.")
    except FileNotFoundError:
        print("📂 No notes file found yet.")

def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").lower()
    if confirm == "yes":
        open(FILENAME, "w").close()
        print("🗑️ All notes deleted.")
    else:
        print("❌ Deletion cancelled.")

# Main Menu
while True:
    print("\n--- Notes Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("👋 Exiting... Bye!")
        break
    else:
        print("❗Invalid choice. Try again.")
