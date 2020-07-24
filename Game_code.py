#TO DO LIST:
#Finish classes
#Finish leveling up
#finish charater sheet display
#finish races
#add notes

#Primary Character Stats
import time
import string
import sys
#This is for the characters base stats
var_charpoints = 72
var_strength = 0
var_dexterity = 0
var_constitution = 0
var_intelligence = 0
var_wisdom = 0
var_charisma = 0
#Name
charName = ""
#Race
Race = ""
#Class
Class = ""
#Alignment
Alignment = ""
#Level
Level = 1
#current XP(start)
PlayerXP = 0
#Required XP (Level 1)
RequiredXP = 100
#These are for the bonuses you get for each race
HumanBonus = 1
ElfBonus = 2
HighBonus = 1
WoodBonus = 1
DarkBonus = 1
ProfBonus = 2
#These are the stat values 
StrengthBonus = 0
DextrityBonus = 0
ConstitutionBonus = 0
InteleganceBonus = 0
WisdomBonus = 0
CharismaBonus = 0
#These are the saving throws
SaveStrength = 0
SaveDexterity = 0
SaveConstitution = 0
SaveIntelegence = 0
SaveWisdom = 0
SaveCharisma = 0
#These are all of the abilities
SkillAcrobatics = 0
SkillAnimalHandling = 0
SkillArcana = 0
SkillAthlectics = 0
SkillDeception = 0
SkillHistory = 0
SkillInsight = 0
Skillintimidation = 0
SkillInvestigation = 0
SkillMedicine = 0
SkillNature = 0
SkillPerception = 0
SkillPerformance = 0
SkillPersuation = 0
SkillReligion = 0
SkillSlightOfHand = 0
SkillStealth = 0
SkillSurvival = 0
#These are Proficiencies for saving throws
SaveStrengthProf = 0
SaveDexterityProf = 0
SaveConstitutionProf = 0
SaveIntelegenceProf = 0
SaveWisdomProf = 0
SaveCharismaProf = 0
#These are proficiencies for abilities
SkillAcrobaticsProf = 0
SkillAnimalHandlingProf = 0
SkillArcanaProf = 0
SkillAthlecticsProf = 0
SkillDeceptionProf = 0
SkillHistoryProf = 0
SkillInsightProf = 0
SkillintimidationProf = 0
SkillInvestigationProf = 0
SkillMedicineProf = 0
SkillNatureProf = 0
SkillPerceptionProf = 0
SkillPerformanceProf = 0
SkillPersuationProf = 0
SkillReligionProf = 0
SkillSlightOfHandProf = 0
SkillStealthProf = 0
SkillSurvivalProf = 0
#litterally irrelevent
chosen = 0

#Race selection
def start():
    print("""
    welcome to dungeons and dragons 5.5e
    to start please choose a race:
    1. Human
    2. Elf
    Please write in your preferd race"""
    )
    global Race
    race = input(str())
    race = race.lower()
    Race = race
    time.sleep(1)
    if True:
        #Taking the player to their selected race function
        #Elf
        if Race == "elf":
            print("Elf has been selected, here is your race preview.")
            time.sleep(1)
            Elf()
        #Human
        elif Race == "human":
            print("Human has been selected, here is your race preview....")
            time.sleep(1)
            Human()
        #Wrong   
        else:
            print("An eroor has occored, this selection is not in our system, please try again.")
            time.sleep(1)
            start()
