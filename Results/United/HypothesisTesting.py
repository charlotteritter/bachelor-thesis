import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def read_excel_file(filename):
    df = pd.read_excel(filename)
    return df

#Chnage input for different tolerance
df = read_excel_file("Omega05_10Iter_a_100Scen_HPC.xls")

StepSizeRules=df['Step Size Rule']
GapLR=df['Gap LR']

alpha=0.05

#Testing a against b
def hypothesis_test(a,b):   #we test if mean of gap of step rule a is smaller or equal than the mean of the gap of step rule b is
    Step1=[]
    Step2=[]
    for i in range(0,len(StepSizeRules)):
        if StepSizeRules[i]==a:
            Step1.append(GapLR[i])
        if StepSizeRules[i]==b:
            Step2.append(GapLR[i])
    mean1=sum(Step1)/len(Step1)
    mean2=sum(Step2)/len(Step2)
    #print(mean1)
    #print(mean2)

    HelpS1=[(Step1[i]-mean1)**2 for i in range(0,len(Step1))]
    HelpS2=[(Step2[i]-mean2)**2 for i in range(0,len(Step2))]
    Var1=(sum(HelpS1))/(len(HelpS1)-1)
    Var2=(sum(HelpS2))/(len(HelpS2)-1)
    #print(Var1)
    #print(Var2)
    sp=((19*Var1+19*Var2)/(38))**(1/2)
    t=(mean1-mean2)/(sp*((1/20+1/20)**(1/2)))
    print(t)
    if (t>1.686):  #alpha Quantil der t-Verteilung mit 38 Freiheitsgraden: 0.05 --> 1.686; 0.1 --> 1.304; 0.25 --> 0.681; 0.5 --> 0
        rejection=True
        print("We reject the nullhypothesis that mean gap of stepsize",a,
              "is smaller or equal than the mean gap of stepsize",b)
    else:
        rejection=False
        print("We are unable to reject the nullhypothesis: Mean gap of stepsize", a,
              "is smaller or equal than the mean gap of stepsize",b)
    return rejection

hypothesis_test(6,5)