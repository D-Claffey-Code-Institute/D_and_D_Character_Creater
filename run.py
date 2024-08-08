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
