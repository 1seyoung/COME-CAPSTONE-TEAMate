from base.execution_engine import ExecutionEngine
from context_obj import ContextData
from student_obj import StudentData
from multiprocessing import Pool
from rx import create
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    agent_list = []
    env_list = []
    
    name_list = ["jy", "sy", "sh"]
    result_obj = StudentData("com101", "team1", name_list)
    
    text = [
        {"name" : "jy", "time" : datetime.strptime("2023-08-07 17:46:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "jy", "time" : datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "sy", "time" : datetime.strptime("2023-08-07 17:47:02", "%Y-%m-%d %H:%M:%S"), "text" : "안녕하세요"},
        {"name" : "sy", "time" : datetime.strptime("2023-08-08 17:46:02", "%Y-%m-%d %H:%M:%S"), "text" : "집가고싶다"},
    ]
    para = {"type" : "short", "timeblock" : 600, "file" : 1, "photo" : 1, "pingpong" : {5 : 1, 7 : 1.5, 10 : 3, 20 : 5, "full" : 8}, "nonpingpong" : {5 : 0, 7 : 0, 10 : 1, 20 : 2, "full" : 3}, "starter" : 1}
    ##timeblock 기준 : min
    
    df = pd.DataFrame(text)
    context = ContextData(df, para)
    
    engine = ExecutionEngine(5)
    engine.append_bootloader("timeloder", "./bootloader/timeloder.simx")
    #engine.append_bootloader("analysisloder", "./bootloader/analysisloder.simx")
    
    engine.state = "timeloder"
    engine.set_agent_source(result_obj.get_source())
    engine.set_env_source(context.get_source())
    
    engine.run_multi_parts()
    
    
    