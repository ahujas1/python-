import numpy as np
import matplotlib.pyplot as plt
rewardA=[]
rewardB=[]

a=2
b=1

stratA=[int(x) for x in np.random.rand(80)*2+1]
stratB=[int(x) for x in np.random.rand(80)*2+1]

### SE GANHA
np.array(stratA)-np.array(stratB)

## PAYOFF MATRIX
for i in range(0,len(stratA)):
    if stratA[i]==1 & stratB[i]==1:
        rewardA.append(0)
        rewardB.append(0)
        if stratA[i]==2 & stratB[i]==2:
            rewardA.append(1)
            rewardB.append(1)
        elif stratA[i]==2 & stratB[i]==1:
                rewardA.append(3)
                rewardB.append(-1)
    else:
        rewardA.append(-1)
        rewardB.append(3)
np.array(rewardA)
np.array(rewardB)


totalA=[]
totalB=[]
for i in range(0,len(rewardA)):
    totalA.append(sum(rewardA[0:i]))
    totalB.append(sum(rewardB[0:i]))
np.array(totalB)

plt.figure(figsize=(9,6))
line1,=plt.plot(np.array(totalA),'-',color='r',linewidth=3,label='Random Strategy')
line2,=plt.plot(np.array(totalB),'-',color='b',linewidth=3,label='Always Defeat')
plt.title("REINFORCEMENT LEARNING: Defeat vs Random Strategy")
plt.legend([line1, line2])
plt.show()