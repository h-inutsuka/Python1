tasks = {}
task_id = 0
task_name = []
task_deadline = []
task_situation = []
task_List = []
deadline = 0
# 起動時に時刻に応じた返答があり、メニューが表示される
import time
import datetime
dt_now = datetime.datetime.now()

while True:
    if dt_now.hour < 9:
        print('おはようございます！タスク管理ボットへようこそ。')
    elif 9 < dt_now.hour < 18:
        print('こんにちは！タスク管理ボットへようこそ。')
    else:
        print('こんばんは！タスク管理ボットへようこそ。')
# 起動時に時刻に応じた返答があり、メニューが表示される
    print("")
    print("メニュー：")
    print("1：タスクを表示")
    print("2：タスクを追加")
    print("3：タスク進行状況の計算")
    print("4：タスクの完了をマーク")
    print("5：タスクの削除")
    print("6：終了")

    user = input("選択してください：")

# タスク表示機能がある（display_tasks関数）
    if user == "1":
        if len(tasks) == 0:
            print("現在、タスクはありません。")
        else:
            print("現在のタスク一覧です：")
            for id in range(len(tasks)):
                print(f"{id}. {tasks[id]["task_name"]} - 締め切り：{tasks[id]["closing"]} - 状態：{tasks[id]["task_situation"]}")
# タスク追加機能がある（add_task関数）
    elif user == "2":
        task_name = input("タスク名を入力してください：")
        closing = input("締め切りを入力してください：")
        task_situation = '未完了'
        tasks[task_id] = {"task_name":task_name,"closing":closing,"task_situation":task_situation}
        print(f"タスク{task_name}が追加されました")
        task_id = task_id + 1

    elif user == "3":
        del_id = int(input("削除するタスクIDを入力してください:"))
        if del_id in tasks:
            del tasks[del_id]
            print("【タスクが削除されました】")
        else:
            print("【タスクはありません】")

    elif user == "4":
        print('現在のタスク一覧です：')
        for id in range(len(tasks)):
            print(f"{id}. {tasks[id]["task_name"]} - 締め切り：{tasks[id]["closing"]} - 状態：{tasks[id]["task_situation"]}")
        print('')
        completion = input('完了にするタスクの番号を入力してください：')
        if completion in tasks:
            tasks[completion]['task_situation'] = '完了'
        print(f'タスク{tasks[id]["task_name"]}を完了にしました。')

    elif user == "5":
        del_id = int(input("削除するタスクIDを入力してください:"))
        if del_id in tasks:
            del tasks[del_id]
            print("【タスクが削除されました】")
        else:
            print("【タスクはありません】")

    elif user == "6":
        print("作業を終了します。さようなら！")
        break

    else:
        print("無効な選択肢です!もう一度試してください")
