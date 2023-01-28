from PIL import Image
import numpy as np

global FirePlace_Map

Fighter= [(127,140,10),(130,165,10),(104,145,10), (108,160,10)]


row_list = np.arange(1000)
col_list = np.arange(1000)


Water_RGB = [0,100]
House_RGB = [100,210]
Water_prob_list = np.linspace(0,1,100)
Wood_House_Prob_list = np.linspace(0,1,100)
Road_Prob_list = np.linspace(0,1,100)

FirePlace_Map = Image.open('/Users/weiliang/ST/new london final.jpg')
wind_condition = ['w','n','e','s']
w='n'
print(Water_prob_list)