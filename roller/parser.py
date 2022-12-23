from roller import dice

class Script():
    def __init__(self, script):
        self.script = script
        self.actions = []
    
    def parse(self):
        """Parse the script and return the result"""
        self.actions = self.script.split(';')
        for action in self.actions:
            acts = action.split()
            res = []
            for act in acts:
                if 'd' in act:
                    s = act.split('d')
                    if len(s) == 2:
                        if s[0].isdigit() and s[1].isdigit():
                            for i in range(int(s[0])):
                                res += dice.Dice(int(s[1]))
                        else:
                            print('Invalid dice')
                            break
                    for i in res:
                        i.roll()
                elif 'ig' in act:
                    s = act.split('ig')[0]
                    if s.isdigit():
                        res = [i for i in res if i > int(s)]
                    