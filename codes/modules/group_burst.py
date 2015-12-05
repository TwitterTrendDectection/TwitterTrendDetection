import pickle

def group_burst(pickle_file,generate_file):
    with open(pickle_file, 'r') as f:
        t = pickle.loads(f.read())
    f.close()
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

    # with open(generate_file,'w')as f:
    #     for x in result:
    #         f.write(str(x[0]) + " " + str(x[1]) + '\n')
    #
    # f.close()
    pickle.dump(result, open(generate_file, 'wb'))


if __name__ == "__main__":
    group_burst()