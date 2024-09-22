import random
import time


question_amounts = ["3", "4", "5"]
replay = "yes"
replay_options = ["yes", "y", "yip", "yeah", "ye"]
quit_options = ["no", "n", "nope", "nah"]


def wait_for_input(options, message):
    """
    Take all input from user for the details in the quiz.

    Data validation for the input given.
    User can just type the beggining of the word, not having to enter the whole thing.
    :param options: The available options for the user to enter
    :param message: The questions we want to ask the user for input
    """
    message = message.replace("%opts%", ", ".join(options))
    option = None
    while True:
        details = input(message).lower()
        if details == "exit":
            print()
            print("Well done on today's work! Thank you for using this quiz.")
            exit(1)
        # Make User able to only type what the words start with
        found = None
        for option in options:
            if option.lower().startswith(details):
                found = option
                break

        if not found:
            print("Please only enter what is offered.")
            time.sleep(1)
        else:
            return found


class subject():
    """This class is used for the subjects in the quiz"""

    def __init__(self, name):
        self.name = name
        self.sections = {}

    def add_section(self, section):
        self.sections[section.name] = section


class section():
    """This class is used for the sections in the quiz"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_random_question(self):
        unasked = []
        for question in self.questions:
            if not question.asked:
                unasked.append(question)
        if len(unasked) == 0:
            return None

        return random.choice(unasked)

    def reset_question(self):
        for question in self.questions:
            question.asked = False
            question.correct = False


class question():
    """This class is used for the questions in the quiz"""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.asked = False
        self.correct = False

    def is_choice_correct(self, choice):
        return (self.answer == choice)

    def mark_answer_correct(self):
        self.correct = True

    def ask_question(self):
        print(self.question)
        self.asked = True
        for choice, answer in self.choices.items():
            print(f"{choice}) {answer}")
        return wait_for_input(self.choices.keys(), "What is the correct answer? (%opts%) : ")

    def print_correct_answer(self):
        for choice, answer in self.choices.items():
            if self.is_choice_correct(choice):
                print(f"{choice}) {answer}")


# Questions for the subject Math
subjects = {}
subj = subject("mathematics")
subjects[subj.name] = subj
# Trig section questions
sect = section("trigonometry")
subj.add_section(sect)
quest = question(f"What do we call the angle that has the symbol, {chr(952)}? ",
                 {"A": "Hypotenuse", "B": "Theta", "C": f"180{chr(176)}", "D": "Opposite"}, "B")
sect.add_question(quest)
quest = question("What are the ratios we use in trigonometry?",
                 {"A": "sin, cos, tan", "B": "pythagorus, cos, sin", "C": "theta, opposite, adjacent"}, "A")
sect.add_question(quest)
quest = question("If I have the Hypotenuse and Theta, what would I use to find the adjacent side?",
                 {"A": "tan", "B": "sin", "C": "cos"}, "C")
sect.add_question(quest)
quest = question("What kind of triangle can I use Trigonometry in?",
                 {"A": "Isoceles triangle", "B": "Right angled triagle", "C": "Any triangle with a given side and angle"}, "B")
sect.add_question(quest)
quest = question(f"What is the equation, c{chr(178)} = a{chr(178)} + b{chr(178)}, used for? ",
                 {"A": "Volume", "B": "Surface Area", "C": "Triangles", "D": "Pythagorus' Therom"}, "D")
sect.add_question(quest)
quest = question(f"Find {chr(952)} in: tan{chr(952)} = 6/24",
                 {"A": "0.25", "B": "0", "C": "14"}, "C")
sect.add_question(quest)
quest = question(f"Find O in: sin(50{chr(176)}) = O/20",
                 {"A": "109", "B": "15", "C": "23", "D": "0"}, "B")
sect.add_question(quest)
quest = question(f"If the Hypotenuse is 12cm and Theta is 78{chr(176)}, what is the opposite side's length?",
                 {"A": "56.5cm", "B": "2.5cm", "C": "11.7cm", "D": "10.3cm"}, "C")
sect.add_question(quest)
quest = question("What is the length of the hypotenuse if the other two sides were 3cm and 4cm?",
                 {"A": "5cm", "B": "500mm", "C": "25cm", "D": "7cm"}, "A")
sect.add_question(quest)
quest = question(f"Find H in: cos(65{chr(176)}) = 3/H",
                 {"A": "3.3cm", "B": "7.1cm", "C": "1.3cm"}, "B")
# General math section questions
sect = section("General Mathematics")
subj.add_section(sect)
quest = question(f"find x in: x + 3 = 4 {chr(247)} 2",
                 {"A": "1", "B": "-1", "C": "5", "D": "0"}, "B")
sect.add_question(quest)
quest = question("15 is is equal to the sum of 3 consecutive numbers. What is the lowest consecutive number?",
                 {"A": "3", "B": "-3", "C": "+7", "D": "4"}, "D")
sect.add_question(quest)
quest = question("In a circle, what is a line from the centre to the circuference called? ",
                 {"A": "Radius", "B": "Diameter", "C": "Chord", "D": "Tangent"}, "A")
sect.add_question(quest)
quest = question("In a circle, what is a line that does not go through the centre called? ",
                 {"A": "Radius", "B": "Diameter", "C": "Chord", "D": "Tangent"}, "C")
sect.add_question(quest)
quest = question("How many meters are in 360cm?",
                 {"A": "0.36m", "B": "36 000m", "C": "3 600m", "D": "3.6m"}, "D")
sect.add_question(quest)
quest = question("How many centimeters are in 2.3m?",
                 {"A": "0.023cm", "B": "230cm", "C": "2300cm", "D": "0.23cm"}, "B")
sect.add_question(quest)
quest = question("If a cylinder has a volume of 200 and a height of 10, what is the radius of the cylinder?",
                 {"A": "4.6", "B": "12", "C": "2.5", "D": "5"}, "C")
# Questions for the subject Science
subj = subject("science")
subjects[subj.name] = subj
# Chemistry section questions
sect = section("chemistry")
subj.add_section(sect)
quest = question("What is an ion?",
                 {"A": "Another name for an atom", "B": "a charged particle", "C": "A compound"}, "B")
sect.add_question(quest)
quest = question("Name the 3rd element of the periodic table.",
                 {"A": "Hydrogen", "B": "Potassium", "C": "Lithium", "D": "Silver"}, "C")
sect.add_question(quest)
quest = question("What is the pH of neutral substances?",
                 {"A": "14", "B": "Green", "C": "7", "D": "3-4"}, "C")
sect.add_question(quest)
quest = question("Which subatomic particle is found in the nucleus and has a positive charge?",
                 {"A": "The atom", "B": "The proton", "C": "The electron", "D": "The neutron"}, "B")
sect.add_question(quest)
quest = question("What is the name of this polyatomic ion: OH-",
                 {"A": "Nitric acid", "B": "Hydroxide", "C": "Hydrogen sulfide", "D": "Sulfuric acid"}, "B")
sect.add_question(quest)
quest = question("What group does the element zinc belong to?",
                 {"A": "5", "B": "9", "C": "4", "D": "12"}, "D")
sect.add_question(quest)
quest = question("Describe the number and type of atoms in the compound 2Fe(NO^3)^3",
                 {"A": "6×Fe; 6×N; 6×O atoms", "B": "2×Fe; 6×N; 18×O atoms", "C": "2×Fe; 3×N; 9×O atoms"}, "B")
sect.add_question(quest)
quest = question("How many atoms are there in total in MgO?",
                 {"A": "1", "B": "2", "C": "3", "D": "4"}, "B")
sect.add_question(quest)
quest = question("How many atoms are on the product side in: Mg+CuSO^4 → Cu+MgSO^4",
                 {"A": "3", "B": "9", "C": "7", "D": "10"}, "C")
sect.add_question(quest)
quest = question("How many atoms are there on the reactants side in: NaOH+HCl → NaCl+H^2O",
                 {"A": "5", "B": "4", "C": "3", "D": "6"}, "A")
# Physics section questions
sect = section("physics")
subj.add_section(sect)
quest = question("What do you measure Volts with?",
                 {"A": "ammeter", "B": "voltmeter", "C": "circuit", "D": "cell"}, "B")
sect.add_question(quest)
quest = question("What is the symbol used for Current?",
                 {"A": "V", "B": "R", "C": "C", "D": "I"}, "D")
sect.add_question(quest)
quest = question("What is the unit of measurement for resistance?",
                 {"A": "ohms", "B": "amperes", "C": "volts"}, "A")
sect.add_question(quest)
quest = question("In two magnets, what will the south side of one do to the north side of the other?",
                 {"A": "Repel", "B": "Attract", "C": "All of the Above", "D": "Nothing"}, "B")
sect.add_question(quest)
quest = question("What do electrons do to other electrons?",
                 {"A": "Repel", "B": "Attract", "C": "All of the Above", "D": "Nothing"}, "A")
sect.add_question(quest)
quest = question("What do protons do to electrons?",
                 {"A": "Repel", "B": "Attract", "C": "All of the Above", "D": "Nothing"}, "B")
sect.add_question(quest)
quest = question("What is the formula we use to work out potential difference (in volts)?",
                 {"A": "V=I/R", "B": "V=P/C", "C": "V=IR", "D": "V=R/I"}, "C")
sect.add_question(quest)
quest = question("What is the formula we use to work out current?",
                 {"A": "V=I/R", "B": "V=P/C", "C": "I=V/R", "D": "V=R/I"}, "C")
sect.add_question(quest)
quest = question("What is the formula we use to work out resistance?",
                 {"A": "V=I/R", "B": "V=P/C", "C": "I=V/R", "D": "R=V/I"}, "D")

# Greet user and print introduction
print("Welcome to the year 11 quiz!")
time.sleep(1)
print("Here you can practice for your subjects at MAGS. You can practice for Math and Science.")
time.sleep(1)
print("If at anytime you would like to leave the quiz, please enter 'exit'.")
time.sleep(2)

# Start quiz loop
while replay in replay_options:
    # Take subject, section and the number of questions
    subject_options = subjects.keys()
    subject = wait_for_input(subject_options, f"Please enter your subject (%opts%): ")
    subj = subjects[subject]

    section_options = subj.sections.keys()
    section = wait_for_input(section_options, f"Please enter your section in {subj.name} (%opts%): ")
    sect = subj.sections[section]

    number_of_questions = int(wait_for_input(question_amounts, "How many questions would you like?(3 to 5): "))
    # Ask and mark the questions
    score = 0
    for question_number in range(number_of_questions):
        quest = sect.get_random_question()
        # Check if user has answered all the questions
        if quest is None:
            print("All questions in this section have been asked!")
            time.sleep(1)
            ask_again = wait_for_input(replay_options + quit_options,f"Do you want to be asked the questions again in {section}? ")
            if ask_again in replay_options:
                sect.reset_question()
                quest = sect.get_random_question()
            else:
                break
        # Mark the questions
        if quest is not None:
            choice = quest.ask_question()
            if quest.is_choice_correct(choice):
                quest.mark_answer_correct()
                print("Correct!")
                score += 1
            else:
                print("Incorrect, the correct answer is")
                quest.print_correct_answer()
            print()
            time.sleep(1)

    # All the users questions have been answered
    if quest is not None:
        print(f"Well done! You've answered all {number_of_questions} of your questions.")
        percent = score * 100 / number_of_questions
        print(f"You got {score} out of {number_of_questions} correct, {percent:.2f}%")

        if score < number_of_questions/2:
            print("Better luck next time!")
        else:
            print("Good Job!")

    time.sleep(2)
    # Check if user wants to continue
    replay = wait_for_input(replay_options + quit_options, "Would you like more practice with another quiz? ")
    if replay in quit_options:
        time.sleep(1)
        total_questions_asked = 0
        total_questions_correct = 0
        for subj in subjects.values():
            for section, sect in subj.sections.items():
                num_asked_sect = 0
                num_correct_sect = 0
                for question in sect.questions:
                    if question.asked:
                        total_questions_asked += 1
                        num_asked_sect += 1
                        if question.correct:
                            total_questions_correct += 1
                            num_correct_sect += 1

                if num_asked_sect > 0:
                    print(f"You got {num_correct_sect} out of {num_asked_sect} correct in {section}")
        # Exit program and give the users final percentage
        percent = total_questions_correct * 100 / total_questions_asked
        print(f"You got a total of {percent:.2f}% for all your questions.")
        time.sleep(1)
        print("We hope this has helped you, you can always come back for more practice later!")
        print("Thank you for using our quiz :)")
        exit(1)
