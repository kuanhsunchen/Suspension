import matplotlib
matplotlib.use('Agg')
import matplotlib.patches as mpatches
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats.mstats import gmean
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
x6 = []
y6 = []
x7 = []
y7 = []
x8 = []
y8 = []
x9 = []
y9 = []
x10 = []
y10 = []
x11 = []
y11 = []
x12 = []
y12 = []
x13 = []
y13 = []
x14 = []
y14 = []
x15 = []
y15 = []
x16 = []
y16 = []
x17 = []
y17 = []
resTotal1 = []
resTotal2 = []
resTotal3 = []
resTotal4 = []
resTotal5 = []
resTotal6 = []
resTotal7 = []
resTotal8 = []
resTotal9 = []
resTotal10 = []
resTotal11 = []
resTotal12 = []
resTotal13 = []
resTotal14 = []
resTotal15 = []
resTotal16 = []
resTotal17 = []
def init():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17
    global y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17
    global resTotal1, resTotal2, resTotal3, resTotal4, resTotal5, resTotal6, resTotal7, resTotal8, resTotal9, resTotal10, resTotal11, resTotal12, resTotal13, resTotal14, resTotal15, resTotal16, resTotal17
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []
    x5 = []
    y5 = []
    x6 = []
    y6 = []
    x7 = []
    y7 = []
    x8 = []
    y8 = []
    x9 = []
    y9 = []
    x10 = []
    y10 = []
    x11 = []
    y11 = []
    x12 = []
    y12 = []
    x13 = []
    y13 = []
    x14 = []
    y14 = []
    x15 = []
    y15 = []
    x16 = []
    y16 = []
    x17 = []
    y17 = []
    resTotal1 = []
    resTotal2 = []
    resTotal3 = []
    resTotal4 = []
    resTotal5 = []
    resTotal6 = []
    resTotal7 = []
    resTotal8 = []
    resTotal9 = []
    resTotal10 = []
    resTotal11 = []
    resTotal12 = []
    resTotal13 = []
    resTotal14 = []
    resTotal15 = []
    resTotal16 = []
    resTotal17 = []

'''
f2 = open(var1+"'1'.txt", 'r')
f3 = open(var1+"'2'.txt", 'r')
f4 = open(var1+"'3'.txt", 'r')
f5 = open(var1+"'4'.txt", 'r')
f6 = open(var1+"'5'.txt", 'r')
'''

