import matplotlib.pyplot as plt
import numpy as np
from utils import decorate, savefig
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from Config import *

from scipy.signal import correlate2d
#use Cell2D class from Cell2D.py and also draw_array function
from Cell2D import Cell2D, draw_array

from time import sleep
from IPython.display import clear_output

from utils import underride

import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

from PIL import Image
import numpy as np



mat_im = np.zeros([col,row])
prob_im = np.zeros([col,row])


            
palette = sns.color_palette('muted')
colors = 'green', 'red', palette[7],'grey'
cmap = LinearSegmentedColormap.from_list('cmap', colors)

def locs_where(condition):
    """Find cells where a logical array is True.
    
    condition: logical array
    
    returns: list of location tuples that are nonzero and fulfil the condition 
    """
    return list(zip(*np.nonzero(condition)))


global n
global m
global t

class FirePlace(Cell2D):

    def __init__(self,n,m,w,arriveT):
        self.place = np.zeros([n,m])
        self.prob_place = prob_im
        self.countor = np.zeros([n,m])
        self.wind=w
        self.arriveT=arriveT
        self.t=0
        self.Fighter_Loc = []
    def Inital_Fire(self,i,j):
        self.place[i][j]=1
    
    
    def MieHuoArea(self,i,j,R):
        if i+R>m:
            rr = m-i
        else:
            rr=R
        if i-R<0:
            lr = i
        else:
            lr = R
        if j-R<0:
            tr=j
        else:
            tr = R
        if j+R>n:
            br = n-j
        else:
            br = R
        r = np.min([rr,lr,tr,br])
        y= np.arange(0,n)
        x = np.arange(0,m)
        mask = (x[np.newaxis,:]-i)**2 + (y[:,np.newaxis]-j)**2 < r**2

        self.prob_place[mask]=self.prob_place[mask]*0.7
        
        #return lb,le,wb,we

    # def firefighterLoc(self,i,j,R):
    #     lb,le,wb,we=self.Boundary(i,j,R)
        
        
    def step(self):
        a = self.place   
        Burning = (a==1)
        Burning_loc = locs_where(Burning)
        F=Burning_loc
        
        #we now start to considering the wind condition.(points will start burning in next time step)
        for i in range(len(F)):
            
            p = self.prob_place[F[i]]
         
            wind_prob=[np.random.choice(a=[True, False], p=[p,1-p]),#Possibilities of a certain block to start burning
                           np.random.choice(a=[True, False], p=[p*1,1-p*1]),
                           np.random.choice(a=[True, False], p=[0.8,1-0.8]),
                           np.random.choice(a=[True, False], p=[0.12,1-0.12]),
                           np.random.choice(a=[True, False], p=[0.12,1-0.12]),
                           np.random.choice(a=[True, False], p=[0.3,1-0.3]),
                           False,False,False,
                           np.random.choice(a=[True, False], p=[0.12,1-0.12]),
                           np.random.choice(a=[True, False], p=[0.12,1-0.12]),
                           np.random.choice(a=[True, False], p=[0.8,1-0.8]),
                           np.random.choice(a=[True, False], p=[0.8,1-0.8])]

            #state is the current burning point, others are the neighbour of it,i.e rstate will represent the block on the right side    
            if self.wind == 'e': # e represents east wind
                    state,rstate,rrstate,rtstate,rbstate,lstate,llstate,ttstate,bbstate,ltstate,lbstate,tstate,bstate = np.array(wind_prob)
            if self.wind == 'w':
                    state,lstate,llstate,ltstate,lbstate,rstate,rrstate,ttstate,bbstate,rtstate,rbstate,tstate,bstate = np.array(wind_prob)
            if self.wind== 's':
                    state,bstate,bbstate,lbstate,rbstate,tstate,ttstate,llstate,rrstate,rtstate,ltstate,rstate,lstate = np.array(wind_prob)
            if self.wind== 'n':
                    state,tstate,ttstate,ltstate,rtstate,bstate,bbstate,llstate,rrstate,rbstate,lbstate,rstate,lstate = np.array(wind_prob)
            
            if state == True:
                
                self.place[F[i]] = 1

                #We determine the right handside block
                #First we determine whether the wind will influence this block or not. And we make sure this block will inside the boundary of our map
                if  rstate == True and F[i][1]+1 > 0 and F[i][1]+1 < m-1 : 
                    
                    #then we consider this block's flammability, whether the fire will let it burn or not
                    pr = self.prob_place[F[i][0],F[i][1]+1]
                    
                    # After we satisfy every condition, this block will start to burn at the next time step
                    if self.place[F[i][0],F[i][1]+1]!=2 and np.random.choice(a=[True,False],p=[pr,1-pr])==True:
                                self.place[F[i][0],F[i][1]+1]=1
                    #We determine the block at right handside of last block
                    if rrstate == True and F[i][1]+1 > 0 and F[i][1]+2 < m-1 :
                        prr = self.prob_place[F[i][0],F[i][1]+2]
                        if self.place[F[i][0],F[i][1]+2]!=2 and np.random.choice(a=[True,False],p=[prr,1-prr])==True:
                                self.place[F[i][0],F[i][1]+2]=1

                #We follow the same step as above
                if rtstate == True and F[i][0]-1 <n-1 and F[i][1]+1 < m-1 and F[i][1]+1 > 0 and F[i][0]-1>0:
                    prt=self.prob_place[F[i][0]-1,F[i][1]+1]
                    if self.place[F[i][0]-1,F[i][1]+1]!=2  and np.random.choice(a=[True,False],p=[prt,1-prt])==True:
                        self.place[F[i][0]-1,F[i][1]+1]=1
                    
                if rbstate == True and F[i][0]+1 <n-1 and F[i][1]+1 < m-1 and F[i][1]+1 > 0:
                    prb=self.prob_place[F[i][0]+1,F[i][1]+1]
                    if self.place[F[i][0]+1,F[i][1]+1]!=2 and np.random.choice(a=[True,False],p=[prb,1-prb])==True:
                        self.place[F[i][0]+1,F[i][1]+1]=1
                 
                if  lstate == True  and F[i][1]-1 > 0:
                    pl=self.prob_place[F[i][0],F[i][1]-1]
                    if self.place[F[i][0],F[i][1]-1]!=2 and np.random.choice(a=[True,False],p=[pl,1-pl])==True :
                        self.place[F[i][0],F[i][1]-1]=1
               
            
                        if llstate == True and F[i][1]-2 > 0:
                            pll=self.prob_place[F[i][0],F[i][1]-2]
                            
                            if self.place[F[i][0],F[i][1]-2]!=2 and np.random.choice(a=[True,False],p=[pll,1-pll])==True:
                                self.place[F[i][0],F[i][1]-2]=1
                                test = F[i][0]
                   
                if ltstate == True and F[i][0]-1>0 and F[i][1]-1> 0:
                    plT=self.prob_place[F[i][0]-1,F[i][1]-1]
                    if self.place[F[i][0]-1,F[i][1]-1]!=2 and np.random.choice(a=[True,False],p=[plT,1-plT])==True:
                        self.place[F[i][0]-1,F[i][1]-1]=1
                    

                if  lbstate == True and F[i][0]+1 <n-1 and F[i][1]-1< m and F[i][1]-1 >0:
                    plb=self.prob_place[F[i][0]+1,F[i][1]-1]
                    if self.place[F[i][0]+1,F[i][1]-1]!=2 and np.random.choice(a=[True,False],p=[plb,1-plb])==True:
                        self.place[F[i][0]+1,F[i][1]-1]=1
                      
                   
                if tstate == True and F[i][0]-1 <n-1 and F[i][0]-1> 0:
                    pt=self.prob_place[F[i][0]-1,F[i][1]]
                    if self.place[F[i][0]-1,F[i][1]]!=2 and np.random.choice(a=[True,False],p=[pt,1-pt])==True:
                        self.place[F[i][0]-1,F[i][1]]=1
                       
                        if ttstate== True and F[i][0]-2 <n-1 and F[i][0]-2> 0: 
                            ptt=self.prob_place[F[i][0]-2,F[i][1]]
                            if self.place[F[i][0]-2,F[i][1]]!=2 and np.random.choice(a=[True,False],p=[ptt,1-ptt])==True:
                                self.place[F[i][0]-2,F[i][1]]=1
                         
                if bstate == True and F[i][0]+1 >0 and F[i][0]+1 < n-1:
                    pb=self.prob_place[F[i][0]+1,F[i][1]]
                    if self.place[F[i][0]+1,F[i][1]]!=2 and np.random.choice(a=[True,False],p=[pb,1-pb])==True:
                        self.place[F[i][0]+1,F[i][1]]=1
                      

                        if  bbstate== True and F[i][0]+2 >0 and F[i][0]+2 < n-1:
                            pbb=self.place[F[i][0]+2,F[i][1]]
                            if self.place[F[i][0]+2,F[i][1]]!=2 and np.random.choice(a=[True,False],p=[pbb,1-pbb])==True:
                                self.place[F[i][0]+2,F[i][1]]=1
                                
        for i in range(len(F)):#We consider the Burning duration here

            if self.countor[F[i]]==0:
                self.place[F[i]] = 2#set the state of current burning points into burnt
                
            if self.countor[F[i]]!= 0: 
                self.countor[F[i]]-=1
                self.place[F[i]] = 1
        self.t=self.t+1
        if self.t==self.arriveT:
            for i in range(len(self.Fighter_Loc)):
                self.MieHuoArea(self.Fighter_Loc[i][0],self.Fighter_Loc[i][1],self.Fighter_Loc[i][2])
            
        


                           
    def Set_prob(self,row,col,Prob):
            self.prob_place[row][col] = Prob


    def draw(self):
        """Draws the cells."""
        return draw_array(self)    
    def draw_array(self):
        cmap1 = LinearSegmentedColormap.from_list('cmap', ['Grey','Cyan'])

        cmap2 = (mpl.colors.ListedColormap(['1', 'red', 'grey']))
        """Draws the cells."""
            
        plt.figure(7,figsize=(20, 20))

        plt.xticks([])
        plt.yticks([])
        plt.imshow(self.prob_place,cmap=cmap1)
        
        
        plt.imshow(self.place,cmap=cmap2,alpha = 0.65,)
        plt.show()
        
    def Print(self):
        print(self.prob_place)
def Res(FP,n):
    for i in range(n): 

        FP.step()

    # FP.draw_array()

n=col
m=row
FirePlace1 = FirePlace(n,m,w,34)
Res(FirePlace1,n)
FirePlace1.Fighter_Loc=Fighter

