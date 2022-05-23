def math_operations(*args, a=None, s=None, d=None, m=None):
    kwargs_dict = {
        'a': a, 's': s, 'd': d, 'm': m,
    }

    hellper_dict = {
        1: 'a', 2: 's', 3: 'd', 4: 'm',
    }

    id = 0
    for arg in args:
        id += 1
        if id > 4:
            id = 1

        curr_kwarg_pos = hellper_dict[id]

        if curr_kwarg_pos == 'a':
            kwargs_dict[curr_kwarg_pos] += arg
        elif curr_kwarg_pos == 's':
            kwargs_dict[curr_kwarg_pos] -= arg
        elif curr_kwarg_pos == 'd':
            if arg == 0:
                continue
            else:
                kwargs_dict[curr_kwarg_pos] /= arg
        elif curr_kwarg_pos == 'm':
            kwargs_dict[curr_kwarg_pos] *= arg

    return kwargs_dict


print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
