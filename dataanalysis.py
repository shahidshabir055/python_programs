# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:39:58 2020

@author: eshah
"""

import pandas as pd

dt={"SNo.":[1,2,3,4,5,6],"shahid":[6,4,3,8,9,1],"Ifrah":[6,4,2,9,1,8]}
df=pd.DataFrame(dt)
print(df)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df.timetuple)