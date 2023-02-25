import random

template = random.randrange(1, 4, 1)

if template == 1:
    number = input("Input a number: ")
    measureOfTime = input("Input meausure of Time: ")
    modeOfTransportation = input("Input mode of Transportation: ")
    adjective = input("Input adjective: ")
    adjective2 = input("Input adjective: ")
    noun = input("Input a noun: ")
    color = input("Input a color: ")
    partOfTheBody = input("Input part of the body: ")
    verb = input("Input a verb: ")
    number2 = input("Input a number: ")
    noun2 = input("Input a noun: ")
    noun3 = input("Input a noun: ")
    partOfTheBody2 = input("Input part of the body: ")
    verb = input("Input a verb: ")
    noun4 = input("Input a noun: ")
    adjective3 = input("Input adjective: ")
    sillyWord = input("Input a silly word: ")
    noun5 = input("Input noun: ")
    
    aOrAn = 'a'
    vowels = "aieou"
    if adjective[0] in vowels:
        aOrAn = "an"
    
    print(f"It was about {number} {measureOfTime} ago when I arrived at the hospital in a {modeOfTransportation}.",
        f"The hospital is {aOrAn} {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {partOfTheBody}.",
        f"If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number} {noun2}."
        f"Today I talked to a doctor and they were wearing a {noun3} on their {partOfTheBody2}. I heard that all doctors {verb} {noun4} every day for breakfast.",
        f"The most {adjective3} thing about being in the hospital is the {sillyWord} {noun5} !")

elif template == 2:
    name = input("Input a person’s name: ")
    noun1 = input("Input noun: ")
    adjective = input("Input adjective (feeling): ")
    verb1 = input("Input a verb: ")
    adjective2 = input("Input adjective (feeling): ")
    animal = input("Input an animal: ")
    verb2 = input("Input a verb: ")
    color1 = input("Input a color: ")
    verb3 = input("Input a verb + ing: ")
    adverb = input("Input a adverb + ly: ")
    number = input("Input a number: ")
    time = input("Input measure of time: ")
    color2 = input("Input a color: ")
    animal2 = input("Input an animal: ")
    number2 = input("Input a number: ")
    silly = input("Input a silly word: ")
    noun2 = input("Input a noun: ")
    
    aOrAn = 'a'
    vowels = "aieou"
    if animal[0] in vowels:
        aOrAn = "an"
      
    print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb1} in a tent.",
        f"I am {adjective2} we might see {aOrAn} {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}.",
        f"I have heard that the {color1} lake is great for {verb3}. Then we will {adverb} hike through the forest for {num1} {time}.",
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {num2} {silly} stories and roast {noun2} around the campfire!!")
        

elif template == 3:
    personsName = input("Input person's name: ")
    castlesName = input("Input adjective: ")
    colorForAnimal = input("Input a color for animal: ")
    animal = input("Input an animal: ")
    place = input("Input place: ")
    adjective = input("Input adjective: ")
    magicalCreatures1 = input("Input an example of magical creature (in plural form): ")
    adjective2 = input("Input adjective: ")
    magicalCreatures2 = input("Input an example of magical creature (in plural form): ")
    room = input("Input a room(name) in a house: ")
    noun = input("Input noun: ")
    noun2 = input("Input another noun: ")
    noun3 = input("Input noun(in plural form): ")
    dream = input("Input adjective: ")
    noun4 = input("Input noun(in plural form): ")
    number = input("Input a number: ")
    measure = input("Measure of the time: ")
    verb = input("Input a verb + ing: ")
    adjLast = input("Input adjective: ")
    noun5 = input("Input a noun: ")
    
    print(f"Dear {personsName},  I am writing to you from a {castlesName} castle in an enchanted forest. I found myself here one day after going for a ride on a {colorForAnimal} {animal} in {place}.",
        f"There are {adjective} {magicalCreatures1} and {adjective2} {magicalCreatures2} here! In the {room} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {noun4}.", 
        f"It feels as though I have lived here for {number} {measure}. I hope one day you can visit, although the only way to get here now is {verb} on a {adjLast} {noun5}!!")
