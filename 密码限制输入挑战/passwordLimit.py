# 检查是否存在字母和数字
def checkDigitalAlpha(arg):
	for x in arg:
		if x.isdigit() or x.isalpha():
			print(x)
		else:
			print("含有数字和字母以外的字符串")

# 检查字符长度
def checkLength(arg):
	if len(arg)>=6:
		print("长度超过6")
	else:
		print("长度小于6")

# 检查是否有三个一样的
def checkThreeRepeat(arg):
	count = 0
	for x in range(len(arg)-1):
		if arg[x] == arg[x+1]:
			count += 1
		else:
			count = 0
		if count == 2:
			print("三个连续一样的")

if __name__ == "__main__":
	checkDigitalAlpha("123klj")
	checkLength("123kl")
	checkThreeRepeat("1233")