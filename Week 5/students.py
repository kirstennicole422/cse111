import csv
def inum_to_digits(inum):
    # if inum.isdigit:
    #     return inum
# else:
    new_inum = []
    for i in inum:
        if i != "-":
            new_inum.append(i)
    return ("".join(new_inum).strip())
    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
  Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
    to use as the keys in the dictionary.
  Return: a compound dictionary that contains
  the contents of the CSV file.
  """
    student_dictionary = {}
    with open (filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            student_dictionary[key] = row
    return student_dictionary

def main():
    student_dictionary = read_dictionary("students.csv", 0)
    
    inum = input("Please enter an I-number (xxxxxxxxx) or type QUIT to exit: ")
    
    
    # print(f"{inum} as digit")
    while inum.lower() !="quit":
        inum = inum_to_digits(inum)
        if inum.isdigit():
            pass
        else: 
            print("Invalid I-Number")
            break
        if len(inum) < 9:
            print("Invalid I-Number: too few digits")
            break
        elif len(inum) > 9:
            print("Invalid I-Number: too many digits")
            break
        else:
            if inum in student_dictionary:
                name = student_dictionary[inum][1]
                print(name)
            else:
                print("No such student")
        inum = input("Please enter an I-number (xxxxxxxxx) or type QUIT to exit:")

    
if __name__ == "__main__":
    main()