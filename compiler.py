prompt = ['개', '서', '아', '아이', '우', '코', '현']

while True:
    l = []
    var = 0

    dir = input().split()

    if not dir[0] == "stand":
        raise SyntaxError
    if not dir[1].endswith(".standhw"):
        raise FileNotFoundError
    code = open(dir[1], 'r', encoding="UTF8")
    code = code.readline()
    if not (code.startswith("코") and code.endswith("아이")): # 코드의 시작과 끝이 "코"와 "아이"가 아니면
        raise SyntaxError
    if code.count("코") != 1 or code.count("아이") != 1: # 코드에 "코"나 "아이"가 한 개가 아니면
        raise SyntaxError
    for i in code:
        l.append(i)
    l.pop()
    l.pop()
    for i in l:
        if i == "코":
            pass
        if i == "서":
            var *= 2
        if i == "현":
            var -= 1
        if i == "우":
            var += 1
        if i == "아":
            print(chr(var), end="")
        if i == "개":
            var = 0
        if i == "아이":
            pass
    print()