#Elf stats
def Elf():
    """This is the Elf race"""
    print("welcome Elf, here are your starting abilities.")
    print("with Elf you get +2 to your dexterity")
    time.sleep(1)
    #confirming race selection
    print("Do you want to continue as an elf, remeber you can not change your mind after.")
    go1 = input(str())
    go1 = go1.lower()
    time.sleep(1)
    #yes
    if go1 == "yes":
        print("Welcome to the Elf race, you now have a few more things to decide.")
        global var_dexterity
        global ElfBonus 
        var_dexterity = var_dexterity + ElfBonus #changing dex score
        print("Now to choose your sub-class")
        time.sleep(1)
        ElfSub()  #taking the user to the sub class function 
        time.sleep(1)
        fun_charcreator()
    #no
    elif go1 == "no":
        print("okay, come back if you change your mind")
        time.sleep(1)
        Start()
    #Wrong
    else:
       print("well that just wasnt nessisary now was it")
       time.sleep(1)
       Elf()

#human stats
def Human():
    """THIS is the Human race"""
    print("Welcome Human, here are your starting abilities.")
    print("with Human you get +1 to all your stats")
    time.sleep(1)
    #confirming race selection
    print("Do you want to continue as a Human, remember you can not change your mind after.")
    go2 = input(str())
    go2 = go2.lower()
    time.sleep(1)
    #yes
    if go2 == "yes":
        print("Welcome to the Human race, heres the Human view on the world and the other races:")
        global HumanBonus
        global charName
        global var_strength
        global var_dexterity
        global var_constitution
        global var_intelligence
        global var_wisdom
        global var_charisma
        #changing ablility scores
        var_strength = var_strength + HumanBonus
        var_dexterity = var_dexterity + HumanBonus
        var_constitution = var_constitution + HumanBonus
        var_intelligence = var_intelligence + HumanBonus
        var_wisdom = var_wisdom + HumanBonus
        var_charisma = var_charisma + HumanBonus
        time.sleep(1)
        fun_charcreator()
    #No 
    elif go2 == "no":
        print("okay, come back if you change your mind")
        time.sleep(1)
        start()
    #Wrong
    else:
        print("well that just wasnt nessisary now was it")
        time.sleep(1)
        start()



#Giving player stats
def fun_charcreator():
    global var_strength
    global var_dexterity
    global var_constitution
    global var_intelligence
    global var_wisdom
    global var_charisma
    global var_charpoints
    #finding which stat they want to change
    print("           ")
    print("It is now time to decide your stats")
    print("Your character has ",var_charpoints," points left")
    print("str for strength,     current: ", var_strength)
    print("dex for dexterity,    current: ", var_dexterity)
    print("con for constitution, current: ", var_constitution)
    print("int for intelligence, current: ", var_intelligence)
    print("wis for wisdom,       current: ", var_wisdom)
    print("cha for charisma,     current: ", var_charisma)
    print("finish for when you are done ! ")
    print("              ")
    time.sleep(1)
    var_charstat = input(str("Choose first stat then select how many points to add, note it cannot be lower than 6 or higher than 20!"))
    var_charstat = var_charstat.lower()
    time.sleep(1)
    print("you have chosen: ",var_charstat)
    #I need to copy paste this for all of the stats. '#This was your note and idk what it means
    
    #Strength
    if var_charstat == "str":
        print("Current strength = ",var_strength)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_strength< 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_strength
            var_charpoints = var_charpoints - var_newstat
            var_strength = var_newstat
            time.sleep(1)
            fun_charcreator()
    #Dexterity
    elif var_charstat == "dex":
        print("Current dexterity = ",var_dexterity)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_dexterity< 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_dexterity
            var_charpoints = var_charpoints - var_newstat
            var_dexterity = var_newstat
            time.sleep(1)
            fun_charcreator()
    #Constitution
    elif var_charstat == "con":
        print("Current constitution = ",var_constitution)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_constitution < 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_constitution
            var_charpoints = var_charpoints - var_newstat
            var_constitution = var_newstat
            time.sleep(1)
            fun_charcreator()
    #Intelligence
    elif var_charstat == "int":
        print("Current intelligence = ",var_intelligence)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_intelligence < 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_intelligence
            var_charpoints = var_charpoints - var_newstat
            var_intelligence = var_newstat
            time.sleep(1)
            fun_charcreator()
    #Wisdom
    elif var_charstat == "wis":
        print("Current wisdom = ",var_wisdom)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_wisdom < 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_wisdom
            var_charpoints = var_charpoints - var_newstat
            var_wisdom = var_newstat
            time.sleep(1)
            fun_charcreator()
    #Charisma
    elif var_charstat == "cha":
        print("Current charisma = ",var_charisma)
        print("Please select no. of points")
        var_newstat = int(input("New Points: "))
        if var_newstat < 6 or var_newstat > 20 or var_charpoints - var_newstat + var_charisma < 0:
            print("Number not possible, retry")
            time.sleep(1)
            fun_charcreator()
        else:
            var_charpoints = var_charpoints + var_charisma
            var_charpoints = var_charpoints - var_newstat
            var_charisma = var_newstat
            time.sleep(1)
            fun_charcreator()

    #Finish
    elif var_charstat == "finish":
        Proficiency()

    #wrong 
    else:
        print("Invalid input detected")
        time.sleep(1)
        fun_charcreator()


