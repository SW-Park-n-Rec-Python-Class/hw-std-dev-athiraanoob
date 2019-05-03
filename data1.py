cost=[10,12,14,15,16,16,17,18.5,19,19.5]
tim_min=[5,7,8,9,10,10,11,11.5,12,13]
num_units=[19,21,22,23,24,24,25,26,27,28]
cost_sum=sum(cost)
tim_min_sum=sum(tim_min)
num_units_sum=sum(num_units)
cost_mean=cost_sum/len(cost)
tim_min_mean=tim_min_sum/len(tim_min)
num_units_mean=num_units_sum/len(num_units)
f=int((len(cost)/2)-1)
cost_median=((cost[f]+cost[f+1])/2)
m=int(len(tim_min)/2)-1
tim_min_median=((tim_min[m]+tim_min[m+1])/2)
v=int(len(num_units)/2)-1
num_units_median=(num_units[v]+num_units[v+1])/2
mode=[]
a=0
for i in cost:
 mode.append(cost.count(i))
for j in mode:
    if max(mode)!=j:
     a+=1
    else:
     break
#print(cost[a])
i=0
j=0
a=0
mode1=[]
for i in tim_min:
    mode1.append(tim_min.count(i))
for j in mode1:
    if max(mode1)!=j:
        a+=1
    else:
      break
#print(tim_min[a])
i=0
j=0
a=0
mode2=[]
for i in num_units:
    mode2.append(num_units.count(i))
for j in mode2:
      if max(mode2)!=j:
                 a+=1
      else:
            break
#print(num_units[a])
se_cost_l=[]
se_tim_min_l=[]
se_num_units_l=[]
se_cost_s=[]
se_tim_min_s=[]
se_num_units_s=[]
i=0
j=0
for i in cost:
 if i>cost_mean:
     se_cost_l.append(i-cost_mean)
 else:
     se_cost_s.append(i-cost_mean)
for j in tim_min:
  if j>tim_min_mean:
      se_tim_min_l.append(j-tim_min_mean)
  else:
      se_tim_min_s.append(j-tim_min_mean)
for z in num_units:
   if z>num_units_mean:
           se_num_units_l.append(z-num_units_mean)
   else:
           se_num_units_s.append(z-num_units_mean)
print('Sum of cost is $%g'%(cost_sum))
print('Mean of cost is $%g'%(cost_mean))
print('Median of cost is $%g'%(cost_median))
print('Mode of cost is',cost[a])
print('Maximum value in cost is $%g'%(max(cost)))
print('Minimum value in cost is $%g'%(min(cost)))
print('Standard error of cost variables from mean:')
print('Values higher than mean:',se_cost_l)
print('Values smaller than mean:',se_cost_s)
print('Sum of time is %gmins'%(tim_min_sum))
print('Mean of time is %g mins'%(tim_min_mean))
print('Median of time is %gmins'%(tim_min_median))
print('Mode of time is %g mins'%(tim_min[a]))
print('Maximum value of cost is %g mins'%(max(tim_min)))
print('Minimum value of cost is %g mins'%(min(tim_min)))
print('Standard error of time variable from mean:')
print('Values higher than mean',se_tim_min_l)
print('Values higher than mean',se_tim_min_s)
print('Sum of units is %g'%(num_units_sum))
print('Mean of units is %g'%(num_units_mean))
print('Median of units is %g'%(num_units_median))
print('Mode of units is %g'%(num_units[a]))
print('Maximum value of units is %g'%(max(num_units)))
print('Minimum value of units is %g'%(min(num_units)))
print('Standard error of unit variable from mean:')
print('Values higher than mean:',se_num_units_l)
print('Values smaller than mean:',se_num_units_s)


           

     
     
                 
                 
    



