class cricket:
	def __init__(self,scores):
		self.scores=scores
	def total_score(self):
		total_score=0
		for score in self.scores:
			total_score=score+total_score
		return "Total Score : " + str(total_score)
	def b1_score(self):
		count=0
		b1=0
		b1_list=""
		for a in self.scores:
			if count==7:
				count=0
			if count==0 and a!=0 :
				b1=a+b1
				if b1_list=="":
					b1_list=b1_list+str(a)
				else:
					b1_list=b1_list+(" + "+str(a))
			if a!=0:
				count+=1
		return "Batsman 1 Score : "+str(b1) +str(" ("+b1_list+")")
	def b2_score(self):
			count=0
			b2=0
			b2_list=""
			for a in self.scores:
				if count==7:
					count=0
				if count!=0 and a!=0:
					b2=b2+a
					if b2_list=="":
						b2_list=b2_list+str(a)
					else:
						b2_list=b2_list+(" + "+str(a))
				if a!=0:
					count+=1
			return "Batsman 2 Score : "+str(b2) +str(" ("+b2_list+")")


scores=[1,2,0,0,4,1,6,2,1,3]
s1=cricket(scores)
print(scores)
print("")
print(s1.total_score())
print(s1.b1_score())
print(s1.b2_score())
print("")
print("Press enter to exit the program")
input()
