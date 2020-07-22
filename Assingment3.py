'''Question1: sum of n (n=10) numbers with the help of while loop'''
sum=0
i=1
while i<=10:
	sum=sum+i
	i=i+1
	print(sum)
#Output: 55




'''Question2: Take a integer and find prime or not'''
num=13
for i in range(2,num):
	if num%i==0:
		print("Not prime")
		break
else:
	print("Prime")
#Output: Prime

