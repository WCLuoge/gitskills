def convert(s, numRows):
    matrix=[]
    length=len(s)
    move=0
    while move<length:
        i=0
        k=0
        tp=[]
        try:
            while i<numRows:
                tp.append(s[move])
                move+=1
                i+=1
            matrix.append(tp)
            for k in range(numRows-2):
                tp=[False]*numRows
                tp[numRows-2-k]=s[move]
                matrix.append(tp)
                move+=1
        except:
            if len(tp)<numRows:
                matrix.append(tp)
            break
    
    while len(matrix[-1])<numRows:
        matrix[-1].append(False)
    ans=""
    for row in zip(*matrix):
        temp=[item for item in row if item]
        s_temp=''.join(temp)
        ans+=s_temp
    
        
    return ans

s = "PAYPALISHIRING"
numRows = 4
matrix=convert(s, numRows)
print(matrix)
        
            
                
        
    
            
    