class AzerothCitizen:
    """
    Creates a citizen of Azeroth
    """
    #CONTANTS
    ALLEGIANCE = ("The Horde", "The Alliance", "The Burning Legion", "Neutral")
    JOBS = ("Warrior", "Mage", "Hunter", "Rogue", "Warlock", "Priest", "Druid", "Shaman", "Paladin", "NPC")
    RACE = ("Orc", "Human", "Troll", "Undead", "Gnome", "Tauren", "Night Elf", "Other")
    SEX = ("Male", "Female")

    def __init__(self, name, race, sex, job, allegiance):
        self.name=name
        #race value must be in JOBS
        if race not in self.RACE:
            raise ValueError(f"race must be one of these {self.RACE}")
        else:
            self.race=race

        self.sex = sex
        self.allegiance = allegiance

    def battle_cry(self):
        return f"{self.name} yells: Charge!!"

class Orc(AzerothCitizen):
    """
    Creates Azeroth Citizen Orc
    """
    def __init__(self, name, sex, job):
        super().__init__(name, "Orc", sex, job, "The Horde")

    def battle_cry(self):
        return f"{self.name} yells: FOR THE HORDE!!"

class Human(AzerothCitizen):
    """
    Creates Azeroth Citizen Human
    """
    def __init__(self, name, sex, job):
        super().__init__(name, "Human", sex, job, "The Alliance")


Thrall = Orc("Thrall","Male", "Warrior")
print(Thrall.battle_cry())


Jaina = Human("Jaina", "Female", "Mage")
print(Jaina.battle_cry())