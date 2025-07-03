tasks = []

def add_task(task): 
    tasks.append(task)
    print(f"Завдання '{task}' додано.")

def remove_task(task): 
    if task in tasks: 
        tasks.remove(task)
        print(f"Завдання '{task}' видалено.")
    else: 
        print("Завдання не знайдено.")

def show_tasks(): 
    if tasks: 
        print("Список завдань:")
        for i, task in enumerate(tasks, 1): 
            print(f"{i}. {task}")
    else: 
        print("Список завдань порожній.")

def main(): 
    while True: 
        print("\n1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Показати завдання")
        print("4. Вихід")
        choice = input("Виберіть дію (1-4): ")

        if choice == "1":
            task = input("Введіть завдання: ")
            add_task(task)
        elif choice == "2":
            task = input("Введіть завдання для видалення: ")
            remove_task(task)
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()