def Proficiency():
    global SaveStrengthProf 
    global SaveDexterityProf 
    global SaveConstitutionProf 
    global SaveIntelegenceProf 
    global SaveWisdomProf 
    global SaveCharismaProf 
    global SkillAcrobaticsProf
    global SkillAnimalHandlingProf 
    global SkillArcanaProf 
    global SkillAthlecticsProf 
    global SkillDeceptionProf 
    global SkillHistoryProf 
    global SkillInsightProf
    global SkillintimidationProf 
    global SkillInvestigationProf 
    global SkillMedicineProf 
    global SkillNatureProf 
    global SkillPerceptionProf
    global SkillPerformanceProf
    global SkillPersuationProf 
    global SkillReligionProf 
    global SkillSlightOfHandProf 
    global SkillStealthProf 
    global SkillSurvivalProf
    global chosen
    print("now for your proficiencies")
    while chosen < 3:
        print("""pick 3 of the following to be proficient in:
        acrobatics, animal handeling, arcarna, athletics, deception, history,
        insight, intimidation, investigation, medicine, nature, perception,
        performance, persuation, relegion, slight of hand, stealth, survival""")
        print("Please write the name of your chosen proficeny")
        prof1 = input(str())
        prof1 = prof1.lower()
        if prof1 == "acrobatics":
            print("acrobatics selected")
            if SkillAcrobaticsProf == 2:
                print("cannot double proficency")
            else:
                SkillAcrobaticsProf = SkillAcrobaticsProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "animal handeling":
            print("animaql handeling selected")
            if SkillAnimalHandlingProf == 2:
                print("cannot double proficency")
            else:
                SkillAcrobaticsProf = ProfBonus + SkillAcrobaticsProf
                print("proficeny added")
                chosen = chosen + 1
        elif prof1 == "arcarna":
            print("arcarna selected")
            if SkillArcanaProf == 2:
                print("Cannot double proficency")
            else:
                SkillArcanaProf = SkillArcanaProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "athletics":
            print("Athletics selected")
            if SkillAthlecticsProf == 2:
                print("Cannot double proficency")
            else:
                SkillAthlecticsProf = SkillAthlecticsProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "deception":
            print("Deception selected")
            if SkillDeceptionProf == 2:
                print("Cannot double proficency")
            else:
                SkillDeceptionProf =  SkillDeceptionProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "history":
            print("History selected")
            if SkillHistoryProf == 2:
                print("Cannot double proficency")
            else:
                SkillHistoryProf = SkillHistoryProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "insight":
            print("Insight selected")
            if SkillInsightProf == 2:
                SkillInsightProf = SkillInsightProf + ProfBonus
                print("Cannot double proficency")
            else:
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "investigation":
            print("Investigation selected")
            if SkillInvestigationProf == 2:
                print("Cannot double proficency")
            else:
                SkillInvestigationProf = SkillInvestigationProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "investigation":
            print("Investigation selected")
            if SkillInvestigationProf == 2:
                print("Cannot double proficency")
            else:
                SkillInvestigationProf = SkillInvestigationProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "medicine":
            print("Medicine selected")
            if SkillMedicineProf == 2:
                print("Cannot double proficency")
            else:
                SkillMedicineProf = SkillMedicineProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "nature":
            print("Nature selected")
            if SkillNatureProf == 2:
                print("Cannot double proficency")
            else:
                SkillNatureProf = SkillNatureProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "perception":
            print("Perception selected")
            if SkillProf == 2:
                print("Cannot double proficency")
            else:
                SkillPerceptionProf = SkillPerceptionProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "performance":
            print("Performance selected")
            if SkillPerformanceProf == 2:
                print("Cannot double proficency")
            else:
                SkillPerformanceProf = SkillPerformanceProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "persuasion":
            print("Persuasion selected")
            if SkillPersuationProf == 2:
                print("Cannot double proficency")
            else:
                print("proficency added")
                SkillPersuationProf = SkillPersuationProf + ProfBonus
                chosen = chosen + 1
        elif prof1 == "religion":
            print("Religion selected")
            if SkillReligionProf == 2:
                print("Cannot double proficency")
            else:
                SkillReligionProf = SkillReligionProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "slight of hand":
            print("Slight of hand selected")
            if SkillSlightOfHandProf == 2:
                print("Cannot double proficency")
            else:
                SkillSlightOfHandProf = SkillSlightOfHandProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        elif prof1 == "stealth":
            print("Stealth selected")
            if SkillStealthProf == 2:
                print("Cannot double proficency")
            else:
                print("proficency added")
                SkillStealthProf = SkillStealthProf + ProfBonus
                chosen = chosen + 1
        elif prof1 == "survival":
            print("Survival selected")
            if SkillSurvivalProf == 2:
                print("Cannot double proficency")
            else:
                SkillSurvivalProf = SkillSurvivalProf + ProfBonus
                print("proficency added")
                chosen = chosen + 1
        #wrong 
        else:
            print("Invalid input detected")
            time.sleep(1)
            Proficiency()
    print("Character creation finished...")
    time.sleep(1)
    print("Calculating sencondary stats...")
    global SaveStrength
    global SaveDexterity
    global SaveConstitution
    global SaveIntelegence
    global SaveWisdom
    global SaveCharisma
    global SkillAcrobatics
    global SkillAnimalHandling
    global SkillArcana
    global SkillAthlectics
    global SkillDeception
    global SkillHistory
    global SkillInsight
    global Skillintimidation
    global SkillInvestigation
    global SkillMedicine
    global SkillNature
    global SkillPerception
    global SkillPerformance
    global SkillPersuation
    global SkillReligion
    global SkillSlightOfHand
    global SkillStealth
    global SkillSurvival
    global StrengthBonus
    global DexterityBonus
    global ConstitutionBonus
    global IntelecenceBonus
    global WisdomBonus
    global CharismaBonus
    if var_strength == 6 or 7:
        StrengthBonus = -2
    elif var_strength == 8 or 9:
        StrengthBonus = -1
    elif var_strength == 10 or 11:
        StrengthBonus = 0
    elif var_strength == 12 or 13:
        StrengthBonus = 1
    elif var_strength == 14 or 15:
        StrengthBonus = 2
    elif var_strength == 16 or 17:
        StrengthBonus = 3
    elif var_strength == 18 or 19:
        StrengthBonus = 4
    elif var_strength == 20:
        StrengthBonus = 5
    if var_dexterity == 6 or 7:
        DexterityBonus = -2
    elif var_dexterity == 8 or 9:
        DexterityBonus = -1
    elif var_dexterity == 10 or 11:
        DexterityBonus = 0
    elif var_dexterity == 12 or 13:
        DexterityBonus = 1
    elif var_dexterity == 14 or 15:
        DexterityBonus = 2
    elif var_dexterity == 16 or 17:
        DexterityBonus = 3
    elif var_dexterity == 18 or 19:
        DexterityBonus = 4
    elif var_dexterity == 20:
        DexterityhBonus = 5
    if var_charisma == 6 or 7:
        CharismaBonus = -2
    elif var_charisma == 8 or 9:
        CharismaBonus = -1
    elif var_charisma == 10 or 11:
        CharismaBonus = 0
    elif var_charisma == 12 or 13:
        CharismaBonus = 1
    elif var_charisma == 14 or 15:
        CharismaBonus = 2
    elif var_charisma == 16 or 17:
        CharismaBonus = 3
    elif var_charisma == 18 or 19:
        CharismaBonus = 4
    elif var_charisma == 20:
        CharismaBonus = 5
    if var_constitution == 6 or 7:
        StrengthBonus = -2
    elif var_constitution == 8 or 9:
        ConstitutionBonus = -1
    elif var_constitution == 10 or 11:
        ConstitutionBonus = 0
    elif var_constitution == 12 or 13:
            ConstitutionBonus = 1
    elif var_constitution == 14 or 15:
        ConstitutionBonus = 2
    elif var_constitution == 16 or 17:
        ConstitutionBonus = 3
    elif var_constitution == 18 or 19:
        ConstitutionBonus = 4
    elif var_constitution == 20:
        ConstitutionBonus = 5
    if var_wisdom == 6 or 7:
        WisdomBonus = -2
    elif var_wisdom == 8 or 9:
        WisdomBonus = -1
    elif var_wisdom == 10 or 11:
        WisdomBonus = 0
    elif var_wisdom == 12 or 13:
        WisdomBonus = 1
    elif var_wisdom == 14 or 15:
        WisdomBonus = 2
    elif var_wisdom == 16 or 17:
        WisdomBonus = 3
    elif var_wisdom == 18 or 19:
        WisdomBonus = 4
    elif var_wisdom == 20:
        WisdomBonus = 5
    if var_intelligence == 6 or 7:
        IntelegenceBonus = -2
    elif var_intelligence == 8 or 9:
        IntelegenceBonus = -1
    elif var_intelligence == 10 or 11:
        IntelegenceBonus = 0
    elif var_intelligence == 12 or 13:
        IntelegenceBonus = 1
    elif var_intelligence == 14 or 15:
        IntelegenceBonus = 2
    elif var_intelligence == 16 or 17:
        IntelegenceBonus = 3
    elif var_intelligence == 18 or 19:
        IntelegenceBonus = 4
    elif var_intelligence == 20:
        IntelegenceBonus = 5
    SaveStrength = SaveStrength + StrengthBonus + SaveStrengthProf
    SaveCharisma = SaveCharisma + CharismaBonus + SaveCharismaProf
    SaveConstitution = SaveConstitution + ConstitutionBonus + SaveConstitutionProf
    SaveDexterity = SaveDexterity + DexterityBonus + SaveDexterityProf
    SaveIntelegence = SaveIntelegence + InteleganceBonus + SaveIntelegenceProf
    SaveWisdom = SaveWisdom + WisdomBonus + SaveWisdomProf
    SkillAcrobatics = SkillAcrobatics + DexterityBonus + SkillAcrobaticsProf
    SkillAnimalHandling = SkillAnimalHandling + WisdomBonus + SkillAnimalHandlingProf
    SkillArcana = SkillArcana + InteleganceBonus + SkillArcanaProf
    SkillAthlectics = SkillAthlectics + StrengthBonus + SkillAthlecticsProf
    SkillDeception = SkillDeception + CharismaBonus + SkillDeceptionProf
    SkillHistory = SkillHistory + InteleganceBonus + SkillHistoryProf
    SkillInsight =  SkillInsight + WisdomBonus + SkillInsightProf
    Skillintimidation = Skillintimidation + CharismaBonus + SkillintimidationProf
    SkillInvestigation = Skillintimidation + InteleganceBonus + SkillInvestigationProf
    SkillMedicine = SkillMedicine + WisdomBonus + SkillMedicineProf
    SkillNature = SkillNature + InteleganceBonus + SkillNatureProf
    SkillPerception = SkillPerception + WisdomBonus + SkillPerceptionProf
    SkillPerformance = SkillPerformance + CharismaBonus + SkillPerformanceProf
    SkillPersuation = SkillPersuation + CharismaBonus + SkillPersuationProf
    SkillReligion = SkillReligion + InteleganceBonus + SkillReligionProf
    SkillSlightOfHand = SkillSlightOfHand + DexterityBonus + SkillSlightOfHandProf
    SkillStealth = SkillStealth + DexterityBonus + SkillStealthProf
    SkillSurvival = SkillSurvival + WisdomBonus +SkillSurvivalProf

    time.sleep(1)
    print("Stats calculated.")
    fun_charsheet()


