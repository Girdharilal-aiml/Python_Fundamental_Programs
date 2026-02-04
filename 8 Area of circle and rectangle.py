def area_calculations():
    import math
    
    # Circle
    radius = float(input("Enter radius of circle: "))
    area_circle = math.pi * radius ** 2
    print(f"Area of circle: {area_circle:.2f}")
    
    # Rectangle
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area_rect = length * width
    print(f"Area of rectangle: {area_rect:.2f}")
