def count_substring(string,sub_string):
    """
    To print the number of occurances of the sub_string in the main string

    Args:
        string - input set of strings
        sub_string - sub_string needs to be searched for occurances.
    """

    occurances = 0
    # First check if the sub_string is present or not
    if sub_string not in string:
        print("String not found")

    # To find the number of instances and print it
    for i in range(len(string)):
        if sub_string in string:
            string = string.replace(sub_string, '', 1)
            occurances += 1

    print(occurances)


# if __name__ == "__main__":
a = raw_input("Enter the string: ")
b = raw_input("enter the string to be searched for occurances: ")
count_substring(a, b)

