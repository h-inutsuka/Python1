import json
import datetime

tasks = {}
task_id = 1
file_name = "tasks.json"

def load_tasks(file_name):
    global tasks, task_id
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            tasks = {int(k): v for k, v in data.get("tasks", {}).items()}
            task_id = max(tasks.keys(), default=0) + 1 if tasks else 1
    except FileNotFoundError:
        pass

def save_tasks(file_name):
    with open(file_name, "w") as file:
        json.dump({"tasks": tasks}, file)

def add_task():
    global task_id
    try:
        task_name = input("追加するタスク名を入力してください：")
        deadline_str = input("このタスクの締め切り（YYYY-MM-DD）を入力してください：")
        deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d").date()
        tasks[task_id] = {"name": task_name, "progress": 0, "deadline": deadline, "completed": False}
        print("【タスクが追加されました🆕】")
        task_id += 1
    except ValueError:
        print("【無効な日付形式です❌】")

def display_tasks():
    if not tasks:
        print("【タスクはありません❌】")
    else:
        print("【表示結果👀】")
        for id, task in tasks.items():
            status = "完了" if task["completed"] else "進行中"
            deadline_str = task["deadline"].strftime("%Y-%m-%d")
            print(f"{id}: {task['name']} (締め切り: {deadline_str}, 状態: {status})")

def delete_task():
    try:
        del_id = int(input("削除するタスクIDを入力してください："))
        if del_id in tasks:
            del tasks[del_id]
            print("【タスクが削除されました🗑️】")
        else:
            print("【タスクはありません❌】")
    except ValueError:
        print("【無効な入力です❌】")

def search_tasks():
    search_name = input("検索するタスク名を入力してください：")
    search_results = [
        f"{id}: {task['name']} (締め切り: {task['deadline'].strftime('%Y-%m-%d')}, 状態: {'完了' if task['completed'] else '進行中'})"
        for id, task in tasks.items() if search_name in task["name"]
    ]
    if search_results:
        print("【検索結果🔍】")
        for result in search_results:
            print(result)
    else:
        print("【タスクはありません❌】")

def update_progress():
    try:
        update_id = int(input("進捗を更新するタスクIDを入力してください："))
        if update_id in tasks:
            tasks[update_id]["completed"] = True
            print(f"【タスクが完了しました✔️】")
        else:
            print("【タスクはありません❌】")
    except ValueError:
        print("【無効な入力です❌】")

def greet_user():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "おはようございます🌅"
    elif 12 <= current_hour < 18:
        greeting = "こんにちは☀️"
    else:
        greeting = "こんばんは🌙"
    print(greeting)

def main():
    greet_user()
    load_tasks(file_name)
    
    while True:
        print("")
        print("- - - - - - - - - -")
        print("1：タスクを追加🆕")
        print("2：タスクを表示👀")
        print("3：タスクを削除🗑️")
        print("4：タスクを検索🔍")
        print("5：タスクの完了を登録✔️")
        print("6：作業を終了🛑")
        print("- - - - - - - - - -")
        print("")
        
        user = input("選択肢を入力してください：")

        if user == "1":
            add_task()
        elif user == "2":
            display_tasks()
        elif user == "3":
            delete_task()
        elif user == "4":
            search_tasks()
        elif user == "5":
            update_progress()
        elif user == "6":
            save_tasks(file_name)
            print("作業を終了します🛑")
            break
        else:
            print("無効な選択肢です🚨もう一度試してください👀")

if __name__ == "__main__":
    main()
