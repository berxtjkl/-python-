from functools import reduce
def addStr(arg1, arg2):
    # 防止使用者传入数字, 导致len()函数报错
    arg1, arg2 = setToStr(arg1, arg2)
    # 存放元素的长度用于判断最小循环次数
    lenArg1, lenArg2 = len(arg1), len(arg2)
    # 获取数组里面小的元素的长度, 按照小的元素长度去循环比较
    minOne = min(lenArg1, lenArg2)
    # 这里循环minOne次, 从1-minOne的数值大小, 如果minOne=3, 则循环1,2,3三次, 起始i是从1开始哟
    for i in range(1, minOne+1):
        if arg1[-i:] == arg2[:i]:
            # 把符合规则的字符串连起来并保存
            tempAddStr = arg1[0:lenArg1-i]+arg2
    return tempAddStr

def setToStr(set1, set2):
    return str(set1), str(set2)

if __name__ == "__main__":
    print(reduce(addStr, ["pizza","apple","letter"]))
    # 测试用
    # print("asd"[-2:])
    # print("sda"[:2])
    # print("asd"[0:3-2]+"sda")
    # print(len("sd"))