def fileInput(var1, group):
    fileidx = 0
    utililist = []
    while fileidx < group:
        tmpUtil = []
        f1 = open(var1+str(fileidx)+".txt", 'r')
        count = -1
        flag = 0
        tmpRes1 = []
        tmpRes2 = []
        tmpRes3 = []
        tmpRes4 = []
        tmpRes5 = []
        tmpRes6 = []
        tmpRes7 = []
        tmpRes8 = []
        tmpRes9 = []
        tmpRes10 = []
        tmpRes11 = []
        tmpRes12 = []
        tmpRes13 = []
        tmpRes14 = []
        tmpRes15 = []
        tmpRes16 = []
        tmpRes17 = []

        for line in f1:
            if count == -1:
                #filename to get utilization:
                filename = line.split('_')
                print filename
                tmpUtil.append(int(filename[1]))

            #Content to get Arithmetic mean and Gmean
            if 0 <count < 200:
                if count%2==1:
                    strline = line.replace('[','')
                    strline = strline.replace(']','')
                    strline = strline.replace('\n','')
                    strline = strline.split(',')
                    #strline[x] x = 0-16
                    #[ILPcarry, ILPblock, ILPjit, Inflation, ILPbaseline, Combo, TDA, TDAcarry, TDAblock, TDAjit, TDAjitblock, TDAmix, CTbaseline, CTcarry, CTblock, CTjit, CTmix]
                    #ILPcarry
                    tmpRes1.append(int(strline[0]))
                    #ILPblock
                    tmpRes2.append(int(strline[1]))
                    #ILPjit
                    tmpRes3.append(int(strline[2]))
                    #Inflation
                    tmpRes4.append(int(strline[3]))
                    #ILPbaseline
                    tmpRes5.append(int(strline[4]))
                    #Combo
                    tmpRes6.append(int(strline[5]))
                    #TDAbaseline
                    tmpRes7.append(int(strline[6]))
                    #TDAcarry
                    tmpRes8.append(int(strline[7]))
                    #TDAblock
                    tmpRes9.append(int(strline[8]))
                    #TDAjit
                    tmpRes10.append(int(strline[9]))
                    #TDAjitblock
                    tmpRes11.append(int(strline[10]))
                    #TDAmix
                    tmpRes12.append(int(strline[11]))
                    #CTbaseline
                    tmpRes13.append(int(strline[12]))
                    #CTbarry
                    tmpRes14.append(int(strline[13]))
                    #CTblock
                    tmpRes15.append(int(strline[14]))
                    #CTjit
                    tmpRes16.append(int(strline[15]))
                    #CTmix
                    tmpRes17.append(int(strline[16]))

            if count == 201:
                '''
                #print 'Gmean:'+line
                strline = line.replace('[','')
                strline = strline.replace(']','')
                strline = strline.replace('\n','')
                strline = strline.split(',')
                print strline
                #strline[x] x = 0-16
                y1.append(float(strline[0]))
                '''
                count = -1
                continue
            count += 1
        f1.close()
        resTotal1.append(tmpRes1)
        resTotal2.append(tmpRes2)
        resTotal3.append(tmpRes3)
        resTotal4.append(tmpRes4)
        resTotal5.append(tmpRes5)
        resTotal6.append(tmpRes6)
        resTotal7.append(tmpRes7)
        resTotal8.append(tmpRes8)
        resTotal9.append(tmpRes9)
        resTotal10.append(tmpRes10)
        resTotal11.append(tmpRes11)
        resTotal12.append(tmpRes12)
        resTotal13.append(tmpRes13)
        resTotal14.append(tmpRes14)
        resTotal15.append(tmpRes15)
        resTotal16.append(tmpRes16)
        resTotal17.append(tmpRes17)

        utililist.append(tmpUtil)
        fileidx += 1
    return utililist
    #print resTotal6

def getResPerUtili(res, numinSets, num): #work for tasks 10 an 20
    utililist = []
    if num == 40:
        readyres = [[] for i in range(6)]
    elif num == 30:
        readyres = [[] for i in range(7)]
    else:
        readyres = [[] for i in range(8)]
    count = 0
    for ind, i in enumerate(res): #each file
        #print ""
        #print i
        #print len(i)
        tmp = []
        icount = 0
        for j in i: #every numinSets input for each utilization
            tmp.append(j)
            count+=1
            #print icount
            if count > numinSets-1:
                readyres[icount]=readyres[icount]+tmp
                tmp = []
                count = 0
                if num == 40:
                    icount = (icount+1)%6
                elif num == 30:
                    icount = (icount+1)%7
                else:
                    icount = (icount+1)%8
        icount = 0
        count = 0

    for i in readyres:
        utililist.append(i)
    return utililist

