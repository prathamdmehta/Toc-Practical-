class FA:
    def __init__(self):
        self.current_state = "q0"
        self.accept_states = ["q2"]
    
    def transition(self, input_char):
        if self.current_state == "q0":
            if input_char == "1":
                self.current_state = "q1"
            else: 
                self.current_state = "q0"
        elif self.current_state == "q1":
            if input_char == "0":
                self.current_state = "q2"
            else: 
                self.current_state = "q1"
        elif self.current_state == "q2":
            if input_char == "1":
                self.current_state = "q2"
            else: 
                self.current_state = "q0"

    def is_accepted(self):
        return self.current_state in self.accept_states

    def process_input_string(input_string, automation):
        for char in input_string:
            automation.transition(char)
        return automation.is_accepted()

input_string = "1011111"
automation = FA()
print(FA.process_input_string(input_string, automation))
