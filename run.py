import random
import pyfiglet
heading = pyfiglet.figlet_format("D and D Character Creator")
def create_rand_character():
    """
    Main Function:  Gives ability to the user to pick a name or let a random one be choosen.
                    Randomly assigns ability scores, race, class and alignment
    """


    def rand_ability_scores():
        """
        Randonmly assigns a score to all abilities based an 3 d6 rolls. (a d6 is a six sided die)
        """
        abilities = {
            "Strenght": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
            }

        # creates a list scores, generating a number between 1 and 6, 3 times
        # sums the results and assigns them to each ability in the abilities dictionary
        for i in range(6):
            
            scores = [random.randint(1, 6) for x in range(3)]
            abilities[list(abilities.keys())[i]] = sum(scores)
        return abilities

    final_abilities = rand_ability_scores()
        

    def rand_name(fnames, lnames):
        """
        Allows the user to input their own name or generates a random name from a list of popular D and D names 
        """
        
        # Takes a random first and last name from a set list
        fname = random.choice(fnames)
        lname = random.choice(lnames)
        return f"{fname} {lname}"

    # List of random fantasy first names
    fnames = ["Bob", "Varis", "Nyx", "Luna", "Ash", 
    "Jack", "Lilith", "Nix", "Zephyer", "Rhogar", 
    "Cleric", "Bard", "Raven", "Ember", "Shadow"]

    # List of random fantasy second names
    lnames = ["Lendor", "Etril", "Sakaris", "Witchelm", 
    "Oskandor", "Edoril", "Sakaris", "Calmaria", 
    "Lorvil", "Morningstar", "Caverns", 
    "Thundershade", "Thalor", "Wildgrove", 
    "Everflame"]
    
    # User input for first name, only allows letters and a max lenght of 10 characters
    first_name = input("Enter your Characters first name\nLetters Only and Max lenght 10 characters\nOr press enter for a random name....\n")
    
    while first_name:
        if not first_name.isalpha():
            print("Invalid input. Please enter letters only...")
        elif len(first_name) > 10:
            print("Invalid input: Max characters is 10. Try again...")          
        else:
            break
        first_name = input("Enter your Characters first name\nor press enter for a random name:\n")   
    if not first_name: 
        first_name = random.choice(fnames)

    # User input for last name, only allows letters and a max lenght of 10 characters
    last_name = input("Enter your Characters first name\nLetters Only and Max lenght 10 characters\nOr press enter for a random name....\n")    
    while last_name:
        if not last_name.isalpha():
            print("Invalid input. Please enter letters only...")
        elif len(last_name) > 10:
            print("Invalid input: Max characters is 10. Try again...")          
        else:
            break
        last_name = input("Enter your Characters first name\nor press enter for a random name:\n")   
    if not last_name: 
        last_name = random.choice(lnames)
    
    full_name = f"{first_name} {last_name}"




    def rand_alignment(alignments):
        """
        Generates a random alignment 
        """

        # Takes a random alignment from a set list
        alignment = random.choice(alignments)
        return f"{alignment}"
    
    # List of Alignments    
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
    
    # List of Races    
    races = ["Dragonborn", "Dwarf(Hill)", "Dwarf(Mountain)", 
    "Elf(Drow)", "Elf(High)", "Elf(Wood)", "Gnome(Forest)", 
    "Gnome(Rock)", "Half-Elf", "Half-Orc", "Halfling(Lightfoot)", 
    "Halfling(Stout)", "Human", "Tiefling"]

    # List of Classes ('occupation' used as class is a restricted keyword)
    occupations = ["Barbarian", "Bard", "Cleric", "Druid", 
    "Fighter", "Monk", "Paladin", "Ranger", "Rogue", 
    "Sorcerer", "Warlock", "Wizard"]

    race_occupation = rand_race_and_occupation(races, occupations)

    # Final print statement taking Name, Race, Occupation and Abilities
    print(f"Name: {full_name}\nRace/Class: {race_occupation}\nAbilities: {final_abilities}\nAlignment: {alignment}")

print(heading)
random_character = create_rand_character()


