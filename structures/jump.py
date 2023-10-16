class Jump:
    def __init__(self,
                 from_state: int,
                 to_state: int, 
                 letter: str) -> None:
        self.from_state = from_state
        self.to_state = to_state
        self.letter = letter