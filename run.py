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

result = rand_ability_scores()
print(result)



def rand_name(fnames, lnames):
    """
    Generates a random name from a list of popular D and D names 
    """
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
print(fullname)



def rand_alignment(alignments):
    """
    Generates a random alignment 
    """
    alignment = random.choice(alignments)
    return f"{alignment}"
    
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", 
"Lawful Neutral", "True Neutral", "Chaotic Neutral", 
"Lawful Evil", "Neutral Evil", "Chaotic Evil"]

alignment = rand_alignment(alignments)
print(alignment)





print(f"Name: {fullname}\n ")