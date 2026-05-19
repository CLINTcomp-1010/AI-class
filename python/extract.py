def extract_characters(name, n):
    #create a variable to store the extracted characters
    result_name = ""
    #index from the argument strings
    index = 0

    while index != n:
        result_name = result_name + name[index]
        index += 1

    return result_name



if __name__ == "__main__":
    n = int(input("enter n characters to be extracted: "))
    name = input("enter string:")
    print(extract_characters(name, n))