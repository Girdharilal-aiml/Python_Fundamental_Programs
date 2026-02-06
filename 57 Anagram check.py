def check_anagram():
    s1 = input("Enter first string: ").lower().replace(" ", "")
    s2 = input("Enter second string: ").lower().replace(" ", "")
    
    if sorted(s1) == sorted(s2):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")
