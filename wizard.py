#!/usr/bin/env python3

from configparser import ConfigParser
import sys
import os.path

##### HOMEWORK  
#  reorganize your code. 
#  apply literate programming (comments)
#  test out completion algorithm in >>> (IDE)

def main():
    set_readline() 
    wiz_help()
    wiz = load('wiz.save')

    try:
        while True:
            task = input("> ")
            task = task.strip().lower()
            print(request(wiz, task))

            save(wiz)
    except (KeyboardInterrupt, EOFError):
        bye()

def request(wiz, task):
    if task in ["quit", "q", "Q"]:
        bye()
    elif task in wiz.locations:
        return wiz.travel(task)
    elif task == "brew":
        return wiz.brew()
    elif task == "forage":
        return wiz.forage()
    elif task == "gift":
        return wiz.gift()
    elif task == "gold":
        return wiz.purse()
    elif task == "health":
        return wiz.health()
    elif task in ["help", "h", "?"]:
        return wiz_help()
    elif task in ["location", "where"]:
        return wiz.where()
    elif task == "purse":
        return wiz.purse()
    elif task == "relax":
        return wiz.relax()
    elif task == "sell":
        return wiz.sell()
    elif task in ["skill level", "skill", "skills"]:
        return wiz.health
    elif task == "shop":
        return wiz.shop()
    elif task == "study":
        return wiz.study()
    elif task == "work":
        return wiz.work()
    else:
        print(f'''I dunno "{task}".''')

class Wizard:
    def __init__(self, location="forest", skill=0, gold=0, books=1, stress=0,
            ego=0, potions=0, mushrooms=0, work=0):
        self.books = int(books)
        self.ego = int(ego)
        self.gold = int(gold)
        self.location = location
        self.mushrooms = int(mushrooms)
        self.skill = int(skill)
        self.stress = int(stress)
        self.potions = int(potions)

        self.locations = {
            "forest" : "You travel to the forest where " \
                "you can forage for mushrooms and relax.",
            "tower"  : "You travel to your tower where there is peace and quiet.",
            "village" : "You travel to your village where " \
                "you can work, sell goods and shop.",
            "black rock city" : "You travel to the playa )'(.",
            }

    def travel(self, location):
        if location not in self.locations: 
            msg = f'''{location} is not a place in this land.'''
        elif location == self.location:
            msg = f'''You are already in the {location}.'''
        else:
            self.location = location
            msg = f'''{self.locations[location]}'''
        return msg
    
    def study(self):
        if self.location == "tower":
            if self.skill < self.books:
                self.skill += 1
                self.stress += 1
                self.books -= 1
                msg = f'''Your skill level is now {self.skill}.'''
            else:
                msg = f'''You have no more new books to read.'''
        else:
            msg = f'''You cannot study in the {self.location}.'''
        return msg

    def brew(self):
        if self.location == "tower":
            if self.mushrooms == 0:
                msg = f'''You can't brew potions without mushrooms.'''
            else:
                self.mushrooms -= 1
                self.potions += 1
                self.stress -= 1
                msg = f'''You now have {self.potions} potions.'''
        else:
            msg = f'''You cannot brew potions in the {self.location}.'''
        return msg
    
    def forage(self):
        if self.location == "forest":
            self.mushrooms += 1
            msg = f'''You now have {self.mushrooms} mushrooms.'''
        else:
            msg = f'''There are no mushrooms in the {self.location}.'''
        return msg

    def gift(self):
        if self.location == "black rock city":
            if self.potions > 0:
                self.potions -= 1
                if self.stress > 0:
                    self.stress -= 1
                    msg = f'''You now have {self.potions} potions and you have lowered your stress level.'''
                else:
                    msg = f'''You now have {self.potions} potions.'''
            else:
                msg = f'''You have no potions to gift.'''
        else:
            msg = f'''You cannot give gifts in the {self.location}.'''
        return msg

    def where(self):
        if self.location is None:
            msg = f'''You are nowhere. Where would you like to go?'''
        else:
            msg = f'''You are at the {self.location}.'''
        return msg

    def purse(self):
        msg = f'''   You have {self.books} books\n'''
        msg += f'''   You have {self.gold} gold\n'''
        msg += f'''   You have {self.mushrooms} mushrooms\n'''
        msg += f'''   You have {self.potions} potions'''
        return msg

    def relax(self):
        if self.location == "forest":
            if self.stress > 0:
                self.stress -= 1
            msg = f'''You now have {self.stress} stress level.'''
        else:
            msg = f'''You can't relax in {self.location}.'''
        return msg

    def sell(self):
        if self.location == "village":
            if self.potions > 0:
                self.gold += 1
                msg = f'''You now have {self.gold} gold.'''
            else:
                msg = f'''You have no brewed potions to sell.'''
        else:
                msg = f'''You can't sell goods in the {self.location}.'''
        return msg

    def shop(self):
        if self.location == "village":
            if self.gold == 0:
                msg = f'''You have {self.gold} gold. You must work to earn gold.'''
            else:
                if self.stress >10:
                    msg = "You are too stressed out. Go do relaxing things."
                else:
                    self.gold -= 1
                    self.books += 1
                    self.stress += 1
                    msg = f'''You now have {self.books} books and {self.gold} gold.'''
        else:
            msg = f'''You can't shop in the {self.location}.'''
        return msg

    def health(self):
        msg = f'''   You have a stress level of {self.stress}.\n'''
        msg += f'''   You have a skill level of {self.skill}.''' 
        return msg

    def work(self):
        if self.location == "village":
            if self.skill > 0:
                self.gold += 1
                self.skill -= 1
                if self.stress >10:
                    msg = "You are too stressed out. Go do relaxing things."
                else:
                    self.stress += 1
                    msg = f'''All in a day's work. You now have {self.gold} gold.'''
            else:
                msg = f'''You can't work without any skills.'''
        else:
            msg = f'''There is no work in the {self.location}.'''
        return msg

