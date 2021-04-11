cvf=0
import os
import binascii

namez = input("cl or for compress ul for extract? ")
            
if namez=="ul":
    name = input("What is name of file? ")
    namea="file.WhiteHall"
    namem=""
    namema="?"
   
    blockw=5
    blockw1=4
    nameas=name
    nac=len(nameas)
    if nameas[nac-4:nac]==".bin":
        nameas=nameas[0:nac-4]
    countraz=0
    cvf=2
    cvf1=0
    s=""
    e2=0
    e3=2
    e4=""
    c=2
    sw=2
    elw=0
 
    sda3=""
    sda2=""

    sscvf=0
    
    qqqqwzl=0
   
    with open(nameas, "w") as f4:
            f4.write(s)
    with open(nameas, "a") as f3:
            f3.write(s)
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        lenf1=len(data)
        lenf5=len(data)
        
        
        if lenf1<6:
            print("This file is too small");
            raise SystemExit
        if lenf1>(2**32)-1:
            print("This file is too big");
            raise SystemExit

        assx=0
        qqqwz=0
       
        while assx<10:
       
            aas1=0
            a1=0
            
            cvf=cvf+1
            
            
            countraz=countraz+1

            with open(nameas, "ab") as f2:
                if countraz==1:
                    sda=bin(int(binascii.hexlify(data),16))[2:]
                    lenf=len(sda)
                    lenf1=len(data)
                
                    xc=(lenf1*8)-lenf
                    z=0
                    if xc!=0:
                        while z<xc:
                            sda="0"+sda
                            z=z+1


                    
                    
                    
                    
                    
                    
                    sda=sda+sda2

                    
                    sda2="000000000011001100000000"+sda
            
                    n = int(sda2, 2)
                
                    qqwslenf=len(sda2)
                    qqwslenf=(qqwslenf/8)*2
                    qqwslenf=str(qqwslenf)
                    qqwslenf="%0"+qqwslenf+"x"
             
                    jl=binascii.unhexlify(qqwslenf % n)
                    sssssw=len(jl)
                    
                    data=jl
                    qqqwz=qqqwz+1
                    
                
                    if countraz==1:
                        
                        import paq
                        data  = paq.decompress(data)
                        
                        lenf5=len(data)

                    sda=bin(int(binascii.hexlify(data),16))[2:]
                    lenf=len(sda)

                    lenf1=len(data)
                
                    xc=(lenf1*8)-lenf
                    z=0
                    if xc!=0:
                        while z<xc:
                            sda="0"+sda
                            z=z+1

                    

                    sda2=sda

                    lenf3=len(sda2)
                lenf2=len(sda2)  
				
                e4=sda2[e2:e3]
                
                if e4=="1":
                    sda3=sda3+"0"
                if e4=="0":
                    sda3=sda3+"1"

                e2=e2+1
                e3=e3+1

                e4=""
          
                if e3==cvf:
                    e2=0
                    e3=1
                    
                    cvf=cvf+1

                    cvf=sw
                    sw=sw+1
             
                if cvf==lenf5*8+4:
                    sw=2
                    cvf=c
                    cvf1=cvf1+1
                     
                    c=c+2

                if cvf1==20:
                    
                    sda2=sda3
                    sda3=""
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2

                    elw=elw+1
                    
                    
                if elw==2:
                    
                    
                    
                     
          
                    

        
                    n = int(sda2, 2)
                
                    qqwslenf=len(sda2)
                    qqwslenf=(qqwslenf/8)*2
                    qqwslenf=str(qqwslenf)
                    qqwslenf="%0"+qqwslenf+"x"
             
                    jl=binascii.unhexlify(qqwslenf % n)
                    sssssw=len(jl)
                    data=jl
                    qqqwz=qqqwz+1
                    szxzzza=""
                    szxzs=""
             
                   

                    assx=10
                    if assx==10:
                        f2.write(jl)
                       
if namez=="cl":
    name = input("What is name of file? ")
    namea="file.WhiteHall"
    namem=""
    namema="?"
   
    blockw=5
    blockw1=4
    nameas=name+".bin"
    countraz=0
    cvf=2
    cvf1=0
    s=""
    e2=0
    e3=2
    e4=""
    c=2
    sw=2
    elw=0
   
    sda3=""

    sscvf=0
    
    qqqqwzl=0
   
    with open(nameas, "w") as f4:
            f4.write(s)
    with open(nameas, "a") as f3:
            f3.write(s)
    with open(name, "rb") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        s=str(data)
        lenf1=len(data)
        lenf5=len(data)
        if lenf1<6:
            print("This file is too small");
            raise SystemExit
        if lenf1>(2**32)-1:
            print("This file is too big");
            raise SystemExit
        
        assx=0
        
        qqqwz=0
        while assx<10:
      
            aas1=0
            a1=0
            
            cvf=cvf+1
            
            countraz=countraz+1

            with open(nameas, "ab") as f2:
                if countraz==1:
                    sda=bin(int(binascii.hexlify(data),16))[2:]
                    lenf=len(sda)
                    
                    lenf1=len(data) 
                    xc=(lenf1*8)-lenf
                    z=0
                    if xc!=0:
                        while z<xc:
                            sda="0"+sda
                            z=z+1
                    sda2=sda
                    lenf3=len(sda2)
                lenf2=len(sda2)  
				
                e4=sda2[e2:e3]
                
                if e4=="1":
                    sda3=sda3+"0"
                if e4=="0":
                    sda3=sda3+"1"

                e2=e2+1
                e3=e3+1

                e4=""
          
                if e3==cvf:
                    e2=0
                    e3=1
                    
                    cvf=cvf+1
                    
                    cvf=sw
                    sw=sw+1
             
                if cvf==lenf5*8+4:
                    sw=2
                    cvf=c
                    cvf1=cvf1+1
                    sda2=sda3
                    
                    c=c+2
                    
                if cvf1==20:
                    
                    sda2=sda3
                    sda3=""
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2

                    elw=elw+1
                    
                    
                if elw==2:
                    

        
                    n = int(sda2, 2)
                
                    qqwslenf=len(sda2)
                    qqwslenf=(qqwslenf/8)*2
                    qqwslenf=str(qqwslenf)
                    qqwslenf="%0"+qqwslenf+"x"
             
                    jl=binascii.unhexlify(qqwslenf % n)
                    sssssw=len(jl)
                    data=jl
                    qqqwz=qqqwz+1
                    szxzzza=""
                    szxzs=""
             
                    import paq
                    
                    jl = paq.compress(jl)

                    sssssw=len(jl)
                    
                    jl = jl[3:]

                    assx=10
                    if assx==10:
                        f2.write(jl)
                       
                
                        

                        
          
                   
