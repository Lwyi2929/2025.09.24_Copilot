
import random
import string
import argparse
import re


def generate_strong_password(length: int = 12) -> str:
    """
    產生一組強密碼，包含大寫、小寫、數字、特殊字元，長度預設12。
    參數:
        length (int): 密碼長度，預設12，最短8。
    回傳:
        str: 強密碼字串。
    """
    if length < 8:
        length = 8
    chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 4)
    random.shuffle(chars)
    return ''.join(chars)

def check_password_strength(password: str) -> str:
    """
    檢查密碼強度，根據長度、數字、大寫、小寫、特殊字元給分，回傳強度等級。
    規則：
        1. 長度大於8分數+1
        2. 含數字+1
        3. 含大寫+1
        4. 含小寫+1
        5. 含特殊字元+1
    回傳：
        "弱" (0-2分), "中" (3-4分), "強" (5分)
    """
    score = 0
    if len(password) > 8:
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中"
    else:
        return "強"

if __name__ == "__main__":
    """
    主程式：
    - 若有 --password 參數，檢查該密碼強度
    - 若無參數，自動產生一組強密碼並顯示
    - 可用 --length 指定產生密碼長度
    """
    parser = argparse.ArgumentParser(description="密碼強度檢查與強密碼產生器")
    parser.add_argument("--password", type=str, help="要檢查的密碼")
    parser.add_argument("--length", type=int, default=12, help="產生密碼長度 (預設12)")
    args = parser.parse_args()

    if args.password:
        print(f"密碼: {args.password}")
        print(f"強度: {check_password_strength(args.password)}")
    else:
        pwd = generate_strong_password(args.length)
        print(f"產生的強密碼: {pwd}")
        print(f"強度: {check_password_strength(pwd)}")
