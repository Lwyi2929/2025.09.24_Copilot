#建立一個名為check_password_strength的函式，接受一個password字串
#規則1.檢查密碼長度是否大於8，如果是，分數+1
#規則2.檢查密碼是否包含至少一個數字，如果是，分數+1
#規則3.檢查密碼是否包含至少一個大寫字母，如果是，分數+1
#規則4.檢查密碼是否包含至少一個小寫字母，如果是，分數+1     
#規則5.檢查密碼是否包含至少一個特殊字元(非字母或數字)，如果是，分數+1
#最後根據總分回傳強度等級:"0-2分:弱", "3-4分:中", "5分:強"
import re
def check_password_strength(password: str) -> str:
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