from base.environment_manage import EnvironmentManagement
import pandas as pd
import dill
from datetime import datetime

class ContextData(EnvironmentManagement) :
    def __init__(self, df, para):
        super().__init__()
        self.environment = {"df" : df, "parameter" : para}
        
if __name__ == "__main__":
    text = [
        {"name" : "jy", "time" : datetime.strptime("2023-08-07 17:46:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "jy", "time" : datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "sy", "time" : datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "sy", "time" : datetime.strptime("2023-08-08 17:46:02", "%Y-%m-%d %H:%M:%S"), "text" : "집가고싶다"},
    ]
    para = {"type" : "short", "timeblock" : 10, "file" : 1, "photo" : 1, "pingpong" : {5 : 1, 7 : 1.5, 10 : 3, 20 : 5, "full" : 8}, "nonpingpong" : {5 : 0, 7 : 0, 10 : 1, 20 : 2, "full" : 3}, "starter" : 1}
    df = pd.DataFrame(text)
    
    result = ContextData(df, para)
    with open("./env/context.simx", "wb") as f:
        dill.dump(result, f)