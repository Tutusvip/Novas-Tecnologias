def display_shapes():
    box = [
        "**********",
        "*        *",
        "*        *",
        "**********"
    ]

    oval = [
        "    ***    ",
        " *       * ",
        "*         *",
        " *       * ",
        "    ***    "
    ]

    arrow = [
        "    *",
        "   ***",
        "  *****",
        "*******",
        "  *****",
        "   ***",
        "    *"
    ]

    diamond = [
        "    *",
        "   ***",
        "  *****",
        " *******",
        "  *****",
        "   ***",
        "    *"
    ]

    print("Box:")
    for line in box:
        print(line)

    print("\nOval:")
    for line in oval:
        print(line)

    print("\nArrow:")
    for line in arrow:
        print(line)

    print("\nDiamond:")
    for line in diamond:
        print(line)

if __name__ == "__main__":
    display_shapes()