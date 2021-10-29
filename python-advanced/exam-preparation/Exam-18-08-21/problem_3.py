def fill_the_box(height, length, width, *args):
    """
    """
    box_dimensions = height * length * width

    count_cubes_in_box = box_dimensions
    total_cubes = 0
    for cube in args:
        if cube == 'Finish':
            break
        else:
            total_cubes += int(cube)

    for arg in args:
        if arg == 'Finish':
            return f'There is free space in the box. You could put {count_cubes_in_box} more cubes.'
        
        if count_cubes_in_box - int(arg) < 0:
            return f'No more free space! You have {total_cubes - box_dimensions} more cubes.'
        
        count_cubes_in_box -= int(arg)


if __name__ == '__main__':
    print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
    print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
    print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
