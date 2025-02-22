def main():
    provinces_list = []
    with open("provinces.txt") as provinces:
        for line in provinces:
            line = line.strip()
            provinces_list.append(line)
       
    print (provinces_list)
    provinces_list.pop(0)
    provinces_list.pop() 
    ab_count = 0
    for i in provinces_list:
        if i == "AB":
            i = "Alberta"
        if i == "Alberta":
            ab_count += 1
    print(f"Alberta occurs {ab_count} times in the modified list")
    print(provinces_list)
if __name__ == "__main__":
    main()