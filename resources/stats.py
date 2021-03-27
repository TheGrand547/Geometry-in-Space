from math import sqrt
from main import getDifficulty
from seedMethods import intSeed
standard = 0
mean = 0
alls = []
alphas = 'abcdefghijklmnopqrstuvwxyz'

f = 'g'
s = 'a'
ssd = 'e'
for ff in alphas:
    for gg in alphas:
        for ee in alphas:
            for ii in alphas:
                    seed = ff + 'e' + gg + ii + ee
                    dif = getDifficulty(seed)
                    alls.append([dif, seed])

print 'Stat Calcuations are Starting'
tots = 0.0
for i in alls:
    tots += i[0]
alls.sort()
print 'The average is ' + str(tots / len(alls))
print 'The middle is ' + str(alls[len(alls) / 2][0])
# print 'The most common is ',
ts = 0
top = 0
maxd = 0
'''
for i in pts:
    if i[1] > top:
        top = i[1]
        maxd = ts
    ts += 1
print pts[maxd][0]
'''

# standard deviation
t2 = 0
low = 30
# to find the hardest seed
kk = 0
ts2 = 0
gg = 0
ts3 = 0
for i in alls:
    t2 += float(float(tots) / len(alls)) - float(i[0])
    if i[0] > top:
        top = i[0]
        ts2 = kk
    if i[0] < low:
        low = i[0]
        ts3 = kk
    kk += 1
t2 /= float(len(alls))
t2 = float(sqrt(abs(float(t2))))
# '''
print 'With a standard deviation of ' + str(t2)
print 'The largest float was ' + str(top) + ', which comes from the seed of ' + str(alls[ts2][1])
print 'The lowest float was ' + str(low) + ', which came from the seed ' + str(alls[ts3][1])
# '''
# find the 10 hardest
tops = []
lows = []
alls.sort(key=lambda seed: seed[0])


for i in range(1, 10):
    lows.append(alls[i])
    tops.append(alls[-i])
stat = open('Hardest and Easiest Seeds.text', 'w')
stat.write("Highest Difficulty Seeds\n")
for i in tops:
    st2 = str(i[1]) + ' with a float of ' + str(i[0] / top) + '\n'
    stat.write(st2)
    print st2
stat.write("Lowest Difficulty Seeds\n")
for i in lows:
    st2 = str(i[1]) + ' with a float of ' + str(i[0] / top) + '\n'
    stat.write(st2)
    print st2
stat.close()

