
def excution(n,count):
    
    a=[]
    if n<7:    
        a.append(n)
        x=n   
        while True:
        
            y=x+3 
            if y>72:
                break
            else:
                a.append(y)
            z=y+5
            if z>72:
                break
            else:
                a.append(z)
                x=z
        if count>=len(a):
            print("Preferred tickts are not availble")
        else:
            print("Your seat number is",a[count-1])                                                                        
            
    else:
        
        a.append(n)
        x=n
        while True:
            y=x+8
            if y>72:
                break
            else:
                a.append(y)
                x=y
        if count>=len(a):
             print("tickts are not availble with your preference")    
        else:
             print("your seat allocation number is",a[count-1])

