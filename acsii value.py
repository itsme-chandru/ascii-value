while True:
    char=input()
    if(type(char) != 'str' and len(char) != 1):
        print("Please enter character only")
    else:
        print("The ASCII value of '" + char + "' is", ord(char))
        break