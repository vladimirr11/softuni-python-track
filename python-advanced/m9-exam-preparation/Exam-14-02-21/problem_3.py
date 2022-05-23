def stock_availability(inventory_list: list, command, *args):
    if command == 'delivery' and args:
        for x in args:
            inventory_list.append(x)

    if command == 'sell' and args:
        if isinstance(args[0], int):
            num_iter = args[0]

            if num_iter >= len(inventory_list):
                num_iter = len(inventory_list)

            for _ in range(num_iter):
                del inventory_list[0]
        else:
            for arg in args:
                if arg in inventory_list:
                    while arg in inventory_list:
                        inventory_list.remove(arg)

    elif command == 'sell':
        del inventory_list[0]

    return inventory_list


if __name__ == '__main__':
    print(stock_availability(
        ["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
    print(stock_availability(["chocolate", "vanilla",
          "banana"], "delivery", "cookie", "banana"))
    print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
    print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
    print(stock_availability(
        ["chocolate", "chocolate", "banana"], "sell", "chocolate"))
    print(stock_availability(
        ["cookie", "chocolate", "banana"], "sell", "chocolate"))
    print(stock_availability(
        ["chocolate", "vanilla", "banana"], "sell", "cookie"))
