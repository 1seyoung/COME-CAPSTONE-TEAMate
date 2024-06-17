from base.parts_model import PartsModel
import dill
import time
import pandas as pd

class TimeBlockModel(PartsModel):
    def __init__(self):
        super().__init__()

    def run_parts(self):
        #block_size = self.environment["parameter"]["timeblock"]  # 10초 기준 시간 블록 크기
        block_size = 600
        check_row = None
        self.environment["df"]['timeblock'] = None
        for index, row in self.environment["df"].iterrows():
            if index < 1 :
                self.environment["df"].loc[index, 'timeblock'] = 0
                row['timeblock'] = 0
                check_row = row
                continue
            
            if (row['time'] - check_row['time']).total_seconds() < block_size :
                self.environment["df"].loc[index,'timeblock'] = check_row['timeblock']
                row['timeblock'] = check_row['timeblock']
            else :
                self.environment["df"].loc[index, 'timeblock'] = check_row['timeblock'] + 1
                row['timeblock'] = check_row['timeblock'] + 1
            check_row = row
        print(self.environment["df"])


if __name__ == "__main__":
    timeblock = TimeBlockModel()
    with open("./partsmodel/timeblock.simx", "wb") as f:
        dill.dump(timeblock, f)
