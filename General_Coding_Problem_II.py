def search(array,element):
	for i in array:
		if i==element:
			return 1
	return 0
class travel:
	def __init__(self,dist,min_dist,tot_st,array):
		self.dist=dist
		self.min_dist=min_dist
		self.tot_st=tot_st
		self.array=array
	def get_output(self):
		i,j,min,count=0,0,99999,0
		output_array=[]
		while j<self.tot_st:
			i=j
			while i<self.tot_st and self.array[j]<=self.min_dist:
				if search(self.array,self.array[i]+self.min_dist)==1:
					index=self.array.index(self.array[i]+self.min_dist)
					if self.array[i]+self.min_dist==self.dist:
						count+=1
						break
					count+=1
					i=index
				else:
					if self.array[i]+self.min_dist>self.dist:
						count+=1
						break
					else:
						count=0
						break
			output_array.append(count)
			count=0
			j+=1
		output_array.sort()
		return output_array[-1]
dist=int(input())
min_dist=int(input())
tot_st=int(input())
array=[]
for i in range(tot_st):
	array.append(int(input()))
test=travel(dist,min_dist,tot_st,array)
if test.get_output()==0:
	print('NOT POSSIBLE')
else:
	print(test.get_output())
