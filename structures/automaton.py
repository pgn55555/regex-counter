from .state import State
from .jump import Jump

class Automaton:
    def __init__(self) -> None:
        self.states = list()
        self.index_start = -1
        self.dfs_counter = list()
        self.dfs_stack = list()

    def add_state(self, is_terminate: bool = False) -> None:
        self.states.append(State(is_terminate))
    
    def add_jump(self,
                 from_state: int,
                 to_state: int, 
                 letter: str) -> None:
        self.states[from_state].jumps.append(Jump(from_state,
                                                  to_state,
                                                  letter))
    
    def configure_from_regex(self,
                             regular_expression: str) -> None:
        alphabet = frozenset(('1', 'a', 'b', 'c'))
        stack_nodes = list()
        index_end_of_state = -1

        for symbol in regular_expression:
            if (symbol in alphabet):
                self.add_state()
                self.add_state(True)
                index_end_of_state += 2
                self.add_jump(index_end_of_state - 1,
                              index_end_of_state,
                              symbol if symbol != '1' else 'eps')
                stack_nodes.append((index_end_of_state - 1,
                                    index_end_of_state))
            elif symbol == '+':
                self.add_state()
                self.add_state(True)
                second_node = stack_nodes.pop()
                first_node = stack_nodes.pop()
                index_end_of_state += 2
                self.add_jump(index_end_of_state - 1,
                              first_node[0],
                              'eps')
                self.add_jump(index_end_of_state - 1,
                              second_node[0],
                              'eps')
                self.add_jump(first_node[1],
                              index_end_of_state,
                              'eps')
                self.add_jump(second_node[1],
                              index_end_of_state,
                              'eps')
                self.states[first_node[1]].is_terminate = False
                self.states[second_node[1]].is_terminate = False
                stack_nodes.append((index_end_of_state - 1,
                                    index_end_of_state))
            elif symbol == '.':
                second_node = stack_nodes.pop()
                first_node = stack_nodes.pop()
                self.add_jump(first_node[1],
                              second_node[0],
                              'eps')
                self.states[first_node[1]].is_terminate = False
                stack_nodes.append((first_node[0],
                                    second_node[1]))
            elif symbol == '*':
                node = stack_nodes.pop()
                self.add_jump(node[1],
                              node[0],
                              'eps')
                self.states[node[1]].is_terminate = False
                self.states[node[0]].is_terminate = True
                stack_nodes.append((node[0],
                                    node[0]))
        
        self.index_start = stack_nodes.pop()[0]

    def is_include(self,
                   letter: str,
                   number_occurrences: int,
                   current_number_occurrences: int,
                   current_index_state: int = -1) -> bool:
        if current_index_state == -1:
            self.dfs_counter = [-1] * len(self.states)
            self.dfs_stack.append(self.index_start)

        while len(self.dfs_stack):
            current_index_state = self.dfs_stack.pop()
            current_state = self.states[current_index_state]
            self.dfs_counter[current_index_state] = current_number_occurrences

            if current_state.is_terminate and \
                number_occurrences == current_number_occurrences:
                return True
            
            for jump in current_state.jumps:
                if jump.letter == letter:
                    if (number_occurrences >= current_number_occurrences + 1):
                        current_number_occurrences += 1
                        self.dfs_stack.append(jump.to_state)
                else:
                    if (self.dfs_counter[jump.to_state] < current_number_occurrences):
                        self.dfs_stack.append(jump.to_state)
        
        return False
