class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

class PDA:
    def __init__(self):
        self.stack = Stack()
        self.current_state = 'q0'
        self.final_states = {'q_accept'}
        self.transitions = {
            ('q0', '(', ''): ('q0', '('), 
            ('q0', '(', '('): ('q0', '(('), 
            ('q0', 'digit', ''): ('q1', ''), 
            ('q0', 'digit', '('): ('q1', '('),
            ('q1', 'digit', ''): ('q_reject', ''),  # Birden fazla basamaklı sayıyı reddet
            ('q1', 'digit', '('): ('q_reject', ''), # Birden fazla basamaklı sayıyı reddet
            ('q1', '+', ''): ('q0', ''), 
            ('q1', '-', ''): ('q0', ''), 
            ('q1', '*', ''): ('q0', ''), 
            ('q1', '/', ''): ('q0', ''), 
            ('q1', '+', '('): ('q0', '('), 
            ('q1', '-', '('): ('q0', '('), 
            ('q1', '*', '('): ('q0', '('), 
            ('q1', '/', '('): ('q0', '('), 
            ('q0', ')', '('): ('q1', ''), 
            ('q1', ')', '('): ('q1', ''), 
            ('q1', 'e', ''): ('q_accept', '') 
        }

    def process_input(self, input_string):
        self.stack.push('')  # Başlangıç yığın sembolü
        input_string += 'e'  # Girdi sonu işareti

        for symbol in input_string:
            if symbol.isdigit():
                symbol = 'digit'
            current_stack_top = self.stack.top()
            if (self.current_state, symbol, current_stack_top) in self.transitions:
                next_state, stack_action = self.transitions[(self.current_state, symbol, current_stack_top)]
                if stack_action == '':  # Pop işlemi
                    self.stack.pop()
                elif stack_action != current_stack_top:
                    self.stack.push(stack_action[-1])
                self.current_state = next_state
            else:
                print("Geçersiz ifade.")
                return False

            if self.current_state == 'q_reject':
                print("Geçersiz ifade.")
                return False

        if self.current_state in self.final_states and self.stack.is_empty():
            print("Geçerli ifade.")
            return True
        else:
            print("Geçersiz ifade.")
            return False

# Kullanıcı girdisi alınıyor
def main():
    expression = input('Matematiksel bir ifade girin: ')
    pda = PDA()
    if pda.process_input(expression):
        print('İfade geçerli.')
    else:
        print('İfade geçersiz.')

if __name__ == '__main__':
    main()