def ElfSub():

    print("""you have 3 options:
    1.High Elf
    2.Wood Elf
    3.Dark Elf(Drow)
    """)
    print("please input the number of your sub-class")
    elfSub = int(input())
    if elfSub == 1:
        print("You have selected the High Elf")
        print("This subclass gives you +1 to your intelegance")
        time.sleep(1)
        print("would you like to continue as a High Elf")
        go3 = input(str())
        go3 = go3.lower()
        if go3 == "yes":
            print("Welcome High Elf.")
            global HighBonus
            global var_intelligence
            var_intelligence = var_intelligence + HighBonus
        elif go3 == "no":
            print("okay see come back soon")
            time.sleep(1)
            ElfSub()
        else:
            print("well thats just not what i asked")
            time.sleep(1)
            ElfSub()
    elif elfSub == 2:
        print("You have selected the Wood Elf")
        print("The Wood Elf gives you +1 to your wisdom")
        time.sleep(1)
        print("would you like to choose Wood Elf")
        go4 = input(str())
        go4 = go4.lower()
        if go4 == "yes":
            print("Welcome Wood Elf")
            global WoodBonus
            global var_wisdom
            var_wisdom = var_wisdom + WoodBonus

    elif elfSub == 3:
        print("You have selected the Dark Elf(Drow)")
        print("Drow gives you +1 to your charisma")
        time.sleep(1)
        print("would you like to continue as Drow")
        go5 = input(str())
        go5 = go5.lower()
        if go5 == "yes":
            print("welcome to Drown race")
            global DarkBonus
            global var_charisma
            var_charisma = var_charisma + DarkBonus
        elif go5  == "no":
            print("okay come back soon")
            time.sleep(1)
            ElfSub()
        else:
            print("not an option bucko")
            time.sleep(1)
            ElfSub()
            
    else:
        print("That is not one of our sub-classes")
        time.sleep(1)
        ElfSub()

