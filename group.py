import pickle

with open('word_to_set.pkl', 'r') as f:
    t = pickle.loads(f.read())

groups = []
lists = []

for key, value in t.iteritems():
    s = set()
    s.add(key)
    groups.append(s)
    lists.append(value)

thresh = 5
for i in xrange(len(t)):
    #print i
    for j in xrange(i):
        #print j
        gi = groups[i]
        gj = groups[j]
        si = lists[i]
        sj = lists[j]
        if len(si.intersection(sj)) >= thresh:
            groups[i] = gi.union(gj)
            lists[i] = si.intersection(sj)
            groups[j] = set()
            lists[j] = set()

pairs = []
for x in xrange(len(groups)):
    pairs.append((groups[x], lists[x]))


pairs.sort(key = lambda x: len(x[0]), reverse = True)

count = 0
for x in pairs:
    if len(x[0]) == 0:
        count += 1

result = pairs[:len(groups)-count]

with open('groupburst.txt','w')as f:
    for x in result:
        f.write(str(x[0]))
        f.write(str(x[1]))
        f.write('\n')
