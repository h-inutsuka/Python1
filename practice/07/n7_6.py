import random

def generate_secret_number():
    return [random.randint(0, 9) for _ in range(3)]

def get_guess():
    while True:
        guess = input("3桁の数字を入力してください: ")
        if len(guess) == 3 and guess.isdigit():
            return [int(digit) for digit in guess]
        else:
            print("無効な入力です。もう一度入力してください。")

def evaluate_guess(secret, guess):
    hits = 0
    blows = 0
    secret_checked = [False] * 3
    guess_checked = [False] * 3

    # ヒットをチェック
    for i in range(3):
        if guess[i] == secret[i]:
            hits += 1
            secret_checked[i] = True
            guess_checked[i] = True

    # ブローをチェック
    for i in range(3):
        if not guess_checked[i]:  # すでにヒットと判定された位置は除外
            for j in range(3):
                if not secret_checked[j] and guess[i] == secret[j]:
                    blows += 1
                    secret_checked[j] = True
                    break

    return hits, blows

def main():
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        attempts += 1
        guess = get_guess()
        hits, blows = evaluate_guess(secret_number, guess)
        
        print(f"ヒット: {hits}, ブロー: {blows}")
        
        if hits == 3:
            print(f"おめでとうございます！{attempts}回で正解を当てました。")
            break

if __name__ == "__main__":
    main()