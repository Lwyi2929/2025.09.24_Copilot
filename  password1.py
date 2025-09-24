#建立一個名為check_password_strength的函式，接受一個password字串
#規則1.檢查密碼長度是否大於8，如果是，分數+1
#規則2.檢查密碼是否包含至少一個數字，如果是，分數+1
#規則3.檢查密碼是否包含至少一個大寫字母，如果是，分數+1
#規則4.檢查密碼是否包含至少一個小寫字母，如果是，分數+1     
#規則5.檢查密碼是否包含至少一個特殊字元(非字母或數字)，如果是，分數+1
#最後根據總分回傳強度等級:"0-2分:弱", "3-4分:中", "5分:強"

import re
import random
import string
import sys

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

def generate_strong_password(length: int = 12) -> str:
    """
    產生一組強密碼，包含大寫、小寫、數字、特殊字元，長度預設12。
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

if __name__ == "__main__":
    """
    主程式：
    - 若有命令列參數，檢查該密碼強度
    - 若無參數，自動產生一組強密碼並顯示
    """
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(f"密碼: {password}")
        print(f"強度: {check_password_strength(password)}")
    else:
        pwd = generate_strong_password()
        print(f"產生的強密碼: {pwd}")
        print(f"強度: {check_password_strength(pwd)}")

#請將我選取的這兩個函式，重構成一個完整的Python腳本。需求如下:讓這個腳本可以從命令列(終端間)執行。
#如果執行時給了一個密碼作為參數，就檢查該密碼的強度。
#如果沒有給任何參數，腳本就呼叫聲成密碼的函示，並印出一個新的強密碼。
#請加上if __name__ == "__main__":的保護區塊來處理執行編輯。
#為所有函式加上適當的文件字串(docstrings)。