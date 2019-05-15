# 根据最大字串长度设置前缀0
def add0AtFront(*arg):
	print(arg)
	maxLengthOne = getMaxLength(arg)
	for i in arg:
		# print(maxLengthOne-len(str(i)))
		tempSubfix0 = (maxLengthOne-len(str(i)))*'0'
		print(''.join([str(tempSubfix0), str(i)]))
# 获取字符串组中最长的字串并返回
def getMaxLength(arg):
	resultList = []
	maxLengthOne = 0
	print(arg)	
	for i in arg:
		# print(maxLengthOne)
		# print(str(i),1)
		if len(str(i))>maxLengthOne:
			maxLengthOne = len(str(i)) + 1
	# print(maxLengthOne)
	return maxLengthOne

if __name__ == "__main__":
    add0AtFront(1323,123123123,1,2222)
