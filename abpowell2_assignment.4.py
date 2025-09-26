student_name = "Aj Powell"
current_gpa = 3.7
study_hours = 20
social_hours = 25
stress_level = 50 
social_points = 65
classes = ["Programming", "Math", "English", "History"]
print("Your Starter Stats:")
print(f"Current GPA is {current_gpa}")
print(f"Your Study Hours {study_hours}")
print(f"Your Social Hours {social_hours}")
print(f"Your Stress Level {stress_level}")
print(f"Your Social Points {social_points}")
print("Pick your Dificulty to start the game")
print("A - Easy, B - Medium, C - Hard")
choose_course_load = input("Enter in your diffuclty letter here:")
if choose_course_load == "A":
    study_hours == study_hours
    social_hours == social_hours  + 5
    stress_level == stress_level - 20
    social_points == social_points +10
    if 2.0 <= current_gpa <= 2.75:
        print("You will do great, and be great friend. Enjoy the game.")
    elif current_gpa > 2.75:
        print("Why dont we kick it up a notch friend. I know you will be great.")
    elif current_gpa < 2.0:
        print("Academic Probation, GAME OVER") 
elif choose_course_load == "B":
    study_hours == study_hours + 6
    social_hours == social_hours - 3
    stress_level == stress_level + 15
    social_points == social_points - 15 
    if 2.5 < current_gpa <= 3.0:
        print("You are Where you need ot be. Enjoy the Game.")
    elif current_gpa > 3.0:
        print("Why dont we kick it up a notch friend. I know you will be great.") 
    elif current_gpa < 2.5:
        print("Maybe you would like to start off a little easier. Enjoy the Game.")
elif choose_course_load == "C":
    study_hours == study_hours + 10
    social_hours == social_hours - 8
    stress_level == stress_level + 30
    social_points == social_points - 20
    if current_gpa < 2.5:
        print("Mabey you would like to start off a little easier. Enjoy the Game.") 
    elif 2.5 < current_gpa < 2.75:
        print("So you want to work hard do you, be carful this will be difficult. Enjoy the game.")
    elif 2.75 <= current_gpa < 3.5:
        print("You are right where you need to be. Enjoy the game.")
    elif current_gpa >= 3.5: 
        study_hours == study_hours + 12
        social_hours == study_hours - 10
        stress_level == stress_level + 45
        social_points == social_points - 30
        print("Tuff stuff huh, Well you do great. Enjoy the game.")
else:
    print("Invlaid Input. Please try again friend.")
print("Your Weekly Stats:")
print(f"Current GPA is {current_gpa}")
print(f"Your Study Hours {study_hours}")
print(f"Your Social Hours {social_hours}")
print(f"Your Stress Level {stress_level}")
print(f"Your Social Points {social_points}")
print("Pick your Dificulty to start the game")
print("Classes: Programing, History, Math, English")
classdescision = input("What class are you going to study:")
if classdescision in classes:
    if classdescision == classes[0]:
        social_points = social_points - 5
        current_gpa == current_gpa + 0.2
    elif classdescision == classes[1]:
        social_points = social_points - 6
        current_gpa = current_gpa + 0.4
    elif classdescision == classes[2]:
        social_points = social_points - 4
        current_gpa = current_gpa + 0.5
    elif classdescision == classes[3]:
        social_points = social_points - 3
        current_gpa = current_gpa + 0.25
elif classdescision not in classes:
    print("Uh Oh lets try that again.")
if classdescision == classes[0] or classdescision == classes[1]:
    print("STEM huh? I like your style")
elif classdescision == classes[2] or classdescision == classes[3]:
    print("Core classes huh? Youve got good taste") 
print("Your Weekly Stats:")
print(f"Current GPA is {current_gpa}")
print(f"Your Study Hours {study_hours}")
print(f"Your Social Hours {social_hours}")
print(f"Your Stress Level {stress_level}")
print(f"Your Social Points {social_points}")
