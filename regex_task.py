from structures.automaton import Automaton

class Regex:
    def __init__(self, input_string: str) -> None:
        regular_expression, self.letter, self.number_occurrences = input_string.split()
        self.is_regex_valid(regular_expression)
        self.automaton = Automaton()
        self.automaton.configure_from_regex(regular_expression)


    def is_include(self) -> bool:
        if self.automaton.is_include(self.letter,
                                    int(self.number_occurrences),
                                    0):
            print('YES')
            return True
        print('NO')
        return False

    def is_regex_valid(self, regular_expression: str) -> None:
        stack_parse = list()
        alphabet = frozenset(('1', 'a', 'b', 'c'))

        for symbol in regular_expression:
            if (symbol in alphabet):
                stack_parse.append(symbol)
            elif symbol == '+':
                if len(stack_parse) < 2:
                    raise ValueError('Too few operands for the plus operator')
                stack_parse.pop()  
            elif symbol == '.':
                if len(stack_parse) < 2:
                    raise ValueError('Too few operands for the concatenation operator')
                stack_parse.pop()
            elif symbol == '*':
                if len(stack_parse) < 1:
                    raise ValueError('Too few operands for the Klini star operator')
        if len(stack_parse) != 1:
            raise ValueError('Too many operands')