def charName():
    global charName
    print("it is now time to choose what your charicacter will be called for the rest of the game")
    time.sleep(1)
    print("please enter characters first name")
    name1 = input()
    time.sleep(1)
    print("please input your charactoers second name")
    name2 = input()
    time.sleep(1)
    charName = name1 + " " + name2
    print("Your characters name is", charName)
    print("    ")

def Align():
    print("It is time to choose an alignment")
    print("Your alinment effects your options in every situation and how other characters will act around you")
    print("""
    To start you have 3 options:
    1. Lawful
    2. Nutrual
    3. Chotic
    """)
    print("please wirte the name of your prefered alignment")
    print("    ")
    align1 = input(str())
    align1 = align1.lower()
    time.sleep(1)
    if align1 == "lawful":
        print("You have chosen to be Lawful")
        print("This means...")
        align1 = "L"
        print("    ")
        time.sleep(1)
        print("now for your next 3")
        print("""
        your nest 3 options are:
        1. good
        2. nutrual
        3. evil
        """)
        print("Please write the name of your preferd alignment")
        print("    ")
        align2 = input(str())
        align2 = align2.lower()
        time.sleep(1)
        if align2 == "good":
            print("you have chosen to be Good")
            print("this means...")
            align2 = "G"
            time.sleep(1)
        elif align2 == "nutrual":
            print("you have chosen to be nutrual")
            print("this means...")
            align2 = "N"
            time.sleep(1)
        elif align2 == "evil":
            print("you have chosen to be evil")
            print("this means...")
            align2  = "E"
            time.sleep(1)
        else:
            print("this isnt one of our alignmeants, try again.")
            time.sleep(1)
            Align()
    elif align1 == "nutrual":
        print("You have chosen to be Nutrual")
        print("this means...")
        align1 = "N"
        print("    ")
        time.sleep(1)
        print("now for your next 3")
        print("""
        your nest 3 options are:
        1. good
        2. nutrual
        3. evil
        """)
        print("Please write the name of your preferd alignment")
        print("    ")
        align2 = input(str())
        align2 = align2.lower()
        time.sleep(1)
        if align2 == "good":
            print("you have chosen to be Good")
            print("this means...")
            align2 = "G"
            time.sleep(1)
        elif align2 == "nutrual":
            print("you have chosen to be nutrual")
            print("this means...")
            align2 = "N"
            time.sleep(1)
        elif align2 == "evil":
            print("you have chosen to be evil")
            print("this means...")
            align2  = "E"
            time.sleep(1)
        else:
            print("this isnt one of our alignmeants, try again.")
            time.sleep(1)
            Align()
    elif align1 == "chotic":
        print("You have chosen to be choctic")
        print("this means...")
        align1 = "C"
        print("    ")
        time.sleep(1)
        print("now for your next 3")
        print("""
        your nest 3 options are:
        1. good
        2. nutrual
        3. evil
        """)
        print("Please write the name of your preferd alignment")
        print("    ")
        align2 = input(str())
        align2 = align2.lower()
        time.sleep(1)
        if align2 == "good":
            print("you have chosen to be Good")
            print("this means...")
            align2 = "G"
            time.sleep(1)
        elif align2 == "nutrual":
            print("you have chosen to be nutrual")
            print("this means...")
            align2 = "N"
            time.sleep(1)
        elif align2 == "evil":
            print("you have chosen to be evil")
            print("this means...")
            align2  = "E"
            time.sleep(1)
        else:
            print("this isnt one of our alignmeants, try again.")
            time.sleep(1)
            Align()
    else:
        print("this was not one of the options, you shall now start the prosses over")
        time.sleep(1)
        Align()
    global Alignment
    Alignment = align1 + align2
    print("your chosen alignment is", Alignment)
    print("                                  ")
    time.sleep(1)
    sys.exit

