def record_unique_names(num_names):
    """
    """
    my_set = set(input() for _ in range(num_names))
    
    [print(name) for name in my_set]


record_unique_names(int(input()))
