from os.path import isfile as exist
from os import system as cmd

functions = ['개', '딱', '서', '아', '우', '현']

while True:
    var = 0
    string = ""

    dir = input().split()
    # 예외 처리
    if exist(dir[1]):
        code = open(dir[1], 'r', encoding="UTF8")
        code = code.readline()
    else: # 파일이 없으면
        raise FileNotFoundError
    if dir[0] != "stand": # 명령어가 올바르지 않으면
        raise SyntaxError
    if not dir[1].endswith(".shw"): # 확장자가 올바르지 않으면
        raise ValueError
    if len(dir) != 2: # 명령어가 올바르지 않거나 파일 이름에 공백이 있으면
        raise SyntaxError
    if not (code.startswith("코") and code.endswith("아이")): # 코드의 시작과 끝이 "코"와 "아이"가 아니면
        raise SyntaxError
    if code.count("코") != 1 or code.count("아이") != 1: # 코드에 "코"나 "아이"가 한 개가 아니면
        raise SyntaxError
    code = code[1:-2]
    if not (all(i in functions for i in code) or code == ""):  # 이상한 글자 있으면
        raise SyntaxError
    for i in code:
        if i == "서":
            var *= 2
        if i == "현":
            var = 0
        if i == "우":
            var += 1
        if i == "아":
            print(chr(var), end="")
            string += str(chr(var))
        if i == "개":
            var -= 1
        if i == "딱":
            f = open("temp.py", 'w', encoding="UTF8")
            f.write(string)
            f.close()
            cmd("python temp.py")
            cmd("del temp.py")
    print()
