from typing import NamedTuple
from functools import wraps
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import datetime
class AzerothCitizen:
    """
    Creates a citizen of Azeroth
    """
    # class constant attributes
    ALLEGIANCE = ("The Horde", "The Alliance", "The Burning Legion", "Neutral")
    JOBS = ("Warrior", "Mage", "Hunter", "Rogue", "Warlock", "Priest", "Druid", "Shaman", "Paladin", "NPC")
    RACE = ("Orc", "Human", "Troll", "Undead", "Gnome", "Tauren", "Night Elf", "Other")
    SEX = ("Male", "Female")

    def __init__(self, name: str, race: RACE, sex: SEX, job: JOBS):
        self._name = name
        # race value must be in RACE
        if race not in self.RACE:
            raise ValueError(f"race must be one of these {self.RACE}")
        else:
            self._race = race

        self.job = job
        self.sex = sex
    #__repr__ should be unambigous, this will help developer/us to debug code
    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, {self._race}, {self.job}, {self.sex})"

    # our write_scroll use the Scroll that has been setup to lever "with" statement
    def write_scroll(self,message):
        scroll_name = self._name
        with Scroll(scroll_name) as scroll:
            scroll.write(message)


    def battle_cry(self):
        return f"{self._name} yells: Charge!!"

    def get_name(self):
        return self._name



class Orc(AzerothCitizen):
    """
    Creates Azeroth Citizen Orc
    """

    def __init__(self, name: str, sex: str, job: str):

        # _denotes class private variable - Python does not enforce, but rather it is convention
        self._allegiance = "The Horde"
        super().__init__(name, "Orc", sex, job)

    def __repr__(self):
        return f"{self.__class__.__name__} class instance - ({self._name}, {self._race}, {self.job}, {self._allegiance})"

    # @property decorator makes our property read only
    # e.i. thrall.allegiance will only return the value(acting as a getter)'
    # we will no longer be able to set the value with this method: thrall.allegiance = "value
    @property
    def allegiance(self):
        return allegiance


    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE HORDE!!"

    @classmethod
    def thrall(cls):
        return cls("Thrall", "Male", "Shaman")

class Human(AzerothCitizen):
    """
    Creates Azeroth Citizen Human
    """
    def __init__(self, name: str, sex: str, job: str):
        self._allegiance = "The Alliance"
        super().__init__(name, "Human", sex, job)
    def __repr__(self):
        return f"{self.__class__.__name__} class instance - ({self._name}, {self._race}, {self.job}, {self._allegiance})"

    def battle_cry(self):
        return f"{self.get_name()} yells: FOR THE ALLIANCE!!"

    @classmethod
    def jaina(cls):
        return cls("Jaina", "Female", "Mage")

class Leader(AzerothCitizen):
    """
    Creates a Azeroth Citizen Leader
    """
    def __init__(self, name: str, race: str, job: str, allegance: str, tribe: str):
        self.tribe=tribe
        super().__init__(name, race, sex, job, allegiance)

    def __repr__(self):
        return f"{self.__class__.__name__} class instance ({self._name}, {self._race}, {self.allegiance}, {self.tribe})"



class BurningLegion(NamedTuple):
    """
    Creates burning legion member
    """
    name: str
    
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name})"
    
    @property
    def leader(self):
        kiljaeden = BurningLegion("Kil'Jaeden")
        return kiljaeden
    def cast(self, spell):
        print( f"{self.name}: {spell.incantation}!" )
    

@dataclass(frozen=True)
class NewBurningLegion():
    """Creates a burning legion member using immutable dataclass"""
    # no need to define __repr__, dataclass automatically does it for us, pretty neat
    # @dataclass decorator only available in Python 3.6 and up
    name: str
    
    @property
    def leader(self):
        kiljaeden = BurningLegion("Kil'Jaeden")
        return kiljaeden
    def cast(self, spell):
        print( f"{self.name}: {spell.incantation}!" )
        
        
@dataclass
class Fraction:
    name: str
    races: list
    leader: Orc
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1

    
class Spell(metaclass=ABCMeta):
    """Creates a spell base class"""
    def __init__(self, name: str, effect: str,  level: int, element: str, incantation: str ):
        self.name = name
        self.level = level
        self.element = element
        self.effect = effect
        self.incantation = incantation

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.level}, {self.element}, {self.effect})"

    # The child class must define this method, else the wrath of the Class gods
    @abstractmethod
    def cast(self):
        pass

    #The child class must define this method, else the wrath of the Class gods
    @abstractmethod
    def defining_feature(self):
        pass

class FireBall(Spell):
    '''
    creates a Fire ball spell
    '''
    def __init__(self, name: str, effect: str, level: int, element: str, incantation: str ):
        super().__init__(name, effect, level, element, incantation)

    def cast(self):
        return print(f"{self.incantation}")
    @property
    def defining_feature(self):
        return f"{self.element} elemental spell"

# custom context manager using built in statement "with"
# our class scroll will write a "scroll"
# by defining __enter__ and __exit__ in our class, we can leverage "with" statements's feature
# "with" will handle the closing of files open by our class
# i.e:  with Scroll("name here") as s:
#           s.write(...)
class Scroll:
    def __init__(self,scroll_name):
        self.scroll_name = scroll_name + ".scroll"

    def __enter__(self):
        self.scroll = open(self.scroll_name,"w")
        return self.scroll

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.scroll:
            self.scroll.close()


# only execute the code below if __name__ is main, which  means the file(azeroth.py) being ran in the main file
# i.e "python azeroth.py", otherwise it will not execute
# i.e if azeroth.py is imported, the code below will not be execute, because it no longer the "main file"
if __name__ == "__main__":
    thrall = Orc.thrall()
    print(thrall)
    thrall.write_scroll("blood and thunder!, dabu")


    the_horde = Fraction("The Horde", ['Orcs', 'Trolls', 'Undeads', 'Taurens'], thrall)
    print(the_horde)

    spell = FireBall("Fire Ball", "Shoots fire ball", 0, "Fire", "Hadoken!")
    print(spell)

    grunt = BurningLegion("grunt")
    print(grunt)
    

    

    jaina = Human.jaina()
    print(jaina)


