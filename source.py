
print("|-----------------------------------------------------|")
print("  |Press ctrl+c to exit out or just close the window|")
print("|-----------------------------------------------------| \n \n")

def main():
    print("What is your DPI")
    DPI = int(input())

    print("What is your sensitivity")
    sens = float(input())
        
    eDPI = DPI * sens

    print("\n","Your DPI is", eDPI, "\n")
    main()

main()

        
