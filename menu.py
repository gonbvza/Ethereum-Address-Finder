from find_combinator import find_combinator
from compareToAddress import compareToAddress

def main():
    print("Welcome to the address finder")
    print("Choose an option")
    print("1. Find the combination without the address")
    print("2. Find the combination with the address")

    option = input("Enter the option: ")

    if option == "1":
        find_combinator()
    elif option == "2":
        target = input("Enter the target address: ")
        compareToAddress(target)

if __name__ == "__main__":
    main()
