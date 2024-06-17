from base.bootloader import BootLoader
import dill

class TimeLoader(BootLoader):
    def __init__(self):
        super().__init__()
        self.state = "TIMEBLOCK"
        self.parts = ["timeblock.simx"]


if __name__ == "__main__":
    loader = TimeLoader()
    with open("./bootloader/timeloder.simx", "wb") as f:
        dill.dump(loader, f)