#wayofMean(np.mean, 10, 'Amean', 'S', 100, 0)
def wayofMean(way, num, atitle, typ, s, MST):
    init()
    typ.replace("'", '')
    if MST == 1:
        target = 'outputM_completed/Results-tasks'+repr(num)+'_stype'+typ+'_'
    else:
        target = 'output_completed/Results-tasks'+repr(num)+'_stype'+typ+'_'
    utili = fileInput(target, g)
    for i in utili[0]:
        x1.append(i)
        x2.append(i)
        x3.append(i)
        x4.append(i)
        x5.append(i)
        x6.append(i)
        x7.append(i)
        x8.append(i)
        x9.append(i)
        x10.append(i)
        x11.append(i)
        x12.append(i)
        x13.append(i)
        x14.append(i)
        x15.append(i)
        x16.append(i)
        x17.append(i)
    if MST == 0:
        fileName = atitle+'Results-tasks'+repr(num)+'_stype_'+repr(typ)
    else:
        fileName = 'M'+atitle+'Results-tasks'+repr(num)+'_stype_'+repr(typ)
    print fileName
    for i in getResPerUtili(resTotal1,s, num): #when g = 6
        y1.append(way(i))
    for i in getResPerUtili(resTotal2,s, num): #when g = 6
        y2.append(way(i))
    for i in getResPerUtili(resTotal3,s, num): #when g = 6
        y3.append(way(i))
    for i in getResPerUtili(resTotal4,s, num): #when g = 6
        y4.append(way(i))
    for i in getResPerUtili(resTotal5,s, num): #when g = 6
        y5.append(way(i))
    for i in getResPerUtili(resTotal6,s, num): #when g = 6
        y6.append(way(i))
    for i in getResPerUtili(resTotal7,s, num): #when g = 6
        y7.append(way(i))
    for i in getResPerUtili(resTotal8,s, num): #when g = 6
        y8.append(way(i))
    for i in getResPerUtili(resTotal9,s, num): #when g = 6
        y9.append(way(i))
    for i in getResPerUtili(resTotal10,s, num): #when g = 6
        y10.append(way(i))
    for i in getResPerUtili(resTotal11,s, num): #when g = 6
        y11.append(way(i))
    for i in getResPerUtili(resTotal12,s, num): #when g = 6
        y12.append(way(i))
    for i in getResPerUtili(resTotal13,s, num): #when g = 6
        y13.append(way(i))
    for i in getResPerUtili(resTotal14,s, num): #when g = 6
        y14.append(way(i))
    for i in getResPerUtili(resTotal15,s, num): #when g = 6
        y15.append(way(i))
    for i in getResPerUtili(resTotal16,s, num): #when g = 6
        y16.append(way(i))
    for i in getResPerUtili(resTotal17,s, num): #when g = 6
        y17.append(way(i))
    # plot in pdf
    pp = PdfPages(folder + fileName + '.pdf')
    title = atitle+'-'+repr(num)+'Tasks-'+repr(typ)
    plt.title(title, fontsize=20)
    plt.grid(True)
    #plt.ylabel('Geometric Mean', fontsize=20)
    #plt.xlabel('Approaches($U^*$)', fontsize=20)
    ax = plt.subplot()
    ax.tick_params(axis='both', which='major',labelsize=16)
    if atitle == 'Amean':
        ax.set_ylabel("Arithmetic Mean", size=20)
    else:
        ax.set_ylabel("Geometric Mean", size=20)
    ax.set_xlabel("Utilization (%)", size=20)

    marker = itertools.cycle(('D', 'd', 'o', 's', 'v'))
    print x5, y5
    try:
        #ax.plot( x1, y1, '-', marker = marker.next(), label='ILPcarry', linewidth=2.0)
        #ax.plot( x2, y2, '-', marker = marker.next(), label='ILPblock', linewidth=2.0)
        #ax.plot( x3, y3, '-', marker = marker.next(), label='ILPjit', linewidth=2.0)
        #ax.plot( x4, y4, '-', marker = marker.next(), label='Inflaction', linewidth=2.0)
        #ax.plot( x5, y5, '-', marker = marker.next(), label='ILPbaseline', linewidth=2.0)
        #ax.plot( x6, y6, '-', marker = marker.next(), label='ILPcombo', linewidth=2.0)
        ax.plot( x7, y7, '-', marker = marker.next(), label='TDAbaseline', linewidth=2.0)
        #ax.plot( x8, y8, '-', marker = marker.next(), label='TDAcarry', linewidth=2.0)
        #ax.plot( x9, y9, '-', marker = marker.next(), label='TDAblock', linewidth=2.0)
        #ax.plot( x10, y10, '-', marker = marker.next(), label='TDAjit', linewidth=2.0)
        #ax.plot( x11, y11, '-', marker = marker.next(), label='TDAjitblock', linewidth=2.0)
        ax.plot( x12, y12, '-', marker = marker.next(), label='TDAmix', linewidth=2.0)
        ax.plot( x13, y13, '-', marker = marker.next(), label='CTbaseline', linewidth=2.0)
        #ax.plot( x14, y14, '-', marker = marker.next(), label='CTcarry', linewidth=2.0)
        #ax.plot( x15, y15, '-', marker = marker.next(), label='CTblock', linewidth=2.0)
        #ax.plot( x16, y16, '-', marker = marker.next(), label='CTjit', linewidth=2.0)
        ax.plot( x17, y17, '-', marker = marker.next(), label='CTmix', linewidth=2.0)

    except ValueError:
        print "ValueError"

    #ax.vlines(0.5, 0, 1, transform=ax.transAxes )
    #ax.text(0.35, 0.04, "$U^*=60\%$", transform=ax.transAxes, size=16 )
    #ax.text(0.85, 0.04, "$U^*=70\%$", transform=ax.transAxes, size=16 )

    ax.legend(loc=0)
    figure = plt.gcf()
    figure.set_size_inches([10, 6])

    pp.savefig()
    plt.clf()
    plt.show()
    pp.close()


