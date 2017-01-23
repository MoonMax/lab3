from friends_age import FriendsAge
from id_from_username import IDFromUsername
import matplotlib.pyplot as plt


input = 'skripkaa73'    #input()
getID = IDFromUsername(input)
ID = getID.execute()

getAges = FriendsAge(ID)
ages = getAges.execute()

max_age = max(ages)

osY = [0] * (max_age + 1)


for age in ages:
    osY[age] += 1

osX = range(max_age + 1)

plt.axis([0, max_age, 0, max(osY)])



plt.xlabel('Age')
plt.ylabel('Friends')

plt.plot(osX, osY)

plt.show()