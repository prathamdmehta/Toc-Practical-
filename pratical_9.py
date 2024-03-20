class DPDA:
    def __init__(self, trf, input, state):
        self.head = 0
        self.trf = trf
        self.state = str(state)
        self.input = input
        self.stack = ['z']
    def step(self):
        a = self.input[self.head]
        s = self.stack.pop()
        state, ss = self.trf.get((self.state, a, s))
        if ss != 'e': 
           for s in ss[::-1]:
               self.stack.append(s)
           self.state = state
        print(' {:20s} [{:10s}] {:5s}'.format(self.input[self.head:],''.join(self.stack),self.state))
        self.head += 1
    def run(self):
        print(' {:20s} [{:10s}] {:5s}'.format(self.input[self.head:],''.join(self.stack),self.state))
        while self.head < len(self.input):
            self.step()
        s = self.stack.pop()
        if self.trf.get((self.state, 'e', s)):
            state, ss = self.trf.get((self.state, 'e', s))
            self.state = state
            print(' {:20s} [{:10s}] {:5s}'.format('e',''.join(self.stack), self.state))

DPDA({
    ('q','a','z'): ('q', 'xz'),
    ('q','a','x'): ('q', 'xx'),
    ('q','b','x'): ('p', 'e'),
    ('q','b','x'): ('p', 'e'),
    ('q','e','z'): ('acc', 'z'),
    },
     'aaaaaaaaabbbbbbbbb','q').run()
           
    
    
