def create_list_dynamically():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)
    print(f"List: {lst}")