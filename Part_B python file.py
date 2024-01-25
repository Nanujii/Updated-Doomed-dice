def prob(DieA,DieB):
    Mat=[]
    uni=[]
    D={}
    for i in DieA:
        for j in DieB:
            total=i+j
            Mat.append(total)
            if total not in uni:
                uni.append(total)
    uni.sort()
    for i in uni:
        D.update({i:(Mat.count(i)/36)})
    return D

def all_com():
    listD = []
    for b in range(2, 9):
        for c in range(b, 9):
            for d in range(c, 9):
                for e in range(d, 9):
                    for f in range(e, 9):
                        dice = [1, b, c, d, e, f]
                        listD.append(dice)

    return listD
def undoom_dice(DieA,DieB):
    org=prob(DieA,DieB)
    L=[]
    for i in all_com():
        H=0
        for j in i: 
            if j<=4:
                H=H+1
            else:
                break
        if H==6:
            L.append(i)
            
    for i in L:
        for j in all_com():
            D1=prob(i,j)
            if org==D1:
                return (i,j)
            
Die_A=[1,2,3,4,5,6]
Die_B=[1,2,3,4,5,6]

New_Die_A,New_Die_B = undoom_dice(Die_A, Die_B)

print("Input Die_A:", Die_A)
print("Input Die_B:", Die_B)
print("Transformed Die_A:", New_Die_A)
print("Transformed Die_B:", New_Die_B)





