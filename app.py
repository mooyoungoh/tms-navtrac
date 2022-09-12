from tms import main as mstMain
from navTrac_api import main as navMain

tms_data = mstMain()
nav_data = navMain()

miss_list = []

for key in tms_data.keys():
    tms_data[key].sort(key=lambda x: x.createdAt)

for key in nav_data.keys():
    nav_data[key].sort(key=lambda x: x.createdAt)
    
for key in tms_data.keys():
    listT = tms_data[key]
    listT_len = len(listT)
    if key in nav_data:
        listN = nav_data[key]
        listN_len = len(listT)
        if listT_len != listN_len:
            miss_list.add(key)
            print("he")
        else:
            print("?")




# Container
# 
# 

# TMS             NavTrack
# 123 ->1         123 -> 1
#       2                2
#       3               