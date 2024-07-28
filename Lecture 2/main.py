# main.py
import firelink

def print_menu():
    print("choose website")
    for idx, site in enumerate(firelink.favourite_sites):
        print(f"{idx + 1}. {site}")

def main():
    print_menu()
    try:
        choice = int(input("choose his number   "))
        if 1 <= choice <= len(firelink.favourite_sites):
            url = firelink.favourite_sites[choice - 1]
            firelink.browser(url)
        else:
            print("error number pls choose correct number")
    except ValueError:
        print("pls enter correct number")

if __name__ == "__main__":
    main()
