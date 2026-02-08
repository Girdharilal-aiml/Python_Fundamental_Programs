# 16.3 Use random module
def use_random_module():
    import random
    
    print(f"Random number: {random.randint(1, 100)}")
    print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
    
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print(f"Shuffled list: {lst}")