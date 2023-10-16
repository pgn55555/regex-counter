class State:
    def __init__(self,
                 is_terminate: bool = False) -> None:
        self.is_terminate = is_terminate;
        self.jumps = list()
