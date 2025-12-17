from function import *


tasks = []

while True:
    print("1. Добавить задачу 2. Показать задачи 3. Выход", sep="\n")
    choice = input("Выберите: ")
    if choice == "1":
        sureAboutadd(tasks)
        print("Хотите посмотреть полный список задач?")
        print("1. ДА/2. НЕТ")
        if choice == "2":
            fulltasks(tasks)
            removeTask(tasks)


    elif choice == "2":
        if len(tasks) == 0:
            print("📭Вы пока не добавили ни одной задачи")
            print()
        else:
            print("📋Полный список задач:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            print()
    elif choice == "3":
        print("👋 До свидания!")
        break