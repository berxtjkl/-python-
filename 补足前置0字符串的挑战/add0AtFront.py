# from functools import reduce
def add0AtFront(*arg):
	resultList = []
	for i in arg:
		print(len(str(i)))
		maxLengthOne = 0
		if len(str(i))>maxLengthOne:
			maxLengthOne = len(str(i)) + 1
		print(maxLengthOne)
	for i in arg:
		tempSubfix0 = maxLengthOne-len(str(i))
		tempSubfix0 = tempSubfix0*'0'
		print(''.join([str(tempSubfix0), str(i)]))


if __name__ == "__main__":
    add0AtFront(1323,123123123,1,2222)




    # 测试用
    # print("asd"[-2:])
    # print("sda"[:2])
    # print("asd"[0:3-2]+"sda")
    # print(len("sd"))
