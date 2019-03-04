class AzerothCitizen:
    """
    Creates a citizen of Azeroth
    """
    # class constant attributes
    ALLEGIANCE = ("The Horde", "The Alliance", "The Burning Legion", "Neutral")
    JOBS = ("Warrior", "Mage", "Hunter", "Rogue", "Warlock", "Priest", "Druid", "Shaman", "Paladin", "NPC")
    RACE = ("Orc", "Human", "Troll", "Undead", "Gnome", "Tauren", "Night Elf", "Other")
    SEX = ("Male", "Female")

    def __init__(self, name: str, race: RACE, sex: SEX, job: JOBS, allegiance: ALLEGIANCE):
        self._name = name
        # race value must be in RACE
        if race not in self.RACE:
            raise ValueError(f"race must be one of these {self.RACE}")
        else:
            self._race = race

        self.job = job
        self.sex = sex
        self.allegiance = allegiance

    def __repr__(self):
        return f"Azeroth citizen object -  {self._name}, {self._race}, {self.job}, {self.sex}, {self.allegiance}"

    def battle_cry(self):
        return f"{self._name} yells: Charge!!"

    def get_name(self):
        return self._name



class Orc(AzerothCitizen):
    """
    Creates Azeroth Citizen Orc
    """
    def __init__(self, name: str, sex: str, job: str):
        super().__init__(name, "Orc", sex, job, "The Horde")

    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE HORDE!!"


class Human(AzerothCitizen):
    """
    Creates Azeroth Citizen Human
    """
    def __init__(self, name: str, sex: str, job: str):
        super().__init__(name, "Human", sex, job, "The Alliance")

    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE ALLIANCE!!"

class Leader(AzerothCitizen):
    """
    Creates a Azeroth Citizen Leader
    """
    def __init(self, name: str, race: str, job: str, allegance: str, tribe: str):
        self.tribe=tribe
        super().__init__(name, race, sex, job, allegiance)

    @classmethod
    def thrall(cls):
        return Orc("Thrall", "Male", "Warrior")

    @classmethod
    def jaina(cls):
        return Human("Jaina", "Female", "Mage")


if __name__ == "__main__":

    thrall = Leader.thrall()
    print(thrall.battle_cry())

    jaina = Leader.jaina()
    print(jaina.battle_cry())

