from func import *


tasks = []

while True:
    print("1. Добавить задачу ",
          "2. Посмотреть задачи",
          "3. Удалить задачу",
          "4. Выход",
          "5. Выполнить задачу",
          "6. Загрузить из файла",
          "7. Поиск задач",
          "8. Статистика",
          "9. Выход",
          sep="\n")
    choiceTask = input("Выберите действие: ")

    # Добавление задач
    if choiceTask == "1":
        addTasks()

    # показ задач
    elif choiceTask == "2":
        showTasks()

    # Удаление задач
    elif choiceTask == "3":
        removesTasks()

    elif choiceTask == "9":
        break



