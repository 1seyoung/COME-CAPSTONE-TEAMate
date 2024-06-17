from base.agent_manage import AgentManagement
import dill

class StudentData(AgentManagement) :
    def __init__(self, class_name, team, name_list,):
        super().__init__()
        self.agent = {"class" : class_name, "team" : team, "score_table" : {name: 0 for name in name_list}}
        
