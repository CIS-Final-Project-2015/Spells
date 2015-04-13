# usr/bin/python3
# Program Name: Spell_Central.py
# Author: Luke Gosnell
# Date: 3/13/2015

#Range and Spell Resistence are dependant on other aspects of World
#Spells without listed durations are instantaneous

#Duration and SavingThrow uncomplete

#CLERIC SPELLS

CastingTime = 0
Range = 0
RequiredRange = 0
Duration = 0
SavingThrow = 0
SpellResistance = "None"

class spells(object):
    def __init__(self,spellPoints):
        self.spellPoints = spellPoints

        def CreateWater(self):
            #Creates 2 gallons of water
            self.CastingTime = CastingTime + 1
            self.RequiredRange = RequiredRange + 25
            if Range < self.RequiredRange:
                print("Too far away!")
                return
        def CureMinorWounds(self):
            #Cures 1 point of damage
        def DetectPoison(self):
            #Detects poison in one creature or object
            self.CastingTime = CastingTime + 1
            self.RequiredRange = RequiredRange + 25
            if Range < self.RequiredRange:
                print("Too far away!")
        def Guidance(self):
            self.CastingTime = CastingTime + 1
            self.RequiredRange = 0
            if Range < self.RequiredRange:
                print("Too far away!")
            GuidanceChoice = input("+1 on which one? 1. ATTACK ROLL 2. SAVING THROW 3. SKILL CHECK")
            if GuidanceChoice = ("1","attack roll","Attack roll","Attack Roll", "ATTACK ROLL"):
                #Attack roll +1
            elif GuidanceChoice = ("2","saving throw","Saving throw","Saving Throw","SAVING THROW"):
                self.SavingThrow = SavingThrow + 1
            elif GuidanceChoice = ("3","skill check", "Skill check", "Skill Check", "SKILL CHECK"):
                #Skill check +1
        def Light(self):
            #Object shines like a torch
            self.CastingTime = CastingTime + 1
            self.RequiredRange = 0
            if Range < self.RequiredRange:
                print("Too far away!")
            #Duration of 10 min
            #Resistance is Object (self.SpellResistance = "Object")
        def Mending(self):
            #Makes repairs on an object
            self.CastingTime = CastingTime + 1
            self.RequiredRange = RequiredRange + 10
            if Range < self.RequiredRange:
                print("Too far away!")
            #Resistance is Object (self.SpellResistance = "Object")
        def PurifyFoodAndDrink(self):
            #Purifies 1 cu. ft./level of food or water
            self.CastingTime = CastingTime + 1
            self.RequiredRange = RequiredRange + 10
            if Range < self.RequiredRange:
                print("Too far away!")
            #Resistance is Harmless and Object (self.SpellResistance = "Harmless","Object")
        def ReadMagic(self):
            #Read scrolls and spell books
             self.CastingTime = CastingTime + 1
             #self.RequiredRange is specific to player(personal)
        def Resistance(self):
            #Subject gains +1 on saving throws
            self.CastingTime = CastingTime + 1
            self.RequiredRange = 0
            if Range < self.RequiredRange:
                print("Too far away!")
            #Duration of 1 min
            #Resistance is harmless (self.SpellResistance = "harmless")
        def Virtue(self:)
            #Subject gains 1 temporary hp
            self.CastingTime = CastingTime + 1
            self.RequiredRange = 0
            if Range < self.RequiredRange:
                print("Too far away!")
            #Duration of 1 min
            #Resistance is harmless (self.SpellResistance = "harmless")
            
            
        
                
            
