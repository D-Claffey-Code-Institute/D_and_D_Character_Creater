import random

def rand_ability_scores():
    """
    Generates six random ability scores simulating rolling 3 six sided dice
    for each ability: Strenght, Dexterity, Constitution, Intelligence, Wisdom
    and Charisma. 
    """
    abilities = {
        "Strenght": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    for i in range(6):
    # creates a list scores, generating a number between 1 and 6, 3 times
    # sums the results and assigns them to each ability in the abilities dictionary
        scores = [random.randint(1, 6) for x in range(3)]
        abilities[list(abilities.keys())[i]] = sum(scores)
    return abilities

final_abilities = rand_ability_scores()




def rand_name(fnames, lnames):
    """
    Generates a random name from a list of popular D and D names 
    """
    
    # Takes a random first and last name from a set list
    fname = random.choice(fnames)
    lname = random.choice(lnames)
    return f"{fname} {lname}"

fnames = ["Bob", "Varis", "Nyx", "Luna", "Ash", 
"Jack", "Lilith", "Nix", "Zephyer", "Rhogar", 
"Cleric", "Bard", "Raven", "Ember", "Shadow"]

lnames = ["Lendor", "Etril", "Sakaris", "Witchelm", 
"Oskandor", "Edoril", "Sakaris", "Calmaria", 
"Lorvil", "Morningstar", "Caverns", 
"Thundershade", "Thalor", "Wildgrove", 
"Everflame"]

fullname = rand_name(fnames, lnames)




def rand_alignment(alignments):
    """
    Generates a random alignment 
    """

    # Takes a random alignment from a set list
    alignment = random.choice(alignments)
    return f"{alignment}"
    
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", 
"Lawful Neutral", "True Neutral", "Chaotic Neutral", 
"Lawful Evil", "Neutral Evil", "Chaotic Evil"]

alignment = rand_alignment(alignments)


def rand_race_and_occupation(races, occupations):
    """
    Generates a random race and class
    """

    # Takes a random race and class from a set list
    race = random.choice(races)
    occupation = random.choice(occupations)
    return f"{race} {occupation}"
    
races = ["Dragonborn", "Dwarf(Hill)", "Dwarf(Mountain)", 
"Elf(Drow)", "Elf(High)", "Elf(Wood)", "Gnome(Forest)", 
"Gnome(Rock)", "Half-Elf", "Half-Orc", "Halfling(Lightfoot)", 
"Halfling(Stout)", "Human", "Tiefling"]
occupations = ["Barbarian", "Bard", "Cleric", "Druid", 
"Fighter", "Monk", "Paladin", "Ranger", "Rogue", 
"Sorcerer", "Warlock", "Wizard"]

race_occupation = rand_race_and_occupation(races, occupations)







print(f"Name: {fullname}\nRace/Class: {race_occupation}\nAbilities: {final_abilities}\nAlignment: {alignment}")