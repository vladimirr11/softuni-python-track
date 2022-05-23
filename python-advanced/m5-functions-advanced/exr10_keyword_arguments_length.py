def kwargs_length(**kwargs: dict):
    return len(kwargs)
    

dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
