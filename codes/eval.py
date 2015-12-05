def micro_eval_each(sysClusters, goldCluster):
    bestF1 = 0
    for sysCluster in sysClusters:
        tp = 0
        fp = 0
        fn = 0
        for item in goldCluster:
            if item in sysCluster:
                tp += 1.0
            else:
                fn += 1.0
        for item in sysCluster:
            if item not in goldCluster:
                fp += 1.0

        if tp == 0:
            continue

        precision = tp / (tp+fp)
        recall = tp / (tp+fn)
        f1 = 2*precision*recall/(precision+recall)

        if f1 > bestF1:
            bestF1 = f1
    return bestF1

def micro_eval(sysClusters, goldClusters):
    sum = 0
    count = len(goldClusters)
    for goldCluster in goldClusters:
        sum += micro_eval_each(sysClusters, goldCluster)
    return sum * 1.0 / count