test = input()
try:
    before = eval(test)
    after = {}
    for key in before:
        after[before[key]] = key
    print(after)
except:
    print("输入错误")