def completion(text, state):
    options = [
        "black rock city",
        "brew",
        "forage",
        "forest",
        "gift",
        "gold",
        "health",
        "location",
        "purse",
        "relax",
        "sell",
        "skill level",
        "shop",
        "study",
        "tower",
        "travel",
        "village", 
        "work",
    ]
    matches = []
    
    for option in options:
        if option.startswith(text):
            matches.append(option)
    if state >= len(matches):
        return None
    return matches[state]

def set_readline():
    import readline

    readline.set_auto_history(True)
    readline.set_completer(completion)

    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

def save(wiz):
    data = ConfigParser()
    data['wizard'] = {
        "location": wiz.location,
        "skill": wiz.skill,
        "gold": wiz.gold,
        "books": wiz.books,
        "stress": wiz.stress,
        "ego": wiz.ego,
        "potions": wiz.potions,
        "mushrooms": wiz.mushrooms,
    }

    save_file = open("wiz.save", "w")
    data.write(save_file)

def load(save_file):
    data = ConfigParser()
    if os.path.isfile(save_file):
        data.read(save_file)
    else:
        data['wizard'] = {}
    
    wiz = Wizard(**data['wizard'])
    return wiz

def wiz_help():
    msg = '''\n LOCATIONS: '''
    msg += '''\n forest ''' 
    msg += '''\n village ''' 
    msg += '''\n tower '''
    msg += '''\n black rock city '''
    msg += '''\n'''
    msg += '''\n ACTIONS: '''
    msg += '''\n brew '''
    msg += '''\n forage '''
    msg += '''\n gift'''
    msg += '''\n gold '''
    msg += '''\n location '''
    msg += '''\n purse '''
    msg += '''\n sell '''
    msg += '''\n skill level '''
    msg += '''\n shop '''
    msg += '''\n study '''
    msg += '''\n work '''
    msg += '''\n'''
    msg += '''\n help '''
    msg += '''\n quit '''
    msg += '''\n \n Please choose an action or location. ''' 
    return msg

def bye():
    print("\nThank you for playing!")
    sys.exit()

if __name__ == "__main__":
    main()