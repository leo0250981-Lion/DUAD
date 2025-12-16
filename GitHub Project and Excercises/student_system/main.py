from menu import show_menu

def main():
    while True:
        option = show_menu()

        if option == "1":
            print("Add a student")
        elif option == "2":
            print("Show Enlisted Students")
        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()