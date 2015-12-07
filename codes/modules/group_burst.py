import pickle

def group_burst(hotword_to_tweets):
    t = hotword_to_tweets
    groups = []
    lists = []

    for key, value in t.iteritems():
        s = set()
        s.add(key)
        groups.append(s)
        lists.append(value)

    for i in xrange(len(t)):
        #print i
        for j in xrange(i):
            #print j
            gi = groups[i]
            gj = groups[j]
            si = lists[i]
            sj = lists[j]
            threshold = (len(si) + len(sj) + len(gi) + len(gj))/5
            if len(si.intersection(sj)) >= threshold:
                groups[i] = gi.union(gj)
                lists[i] = si.intersection(sj)
                groups[j] = set()
                lists[j] = set()

    pairs = []
    for x in xrange(len(groups)):
        if len(groups[x]) > 3 and len(lists[x])> 1:
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
    # pickle.dump(result, open('./file/' + generate_file, 'wb'))
    return result
