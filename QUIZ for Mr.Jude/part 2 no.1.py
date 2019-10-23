#%%quiz

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + "" + self.incantation + "\n" + self.get_description()

    def get_description(self):
         return "No description"
     
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        return Spell.__init__(self, "Accio", "Summoning Charm")
    
    def getDescription(self): # this is the code we have to add for question d
        return "This charm summons an object to the caster, potentially over a significant distance."

class Confundo(Spell):
    def __init__(self):
        return Spell.__init__(self, "Confundo", "Confundus Charm")
      
    def get_description(self):
        return "Causes the victim to become confused and befuddled."
    
def study_spell(spell):
        print(spell)
        
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
#%%
a. What are the parent and child classes here?
b. What does the code print out? (Try figuring it out without running it in Python)
c. Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
d. What do we need to do so that ‘print Accio()’ will print the appropriate description (‘This charm summons
an object to the caster, potentially over a significant distance’)?
Write down the code that we need to add and/or change.
