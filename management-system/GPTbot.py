tasks = {}
task_id = 1

while True:
    print("")
    print("- - - - - - - - - -")
    print("1：タスクを追加🆕")
    print("2：タスクを表示👀")
    print("3：タスクを削除🗑️")
    print("4：タスクを検索🔍")
    print("5：タスクを完了✔️")
    print("6：未完了のタスクを表示👀")
    print("7：タスク進捗率を表示📊")
    print("8：作業を終了🛑")
    print("- - - - - - - - - -")
    print("")

    user = input("選択肢を入力してください：")

    if user == "1":
        task_name = input("追加するタスク名を入力してください：")
        task_deadline = input("タスクの締め切りを入力してください（例：2024-07-31）：")
        tasks[task_id] = {"name": task_name, "completed": False, "deadline": task_deadline}
        print("【タスクが追加されました🆕】")
        task_id = task_id + 1

    elif user == "2":
        if len(tasks) == 0:
            print("【タスクはありません❌】")
        else:
            print("【表示結果👀】")
            for id in tasks:
                task = tasks[id]
                status = "完了✔️" if task["completed"] else "未完了❌"
                print(f"{id}: {task['name']} - {status} - 締め切り: {task['deadline']}")

    elif user == "3":
        del_id = int(input("削除するタスクIDを入力してください："))
        if del_id in tasks:
            del tasks[del_id]
            print("【タスクが削除されました🗑️】")
        else:
            print("【タスクはありません❌】")

    elif user == "4":
        search_name = input("検索するタスク名を入力してください：")
        search_tasks = []
        for id in tasks:
            task = tasks[id]
            if search_name in task["name"]:
                status = "完了✔️" if task["completed"] else "未完了❌"
                search_tasks.append(f"{id}: {task['name']} - {status} - 締め切り: {task['deadline']}")
        if search_tasks:
            print("【検索結果🔍】")
            for result in search_tasks:
                print(result)
        else:
            print("【タスクはありません❌】")

    elif user == "5":
        complete_id = int(input("完了するタスクIDを入力してください："))
        if complete_id in tasks:
            tasks[complete_id]["completed"] = True
            print("【タスクが完了しました✔️】")
        else:
            print("【タスクはありません❌】")

    elif user == "6":
        if len(tasks) == 0:
            print("【タスクはありません❌】")
        else:
            print("【未完了のタスク👀】")
            for id in tasks:
                task = tasks[id]
                if not task["completed"]:
                    print(f"{id}: {task['name']} - 未完了❌ - 締め切り: {task['deadline']}")

    elif user == "7":
        if len(tasks) == 0:
            print("【タスクはありません❌】")
        else:
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks.values() if task["completed"])
            progress = (completed_tasks / total_tasks) * 100
            print(f"【タスク進捗率📊】")
            print(f"完了タスク: {completed_tasks}/{total_tasks} ({progress:.2f}%)")

    elif user == "8":
        print("作業を終了します🛑")
        break

    else:
        print("無効な選択肢です🚨もう一度試してください👀")
