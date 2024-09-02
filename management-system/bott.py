tasks = {}
task_id = 1

import datetime
dt_now = datetime.datetime.now()
# タスク表示機能がある（display_tasks関数）
def display_tasks():
    if len(tasks) == 0:
        print("現在、タスクはありません。")
    else:
        print("現在のタスク一覧です：")
        for id in tasks:
            print(f"{id}. {tasks[id]['task_name']} - 締め切り：{tasks[id]['closing']} - 状態：{tasks[id]['task_situation']}")
# タスク追加機能がある（add_task関数）
def add_task():
    global task_id
    task_name = input("タスク名を入力してください：")
    closing = input("締め切りを入力してください：")
    task_situation = '未完了'
    tasks[task_id] = {"task_name": task_name, "closing": closing, "task_situation": task_situation}
    print(f"タスク '{task_name}' が追加されました")
    task_id += 1
# タスク進捗率計算機能がある（calculate_completion関数）
def calculate_completion():
    if len(tasks) == 0:
        print("現在、タスクはありません。")
    else:
        completed_tasks = [task for task in tasks.values() if task["task_situation"] == "完了"]
        total_tasks = len(tasks)
        completion_rate = len(completed_tasks) / total_tasks * 100
        print(f"タスクの進行率は {completion_rate:.2f}% です。")
# タスク完了マーク機能がある（mark_task_complete関数）
def mark_task_complete():
    if len(tasks) == 0:
        print("現在、タスクはありません。")
    else:
        print('現在のタスク一覧です：')
        for id in tasks:
            print(f"{id}. {tasks[id]['task_name']} - 締め切り：{tasks[id]['closing']} - 状態：{tasks[id]['task_situation']}")
        print('')
        completion = int(input('完了にするタスクの番号を入力してください：'))
        if completion in tasks:
            tasks[completion]['task_situation'] = '完了'
            print(f"タスク '{tasks[completion]['task_name']}' を完了にしました。")
        else:
            print("無効なタスク番号です")

def delete_tasks():
    del_id = int(input("削除するタスクIDを入力してください："))
    if del_id in tasks:
        del tasks[del_id]
        print("【タスクが削除されました】")
    else:
        print("【タスクはありません】")
# 起動時に時刻に応じた返答があり、メニューが表示される
while True:
    if dt_now.hour < 9:
        print('おはようございます！タスク管理ボットへようこそ。')
    elif 9 <= dt_now.hour < 18:
        print('こんにちは！タスク管理ボットへようこそ。')
    else:
        print('こんばんは！タスク管理ボットへようこそ。')

    print("")
    print("メニュー：")
    print("1：タスクを表示")
    print("2：タスクを追加")
    print("3：タスク進行状況の計算")
    print("4：タスクの完了をマーク")
    print("5：タスクの削除")
    print("6：終了")

    user = input("選択してください：")

    try:
        if user == "1":
            display_tasks()

        elif user == "2":
            add_task()

        elif user == "3":
            calculate_completion()

        elif user == "4":
            mark_task_complete()

        elif user == "5":
            delete_tasks()

        elif user == "6":
            print("作業を終了します。さようなら！")
            break

        else:
            print("無効な選択肢です!もう一度試してください")

    except ValueError:
        print("入力が無効です。数値を入力してください。")
    except Exception as e:
        print(f"エラーが発生しました：{e}")