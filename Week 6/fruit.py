def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    reverse_fruit_list = []
    print(f"original: {fruit_list}")

    for fruit in range((len(fruit_list)-1), -1, -1):
        # print (fruit)
        reverse_fruit_list.append(fruit_list[fruit])
    print(f"reversed: {reverse_fruit_list}")

    reverse_fruit_list.append("orange")
    print(f"append orange: {reverse_fruit_list}")

    apple_index = reverse_fruit_list.index("apple")
    reverse_fruit_list.insert(apple_index, "cherry")
    print(f"insert cherry: {reverse_fruit_list}")

    reverse_fruit_list.remove("banana")
    print(f"remove banana: {reverse_fruit_list}")

    item_to_remove = reverse_fruit_list[-1]
    reverse_fruit_list.pop()
    print(f"pop {item_to_remove}: {reverse_fruit_list}")

    reverse_fruit_list.sort()
    print(f"sorted: {reverse_fruit_list}")

    reverse_fruit_list.clear()
    print(f"cleared: {reverse_fruit_list}")





if __name__ == "__main__":
    main()