def FunClass():
    print("welcome to class selection")
    print("""
    Please choose one of the following:
    !. Fighter
    2. Rogue
    Please enter the name of your prefered class""")
    VarClass = input(str())
    VarClass = VarClass.lower()
    if VarClass == "fighter":
        print("You have chosen Fighter class")
        print("fighter gives you these benefits....")#continue the fighter benefits
        print("would you liike to continue as a Fighter?")
        go6 = input(str())
        go6 = go6.lower()
        if go6 == "yes":
            global Class
            print("Welcome fighter")
            Class = "Fighter"
            print("             ")
            sys.exit
        elif go6 == "no":
            print("okay return if you change your mind")
            time.sleep(1)
            FunClas()
        else:
            print("not an option, try again")
            time.sleep(1)
            FunClass()
    elif VarClass == "rogue":
        print("You have chosen Rogue class")
        print("Rogue gives you these benefits.....")#continue rogue benefits
        print("Would you like to continue as a Rogue")
        go7 = input(str())
        go7 = go7.lower()
        if go7 == "yes":
            print("welcome to the Rogue class")
            Class = "Rogue"
            print("                  ")
            sys.exit
        elif go7 == "no":
           print("okay, return if you change your mind")
           time.sleep(1)
           FunClass()
        else:
            print("not an option, try again")
            time.sleep(1)
            FunClass()


            
