def main():
    camel = input("camelCase: ")
    print("snake_case:", convert_to_snake(camel))


def convert_to_snake(camel):
    snake = camel[0].lower()  #change first index to lowercase
    for char in camel[1:]:  #check each index from 1 onwards
        if char.isupper():  #if uppercase
            snake += "_" + char.lower() #add _ and change to lowercase
        else:
            snake += char
    return snake #print the changes made


main()
