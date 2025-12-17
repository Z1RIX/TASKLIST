from main import *


def addTasks():
    choice = input("Введите задачу: ")
    print(f"Вы уверены что хотите сохранить задачу '{choice}'?")
    print("1. ДА/2. НЕТ")
    sub = input()
    if sub == "1" or sub == "ДА":
        tasks.append(choice)
        print(f"Задача {choice} успешно сохранена✅")

def showTasks():
    if len(tasks) == 0:
        print("Вы еще не добавили ни одной задачи!")
    else:
        print("------СПИСОК ЗАДАЧ------")
        print()
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    print()
    print()

def removesTasks():
    if len(tasks) == 0:
        print("Вы еще не добавили ни одной задачи!")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    print()
    sub3 = int(input("Введите номер задачи для удаления: ")) - 1
    print()
    if 0 <= sub3 < len(tasks):
        removed = tasks.pop(sub3)
        print(f"Задача '{removed}' успешно удалена! ✅")
    else:
        print("Задачи под таким номером не существует❌")