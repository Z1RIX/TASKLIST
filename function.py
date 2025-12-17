
def sureAboutadd(tasks):
    task = input("Задача: ")
    print(f"Вы уверены, что хотите сохранить задачу '{task}'?")
    print("1.ДА/2.НЕТ")
    choice2 = input("Выберите: ")
    if choice2 == "1":
        tasks.append(task)
        print(f"Задача: {task} успешно добавлена✅")
    if choice2 == "2":
        print("Задача не сохранена")

def fulltasks(tasks):
    choice3 = input()
    print()
    if choice3 == "1":
        print("Полный список задач:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def removeTask(tasks):
    print("Хотите удалить задачу?")
    print("1. ДА/2. НЕТ")
    choice1 = input()
    if choice1 == "1":
        print("Под каким номером находится задача которую вы хотите удалить?")
        choiceRemove = int(input())

        if choiceRemove > len(tasks):
            print("Задачи под таким номером нет")
        else:
            del tasks[choiceRemove]