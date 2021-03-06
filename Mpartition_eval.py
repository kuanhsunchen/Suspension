from __future__ import division
from collections import OrderedDict
import Mpartition_ILP as multi
import Mcombo_ILP as combo
import MSTPartition as STP
import generator
import sys
import math
import numpy as np
from scipy.stats.mstats import gmean
from miscs import *

def main():
    print "This is Mpartition evaluation"
    args = sys.argv
    if len(args) < 5:
            print "Usage: python partition_eval.py [debug] [# of sets] [generate/load] [stype] [btype]"
            return -1 # no input

    debug = int (args[1])
    if debug == 0 or debug == 2:
        tasksets_amount = int (args[2])
        mode = int(args[3]) # 0 = generate, 1 = directly use the inputs
        stype = args[4] # S, M, L
        btype = args[5] # {1, 2, 3} as {0.2, 0.5, 0.75} * minimum period
        inputfiles_amount = 1 # n for distribution
        tasksets_amount = int(math.ceil(tasksets_amount / inputfiles_amount))

        dist_utilizations = OrderedDict()
        dist_utilizations['10Tasks'] = 10
        dist_utilizations['20Tasks'] = 20
        dist_utilizations['30Tasks'] = 30
        dist_utilizations['40Tasks'] = 40

        idx = 0
        perAmount = [[] for i in range(len(dist_utilizations.items()))]
        for set_name, amount in dist_utilizations.items():
            for uti in range(int(100/10*amount), int(450/10*amount)+1, 5*amount):
                if idx == 2 and uti >= 1350: # 30 tasks
                    continue
                if idx == 3 and uti >= 1600: # 40 tasks
                    continue
                if mode == 0:
                    if stype == 'S':
                        tasksets = [generator.taskGeneration(amount, uti, 'S', 1, btype) for n in range(tasksets_amount)]
                        np.save ('input/'+str(set_name)+'_'+str(uti)+'_S_'+btype, tasksets)

                    elif stype == 'M':
                        tasksets = [generator.taskGeneration(amount, uti, 'M', 1, btype) for n in range(tasksets_amount)]
                        np.save ('input/'+str(set_name)+'_'+str(uti)+'_M_'+btype, tasksets)

                    elif stype == 'L':
                        tasksets = [generator.taskGeneration(amount, uti, 'L', 1, btype) for n in range(tasksets_amount)]
                        np.save ('input/'+str(set_name)+'_'+str(uti)+'_L_'+btype, tasksets)
                else:
                    pass
                    #TODO check if the inputs are there.
                perAmount[idx].append('input/'+str(set_name)+'_'+str(uti)+'_'+stype+'_'+btype+'.npy')
            idx+=1
        print perAmount

        if mode == 1:
            gRes=[[] for i in range(17)] # 17 methods
            for idx, filenames  in enumerate(perAmount):
                fileEx = 'Exceptions-tasks'+repr((1+idx)*10)+'_stype'+stype+'_btype'+btype
                fileB = 'Results-tasks'+repr((1+idx)*10)+'_stype'+stype+'_btype'+btype
                #fileEx = 'Exceptions-tasks'+repr((1+idx)*20)+'_stype'+repr(stype)+'_group'+repr(group)
                #fileB = 'Results-tasks'+repr((1+idx)*20)+'_stype'+repr(stype)+'_group'+repr(group)

                #fileEx = 'Exceptions-tasks'+repr((1+idx)*30)+'_stype'+repr(stype)+'_group'+repr(group)
                #fileB = 'Results-tasks'+repr((1+idx)*30)+'_stype'+repr(stype)+'_group'+repr(group)
                file_Ex = open('outputM/'+fileEx + '.txt', "w")
                file_B = open('outputM/'+fileB + '.txt', "w")
                for filename in filenames:
                    file_B.write(filename+'\n')
                    file_Ex.write(filename+'\n')
                    tasksets = np.load(filename)
                    for taskset in tasksets:
                        if idx == 2 or idx == 3:
                            res = test(taskset, debug, 1, btype)
                        else:
                            res = test(taskset, debug, 0, btype)
                        file_B.write('[ILPcarry, ILPblock, ILPjit, Inflation, ILPbaseline, Combo, TDA, TDAcarry, TDAblock, TDAjit, TDAjitblock, TDAmix, CTbaseline, CTcarry, CTblock, CTjit, CTmix]\n')
                        file_B.write(str(res)+'\n')
                        for ind, j in enumerate(res):
                            if j == -1:
                                #file_B.write('Infeasible in ILP \n')
                                file_Ex.write('Infeasible in ILP \n')
                                file_Ex.write(str(taskset)+'\n')
                                file_Ex.write(str(res)+'\n')
                                gRes[ind].append(len(taskset))
                            elif j == -2:
                                #file_B.write('ILP pops out an uncatched status \n')
                                file_Ex.write('ILP pops out an uncatched status \n')
                                file_Ex.write(str(taskset)+'\n')
                                file_Ex.write(str(res)+'\n')
                                gRes[ind].append(len(taskset))
                            elif j == -3:
                                #file_B.write('Infeasible in the double checking \n')
                                file_Ex.write('Infeasible in the double checking \n')
                                file_Ex.write(str(taskset)+'\n')
                                file_Ex.write(str(res)+'\n')
                                gRes[ind].append(len(taskset))
                            else:
                                gRes[ind].append(j)
                    # Way of present
                    result = []
                    for i in gRes:
                        result.append(gmean(i))
                    file_B.write('Gmean: \n')
                    file_B.write(str(result)+'\n')
                file_B.close()
                file_Ex.close()
        '''
        if mode == 2:
            gRes=[[] for i in range(17)] # 17 methods
            for idx, filenames  in enumerate(perAmount):
                if idx == 2: #print for 30 tasks
                    fileA = 'DEtasks'+repr((1+idx)*10)+'_stype'+repr(stype)
                    file = open('outputM/'+fileA + '.txt', "w")
                    for filename in filenames:
                        file.write(filename+'\n')
                        tasksets = np.load(filename)
                        for taskset in tasksets:
                            file.write(str(taskset)+'\n')
                            sumUt = 0.0
                            sumUs = 0.0
                            for i in taskset:
                                sumUt += utili(i)
                                sumUs += utiliAddE(i)
                            file.write('total utili:'+str(sumUt)+'\n')
                            file.write('total utili+exclusive:'+str(sumUs)+'\n')
                        file.write('\n')
                    file.close()
        '''
    else:
        # DEBUG
        # generate some taskset, third argument is for sstype setting as PASS {S, M, L}
        taskset = generator.taskGeneration(10, 300, 'S', 1, 1)
        print test(taskset, debug, btype)

