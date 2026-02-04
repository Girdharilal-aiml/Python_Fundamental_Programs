def formatted_output():
    name = "Python"
    version = 3.11
    
    # f-string
    print(f"Language: {name}, Version: {version:.2f}")
    
    # format method
    print("Language: {}, Version: {:.2f}".format(name, version))
    
    # % formatting
    print("Language: %s, Version: %.2f" % (name, version))

