epsilon1=1
epsilon2=epsilon1*0.5
epsilon3=epsilon2+1
while epsilon3>1:
    epsilon1=epsilon2
    epsilon2=epsilon1*0.5
    epsilon3=epsilon2+1
print(epsilon1)