#Finish #####'#############################################################################################################
def finChar():
    global var_strength
    global var_dexterity
    global var_constitution
    global var_intelligence
    global var_wisdom
    global var_charisma
    global charNmae
    global Race
    global Class
    global Alignment
    global HumanBonus
    global ElfBonus 
    global HighBonus
    global WoodBonus
    global DarkBonus
    global SaveStrength
    global SaveDexterity
    global SaveConstitution
    global SaveIntelegence
    global SaveWisdom
    global SaveCharisma
    global SkillAcrobatics
    global SkillAnimalHandling
    global SkillArcana
    global SkillAthlectics
    global SkillDeception
    global SkillHistory
    global SkillInsight
    global Skillintimidation
    global SkillInvestigation
    global SkillMedicine
    global SkillNature
    global SkillPerception
    global SkillPersuation
    global SkillReligion
    global SkillSlightOfHand
    global SkillStealth
    global SkillSurvival
    print("""
    please choose what you would like to look at:
    1.Name
    2.Race
    3.Class
    4.Base Stats
    5.Skills
    6.Saving throws
    please enter the number that you would like
    """)
    select = int(input())
    if select == 1:
        print(charName)
        time.sleep(1)
        finChar()
    elif select == 2:
        print(Race)
        time.sleep(1)
        finChar()
    elif select == 3:
        print(Class)
        time.sleep(1)
        finChar()
    elif select == 4:
        print(var_strength)
        print(var_dexterity)
        print(var_constitution)
        print(var_intelligence)
        print(var_wisdom)
        print(var_charisma)
        time.sleep(3)
        finChar()
    elif select == 5:
        print(SkillAcrobatics)
        print(SkillAnimalHandling)
        print(SkillArcana)
        print(SkillAthlectics)
        print(SkillDeception)
        print(SkillHistory)
        print(SkillInsight)
        print(Skillintimidation)
        print(SkillInvestigation)
        print(SkillMedicine)
        print(SkillNature)
        print(SkillPerception)
        print(SkillPersuation)
        print(SkillReligion)
        print(SkillSlightOfHand)
        print(SkillStealth)
        print(SkillSurvival)
        time.sleep(4)
        finChar()
    elif select == 6:
        print(SaveStrength)
        print(SaveDexterity)
        print(SaveConstitution)
        print(SaveIntelegence)
        print(SaveWisdom)
        print(SaveCharisma)
        time.sleep(3)
        finChar()
    elif select == 7:
        print("Returning to story")
        time.sleep(1)
        sys.exit 
    else:
        print("that wasn't an option")
        finChar()


def fun_charsheet():
    print("Welcome to your character, time to finish the details")
    print("lets start with a name")
    time.sleep(1)
    charName()
    print("Now for your alignment")
    time.sleep(1)
    Align()
    print("Finally, your class")
    time.sleep(1)
    FunClass()
    print("here is your finished character")
    time.sleep(1)
    finChar()
    print("""If you would like to look at your character sheet during the story, just type "character sheet" """)

def Control():
    global PlayerXP
    global RequiredXP
    global Level 
    if PlayerXP >= RequiredXP:
        print("Good Job you are now level", Level)
        Level = Level + 1
        if Level == 2:
            Level2()
        elif Level == 3:
            Level3()
        elif Level == 4:
            Level4
    else:
        sys.exit

def Level2():
    global RequiredXP
    RequiredXP = 400
    sys.exit

start()


