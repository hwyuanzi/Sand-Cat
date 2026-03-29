from sandcat_fun import (
    cat_greeting,
    cat_comfort,
    cat_fortune,
    draw_cat,
    get_fortune,
)

def main():
    print("=== Sand Cat Package Demo ===\n")

    print("1. Greeting")
    print(cat_greeting("Tuo", "happy"))
    print()

    print("2. Comfort")
    print(cat_comfort(3))
    print()

    print("3. Draw")
    print(draw_cat("coding"))
    print()

    print("4. Cat Fortune")
    print(cat_fortune("sunny", 8))
    print()

    print("5. Get Fortune")
    print(get_fortune(5))
    print()


if __name__ == "__main__":
    main()