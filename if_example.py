# def main():
#     condition = True

#     if condition:
#         print("The condition is True")

#     Print("Hello world!")



# def main():
#     condition = False

#     if condition:
#         print("The condition is True")
#     else:
#         print("Th conditional is false")

#     Print("Hello world!")

#IF__ELIF__ELSE
#def main():
# record_count = 23

# if record_count > 5:
#         print("The record count are > 5")
# elif record_count <= 22:
#         print("Records count are > 22 and <= 5")
# else:
#         print("Th conditional is false")

# print("Hello world!")


# While
# def main():
#     counter = 10 

#     while counter >= 0:
#         print("Counter:", counter)
# #        counter = counter - 1    
#         counter -= 1    #Shortcut, sugar syntax

#     print("Hello World")

# if __name__ == "__main__":
#     main()



def main():
    user_id = "" 

    while not user_id.isnumeric():
        user_id = input("Type your user id:")

    print("The user has id:", user_id)

if __name__ == "__main__":
    main()