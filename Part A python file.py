#Part A
DieA=[1,2,3,4,5,6]
DieB=[1,2,3,4,5,6]
#Find Posible combinations
count=0
for i in DieA:
    for j in DieB:
        count=count+1
print("The total combinations =",count)
#Calculate and display the distribution of all possible combinations that can beobtained when rolling both Die A and Die B together. Show the math along with the code!
Mat=[]
for i in DieA:
    L=[]
    for j in DieB:
        total=i+j
        L.append(total)
    Mat.append(L)
print("Sum of all ombinations ")
for i in Mat:
    print(i)
#Probability
Mat=[]
uni=[]
D={}
for i in DieA:
    for j in DieB:
        total=i+j
        Mat.append(total)
        if total not in uni:
            uni.append(total)
for i in uni:
    D.update({i:Mat.count(i)})
print("Probability of all Possible Sums occurring among the number of combinations from (2)")
for i in D:
    print("P(Sum = ",i,") = ",D.get(i),"/",len(Mat)," = ",D.get(i)/len(Mat))