def test(taskset, debug, flag, btype):
    # taskset, num of procs
    obj = []
    if debug == 2:
        #print "SPECIAL CHEKCING MODE:"
        # ILP Tests
        #obj.append(multi.partition(taskset, 'carryin'))
        #obj.append(multi.partition(taskset, 'blocking'))
        #obj.append(multi.partition(taskset, 'k2q'))
        obj.append(-5)
        obj.append(-5)
        obj.append(-5)
        obj.append(multi.partition(taskset, 'inflation'))
        #obj.append(multi.partition(taskset, 'ilpbaseline'))
        obj.append(-5)
        obj.append(combo.partition(taskset))

        binpack = 'first'
        # Heuristic + TDA Tests
        objMap = STP.STPartition(taskset, 'tda', binpack)
        obj.append(objMap[0])
        #objMap = STP.STPartition(taskset, 'carry', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        #objMap = STP.STPartition(taskset, 'block', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        #objMap = STP.STPartition(taskset, 'jit', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        #objMap = STP.STPartition(taskset, 'jitblock', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        objMap = STP.STPartition(taskset, 'tdamix', binpack)
        obj.append(objMap[0])

        # Heuristic + Constant Time Tests
        objMap = STP.STPartition(taskset, 'CTbaseline', binpack)
        obj.append(objMap[0])
        #objMap = STP.STPartition(taskset, 'CTcarry', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        #objMap = STP.STPartition(taskset, 'CTblock', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        #objMap = STP.STPartition(taskset, 'CTjit', binpack)
        #obj.append(objMap[0])
        obj.append(-5)
        objMap = STP.STPartition(taskset, 'CTmix', binpack)
        obj.append(objMap[0])

    elif debug == 1:
        print "DEBUG MODE:"
        # ILP Tests
        #obj.append(multi.partition(taskset, 'carryin'))
        #obj.append(multi.partition(taskset, 'blocking'))
        #obj.append(multi.partition(taskset, 'k2q'))
        obj.append(len(taskset))
        obj.append(len(taskset))
        obj.append(len(taskset))
        obj.append(multi.partition(taskset, 'inflation'))
        #obj.append(multi.partition(taskset, 'ilpbaseline'))
        obj.append(len(taskset))
        obj.append(combo.partition(taskset))
        binpack = 'first'
        # Heuristic + TDA Tests
        objMap = STP.STPartition(taskset, 'tda', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'carry', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'block', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'jit', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'jitblock', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'tdamix', binpack)
        obj.append(objMap[0])

        # Heuristic + Constant Time Tests
        objMap = STP.STPartition(taskset, 'CTbaseline', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTcarry', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTblock', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTjit', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTmix', binpack)
        obj.append(objMap[0])

    else:
        # ILP Tests
        if flag == 0:
            obj.append(multi.partition(taskset, 'carryin'))
            if btype != 'N':
                obj.append(len(taskset))
            else:
                obj.append(multi.partition(taskset, 'blocking'))
            obj.append(multi.partition(taskset, 'k2q'))
            obj.append(multi.partition(taskset, 'inflation'))
            obj.append(multi.partition(taskset, 'ilpbaseline'))
            # TODO remove Eq21.
            obj.append(combo.partition(taskset, btype))
        else:
            obj.append(len(taskset))
            obj.append(len(taskset))
            obj.append(len(taskset))
            obj.append(len(taskset))
            obj.append(len(taskset))
            obj.append(len(taskset))
        binpack = 'first'
        # Heuristic + TDA Tests
        objMap = STP.STPartition(taskset, 'tda', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'carry', binpack)
        obj.append(objMap[0])
        if btype != 'N':
            obj.append(len(taskset))
        else:
            objMap = STP.STPartition(taskset, 'block', binpack)
            obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'jit', binpack)
        obj.append(objMap[0])
        if btype != 'N':
            obj.append(len(taskset))
        else:
            objMap = STP.STPartition(taskset, 'jitblock', binpack)
            obj.append(objMap[0])

        objMap = STP.STPartition(taskset, 'tdamix', binpack)
        obj.append(objMap[0])

        # Heuristic + Constant Time Tests
        objMap = STP.STPartition(taskset, 'CTbaseline', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTcarry', binpack)
        obj.append(objMap[0])
        if btype != 'N':
            obj.append(len(taskset))
        else:
            objMap = STP.STPartition(taskset, 'CTblock', binpack)
            obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTjit', binpack)
        obj.append(objMap[0])
        objMap = STP.STPartition(taskset, 'CTmix', binpack)
        obj.append(objMap[0])

    # Show the results

    #print ''
    #print '[ILPcarry, ILPblock, ILPjit, Inflation, Combo, TDAcarry, TDAblock, TDAjit, TDAjitblock, TDAmix, CTcarry, CTblock, CTjit, CTmix]'
    #print obj
    return obj
if __name__ == "__main__":
    main()
