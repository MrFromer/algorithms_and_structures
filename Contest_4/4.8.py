def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Считываем количество задач и баллов за задачу
    n = int(data[0])
    c = int(data[1])

    # Считываем задачи
    tasks = []
    for i in range(n):
        s = int(data[2 + 2 * i])
        t = int(data[3 + 2 * i])
        tasks.append((s, t, i + 1))  # (время начала, время решения, номер задачи)

    # Сортируем задачи по времени окончания (s_i + t_i)
    tasks.sort(key=lambda x: x[0] + x[1])

    # Жадный выбор задач
    selected_tasks = []
    last_end_time = -1  # Время окончания последней выбранной задачи

    for task in tasks:
        s, t, idx = task
        if s >= last_end_time:  # Если задача не пересекается с последней выбранной
            selected_tasks.append(idx)
            last_end_time = s + t  # Обновляем время окончания

    # Вычисляем максимальное количество баллов
    max_score = len(selected_tasks) * c

    # Выводим результат
    print(max_score)
    print(len(selected_tasks))
    print(" ".join(map(str, selected_tasks)))

if __name__ == "__main__":
    main()