folder = 'plots/'
g = 1
#after this, 6 sets of methods are prepared
wayofMean(np.mean, 10, 'Amean', 'S', 100, 0)
wayofMean(gmean, 10, 'Gmean', 'S', 100, 0)
wayofMean(np.mean, 10, 'Amean', 'M', 100, 0)
wayofMean(gmean, 10, 'Gmean', 'M', 100, 0)
wayofMean(np.mean, 10, 'Amean', 'L', 100, 0)
wayofMean(gmean, 10, 'Gmean', 'L', 100, 0)
wayofMean(np.mean, 20, 'Amean', 'S', 100, 0)
wayofMean(gmean, 20, 'Gmean', 'S', 100, 0)
wayofMean(np.mean, 20, 'Amean', 'M', 100, 0)
wayofMean(gmean, 20, 'Gmean', 'M', 100, 0)
wayofMean(np.mean, 20, 'Amean', 'L', 100, 0)
wayofMean(gmean, 20, 'Gmean', 'L', 100, 0)
wayofMean(np.mean, 30, 'Amean', 'S', 100, 0)
wayofMean(gmean, 30, 'Gmean', 'S', 100, 0)
wayofMean(np.mean, 30, 'Amean', 'M', 100, 0)
wayofMean(gmean, 30, 'Gmean', 'M', 100, 0)
wayofMean(np.mean, 30, 'Amean', 'L', 100, 0)
wayofMean(gmean, 30, 'Gmean', 'L', 100, 0)
wayofMean(np.mean, 40, 'Amean', 'S', 100, 0)
wayofMean(gmean, 40, 'Gmean', 'S', 100, 0)
wayofMean(np.mean, 40, 'Amean', 'M', 100, 0)
wayofMean(gmean, 40, 'Gmean', 'M', 100, 0)
wayofMean(np.mean, 40, 'Amean', 'L', 100, 0)
wayofMean(gmean, 40, 'Gmean', 'L', 100, 0)

wayofMean(np.mean, 10, 'Amean', 'S', 100, 1)
wayofMean(gmean, 10, 'Gmean', 'S', 100, 1)
wayofMean(np.mean, 10, 'Amean', 'M', 100, 1)
wayofMean(gmean, 10, 'Gmean', 'M', 100, 1)
wayofMean(np.mean, 10, 'Amean', 'L', 100, 1)
wayofMean(gmean, 10, 'Gmean', 'L', 100, 1)
wayofMean(np.mean, 20, 'Amean', 'S', 100, 1)
wayofMean(gmean, 20, 'Gmean', 'S', 100, 1)
wayofMean(np.mean, 20, 'Amean', 'M', 100, 1)
wayofMean(gmean, 20, 'Gmean', 'M', 100, 1)
wayofMean(np.mean, 20, 'Amean', 'L', 100, 1)
wayofMean(gmean, 20, 'Gmean', 'L', 100, 1)
wayofMean(np.mean, 30, 'Amean', 'S', 100, 1)
wayofMean(gmean, 30, 'Gmean', 'S', 100, 1)
wayofMean(np.mean, 30, 'Amean', 'M', 100, 1)
wayofMean(gmean, 30, 'Gmean', 'M', 100, 1)
wayofMean(np.mean, 30, 'Amean', 'L', 100, 1)
wayofMean(gmean, 30, 'Gmean', 'L', 100, 1)
wayofMean(np.mean, 40, 'Amean', 'S', 100, 1)
wayofMean(gmean, 40, 'Gmean', 'S', 100, 1)
wayofMean(np.mean, 40, 'Amean', 'M', 100, 1)
wayofMean(gmean, 40, 'Gmean', 'M', 100, 1)
wayofMean(np.mean, 40, 'Amean', 'L', 100, 1)
wayofMean(gmean, 40, 'Gmean', 'L', 100, 1)