def my_handler(cmd, val, data):
    """
    Обрабатывает данные согласно команде
        cmd: команда (filter, map, limit, unique, sort)
        val: значение для команды
        data: список строк или итератор
    return:
        обработанные данные в виде списка строк
    """
    if cmd == "filter":
        res = list(filter(lambda line: val in line, data))
    elif cmd == "map":
        res = [line.split()[int(val)] for line in data if len(line.split()) > int(val)]
    elif cmd == "limit":
        res = list(data)[:int(val)]
    elif cmd == "unique":
        res = list(set(data))
    elif cmd == "sort":
        is_reverse = val == "desc"
        res = sorted(data, reverse=is_reverse)
    else:
        raise ValueError(f"Неизвестная команда: {cmd}")

    return res