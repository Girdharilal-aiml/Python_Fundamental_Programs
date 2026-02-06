def sort_dict_by_value():
    d = {'apple': 3, 'banana': 1, 'cherry': 2}
    sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
    print(f"Original: {d}")
    print(f"Sorted by value: {sorted_d}")
