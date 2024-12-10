def print_christmas_tree(levels):
    # Loop for the tree levels
    for i in range(levels):
        for j in range(levels - i - 1):
            print(" ", end="")  # Spaces for alignment
        for k in range(2 * i + 1):
            if k % 2 == 0:
                print("*", end="")  # Star ornaments
            else:
                print("o", end="")  # Ornaments
        print()  # Newline after each level

    # Tree trunk
    for i in range(2):
        for j in range(levels - 1):
            print(" ", end="")  # Spaces for alignment
        print("| |")  # Trunk

# Set the number of levels for the tree
levels = int(input("Enter the number of levels for the Christmas Tree: "))
print_christmas_tree(levels)
