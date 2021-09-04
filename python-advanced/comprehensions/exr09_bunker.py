def get_quality_quantity_sums(items_lst):
    """
    """
    quantity_sum = 0
    quality_sum = 0
    for qq in items_lst:
        quantity, quality = qq.split(';')
        _, quantity_num = quantity.split(':')
        _, quality_num = quality.split(':')
        quantity_sum += int(quantity_num)
        quality_sum += int(quality_num)
    
    return (quantity_sum, quality_sum)


def get_bunker_items(keys, num_items):
    """
    """
    items_category_dict = {k: [] for k in keys.split(', ')}

    items_lst = [[items for items in input().split(' - ')] for _ in range(num_items)]

    for i in range(len(items_lst)):
        for j in range(len(items_lst[0])):
            if j == 0:
                items_category_dict[items_lst[i][j]].append(items_lst[i][j + 1])

    quantity_quality_lst = [row[indx] for row in items_lst for indx in range(len(row)) if indx == 2]

    quantity_sum, quality_sum = get_quality_quantity_sums(quantity_quality_lst)
    
    print(f'Count of items: {quantity_sum}')
    print(f'Average quality: {quality_sum  / len(items_category_dict):.2f}')

    {print(f'{k} -> {", ".join(v)}') for (k, v) in items_category_dict.items()}


get_bunker_items(input(), int(input()))
