from PIL import Image
global Water_prob
global Wood_House_Prob
global Road_Prob 

global Water_RGB
global Road_RGB
global House_RGB

global FirePlace_Map

Fighter= [(127,140,10),(130,165,10),(104,145,10), (108,160,10)]
row = 300
col = 300

Water_RGB = [0,100]
House_RGB = [100,210]

Water_prob = 0
Wood_House_Prob = 0.9
Road_Prob = 1

FirePlace_Map = Image.open('/Users/weiliang/ST/new london final.jpg')
wind_condition = ['w','n','e','s']
w='n'