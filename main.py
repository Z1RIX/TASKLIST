tasks = []



while True:
    print("1. Добавить задачу ",
          "2. Посмотреть задачи",
          "3. Удалить задачу",
          "4. Выход",sep="\n")
    choiceTask = input("Выберите действие: ")
    if choiceTask == "1":
        choice = input("Введите задачу: ")
        print(f"Вы уверены что хотитет сохранить задачу '{choice}'?")
        print("1. ДА/2. НЕТ")
        sub = input()
        if sub == "1" or sub == "ДА":
            tasks.append(choice)
            print(f"Задача {choice} успешно сохранена")
    elif choiceTask == "2":
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    elif choiceTask == "3":
        sub3 = input("Для удаления ведите номер под которым находится задача: ")




