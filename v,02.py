import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear()
    print("""
███████╗███╗   ███╗ ██████╗ ██████╗  █████╗ ███╗   ██╗███████╗
██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║██╔════╝
███████╗██╔████╔██║██║   ██║██████╔╝███████║██╔██╗ ██║███████╗
╚════██║██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║╚════██║
███████║██║ ╚═╝ ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║███████║
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
By TADASH10

[1] Encrypt API requests
[2] Decrypt API responses
[3] Generate encryption keys
[4] Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Implement code to encrypt API requests
        print("Encrypting API requests...")
        input("Press Enter to continue...")
        main_menu()

    elif choice == "2":
        # Implement code to decrypt API responses
        print("Decrypting API responses...")
        input("Press Enter to continue...")
        main_menu()

    elif choice == "3":
        # Implement code to generate encryption keys
        print("Generating encryption keys...")
        input("Press Enter to continue...")
        main_menu()

    elif choice == "4":
        # Exit the menu
        clear()
        print("Goodbye!")

    else:
        # Invalid input
        input("Invalid choice. Press Enter to try again...")
        main_menu()

if __name__ == "__main__":
    main_menu()
