#cost=[10,12,14,15,16,16,17,18.5,19,19.5]
#tim_min=[5,7,8,9,10,10,11,11.5,12,13]
#num_units=[19,21,22,23,24,24,25,26,27,28]
import math
funct=[]
mod=[]
x=int(input('Enter the number(1.cost,2.time minimum,3.number units)'))
if(x==1):
  funct=[10,12,14,15,16,16,17,18.5,19,19.5]
else:
    if(x==2):
        funct=[5,7,8,9,10,10,11,11.5,12,13]
    else:
        if(x==3):
            funct=[19,21,22,23,24,24,25,26,27,28]
n=str(input('enter 1.sum 2.mean 3.median 4.mode 5.std_error 6.values higher than mean 7.values less than mean'))
mean=(sum(funct)/len(funct))
if n=='1':
    print(sum(funct))
elif n=='2':
    print('mean is %g'%(mean))
elif n=='3':
    f=int(len(funct)/2)
    funct.sort()
    b=((funct[f]+funct[f+1])/2)
    print('median is')
    print(b)      
elif n=='4':
    a=0
    for i in funct:
        print(funct.count(i))
        mod.append(funct.count(i))
    for j in mod:
        if max(mod)!=j:
          a+=1
        else:  
          break
    #print(j)    
    print('mode is %g'%(funct[a]))
elif n=='5':
    s=0
    mean=(sum(funct)/len(funct))
    for i in funct:
        variation=(i-mean)**2
        s=s+variation
    n=s/(len(funct)-1)
    sd=math.sqrt(n)
    se=sd/math.sqrt(len(funct))
    print('standard error is')
    print(se)
else:
  new_mod=[]
  larger=[]
  smaller=[]
  for i in funct:
    if i-mean<0:
      g=-1*(i-mean)
    else:
      g=1*(i-mean)
    new_mod.append(g)
  new_mod.sort()  
  print('standard error greater than mean')
  for i in new_mod:
    if i>mean:
        (str)(larger.append(i))
    else:
        (str)(smaller.append(i))
  print(larger)
  print('standard error less than mean')
  print(smaller)
  
                   
                     
                  
                    
                  
                 
                        
                 
                 
                 
                 
                 
                 
