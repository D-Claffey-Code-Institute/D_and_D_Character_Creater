"""Program to run a simple D and D character Creator."""
import random
import welcome


def create_rand_character():
    """
    Give ability to the user to pick a name or let a random one be choosen.

    Randomly assigns ability scores, race, class and alignment.
    """

    def rand_ability_scores():
        """
        Randonmly assigns a score to all abilities based an 3 d6 rolls.

        (a d6 is a six sided die).
        """
        abilities = {
            "Strenght": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0,
        }

        """
        Creates a list scores, generating a number between 1 and 6, 3 times.

        Sums the results and assigns them to each ability

        in the abilities dictionary.
        """
        for i in range(6):
            scores = [random.randint(1, 6) for x in range(3)]
            abilities[list(abilities.keys())[i]] = sum(scores)
        return abilities

    final_abilities = rand_ability_scores()

    def rand_name(fnames, lnames):
        """
        User to input their own name.

        Or generate a random name from
        a list of popular D and D names.
        """
        # Takes a random first and last name from a set list
        fname = random.choice(fnames)
        lname = random.choice(lnames)
        return f"{fname} {lname}"

    # List of random fantasy first names
    fnames = [
        "Bob",
        "Varis",
        "Nyx",
        "Luna",
        "Ash",
        "Jack",
        "Lilith",
        "Nix",
        "Zephyer",
        "Rhogar",
        "Cleric",
        "Bard",
        "Raven",
        "Ember",
        "Shadow",
    ]

    # List of random fantasy second names
    lnames = [
        "Lendor",
        "Etril",
        "Sakaris",
        "Witchelm",
        "Oskandor",
        "Edoril",
        "Sakaris",
        "Calmaria",
        "Lorvil",
        "Morningstar",
        "Caverns",
        "Thundershade",
        "Thalor",
        "Wildgrove",
        "Everflame",
    ]

    # User input for first name, allows letters and max lenght 10
    first_name = input("Enter your Characters first name\n"
                       "Letters Only and Max lenght 10 characters\n"
                       "Or press enter for a random name....\n")
    print("------------------------------------")

    while first_name:
        if not first_name.isalpha():
            print("Invalid input. Please enter letters only...")
            print("------------------------------------")
        elif len(first_name) > 10:
            print("Invalid input: Max characters is 10. Try again...")
            print("------------------------------------")
        else:
            break
        first_name = input(
            "Enter your Characters first name\n"
            "or press enter for a random name:\n"
        )
        print("------------------------------------")
    if not first_name:
        first_name = random.choice(fnames)

    # User input for last name, allows letters and max lenght 10
    last_name = input(
        "Enter your Characters last name\n"
        "Letters Only and Max lenght 10 characters\n"
        "Or press enter for a random name....\n"
    )
    print("------------------------------------")
    while last_name:
        if not last_name.isalpha():
            print("Invalid input. Please enter letters only...")
            print("------------------------------------")
        elif len(last_name) > 10:
            print("Invalid input: Max characters is 10. Try again...")
            print("------------------------------------")
        else:
            break
        last_name = input(
            "Enter your Characters last name\n"
            "or press enter for a random name:\n"
        )
        print("------------------------------------")
    if not last_name:
        last_name = random.choice(lnames)

    full_name = f"{first_name} {last_name}"

    def rand_alignment(alignments):
        """Generate a random alignment."""
        # Takes a random alignment from a set list
        alignment = random.choice(alignments)
        return f"{alignment}"

    # List of Alignments
    alignments = [
        "Lawful Good",
        "Neutral Good",
        "Chaotic Good",
        "Lawful Neutral",
        "True Neutral",
        "Chaotic Neutral",
        "Lawful Evil",
        "Neutral Evil",
        "Chaotic Evil",
    ]

    alignment = rand_alignment(alignments)

    def rand_race_and_occupation(races, occupations):
        """Generate a random race and class."""
        # Takes a random race and class from a set list
        race = random.choice(races)
        occupation = random.choice(occupations)
        return f"{race} {occupation}"

    # List of Races
    races = [
        "Dragonborn",
        "Dwarf(Hill)",
        "Dwarf(Mountain)",
        "Elf(Drow)",
        "Elf(High)",
        "Elf(Wood)",
        "Gnome(Forest)",
        "Gnome(Rock)",
        "Half-Elf",
        "Half-Orc",
        "Halfling(Lightfoot)",
        "Halfling(Stout)",
        "Human",
        "Tiefling",
    ]

    # List of Classes ('occupation' used as class is a restricted keyword)
    occupations = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard",
    ]

    race_occupation = rand_race_and_occupation(races, occupations)

    # Final print statement taking Name, Race, Occupation and Abilities

    print("------------------------------------")
    print(f"Name: {full_name}")
    print("                -----               ")
    print(f"Race/Class: {race_occupation}")
    print("                -----               ")
    print(f"Abilities: {final_abilities}")
    print("                -----               ")
    print(f"Alignment: {alignment}")
    print("------------------------------------")

    def repeat():
        repeat = input(
            "Would you like to create another character? type 'yes' or 'no':\n"
        )
        print("------------------------------------")
        while repeat:
            if not repeat.isalpha():
                print("Invalid input. Please enter only 'yes' or 'no'...")
                print("------------------------------------")
            elif repeat == "yes":
                print("------------------------------------")
                create_rand_character()
            elif repeat == "no":
                print("------------------------------------")
                print("Thanks for using my app")
                print("------------------------------------")
                exit()
            else:
                break

    repeat()


welcome.welcome()

create_rand_character()
