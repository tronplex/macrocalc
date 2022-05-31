import time

# CREATE USERINFORMATION DICTIONARY USING KEY AND UNNASSIGNED VALUES. 
keys = {'userName', 'userAge', 'userHeight_IN','userHeight_CM', 'userWeight_LBS', 'userWeight_KG', 'userGender', 
'userBodyFatPercentage', 'userGoalBodyFatPercentage', 'userActivityLevel', 'userLBM', 'userLBM_KG', 'userGoalWeight_LBS',
'userGoalCalories', 'userMaxHeartRate', 'userTargetHeartRateLower', 'userTargetHeartRateUpper', 'userProteinMultiplier'}
value = []
userInformation = dict.fromkeys(keys, value)

# VISUAL SEPARATION ITEMS
horizontalRule_stars = "*" * 50
horizontalRule_dashes = "-" * 50

# FUNCTION THAT ASKS USER FOR GENDER, CONVERTS TO LOWERCASE IF INPUT IS UPPERCASE, AND VALIDATES USER INPUT
def get_gender(prompt):
    while True:
        try:
            gender = str(input(prompt)).lower()
            valid_genders = ['m', 'f']
        except ValueError:
            print("Sorry, please enter 'm' or 'f'.")
            continue
        if gender not in valid_genders:
            print("Sorry, please enter 'm' or 'f'.")
            continue
        elif len(gender) > 1:
            print("Sorry, please enter 'm' or 'f'.")
            continue
        else:
            break
    return gender

# FUNCTION THAT ASKS USER FOR INFORMATION IN INTEGERS (AGE, WEIGHT, HEIGHT, ETC), AND VALIDATES USER INPUT
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Sorry, please enter whole numbers.')
            continue
        if value < 0:
            print('Sorry, numbers must not be negative.')
            continue
        elif value > 600:
            print('Please enter accurate information.')
            continue
        else:
            break
    return value

# HEADER AND TITLE. INTRODUCTION.
print(horizontalRule_stars)
print(horizontalRule_stars)
print("MACRONUTRIENT CALCULATOR")
print(horizontalRule_stars)
print(horizontalRule_stars)
print("""The following program will help create a custom diet tailored specifically
for you. First, we will gather some information regarding your current height, weight, age,
gender, current body fat percentage, goal body fat percentage, and level of activity. Then,
we will calculate a diet program that will help you meet your fitness goals.

When you're ready to get started, let us know your name. From there, we will gather the 
rest of the required information.\n""")

# SLEEP FOR 5 SECONDS
time.sleep(5)

# GET USER'S NAME AND UPDATE USERINFORMATION DICTIONARY
userName = (input("What is your name?: "))
userInformation.update({"userName":userName})
print(horizontalRule_dashes + "\n")
print("Great! Nice to meet you " + str(userName) + ". Next, we will need to know your current weight in pounds.")


# GET USER'S WEIGHT USING GET_FLOAT FUNCTION, CALCULATE USERWEIGHT_KG AND UPDATE USERINFORMATION DICTIONARY
userWeight_LBS = get_float(str(userName) + ", please enter your weight in pounds (lbs.): ")
userWeight_KG = userWeight_LBS / 2.2
userInformation.update({"userWeight_LBS":userWeight_LBS})
userInformation.update({"userWeight_KG":userWeight_KG})
print(horizontalRule_dashes + "\n")

# GET USER'S HEIGHT USING GET_FLOAT FUNCTION, CALCULATE USERHEIGHT_CM AND UPDATE USERINFORMATION DICTIONARY
userHeight_IN = get_float(str(userName) + ", please enter your height in inches (in.): ")
userHeight_CM = userHeight_IN * 2.54
userInformation.update({"userHeight_IN":userHeight_IN})
userInformation.update({"userHeight_CM":userHeight_CM})
print(horizontalRule_dashes + "\n")

# GET USER'S AGE USING THE GET_FLOAT FUNCTION AND UPDATE USERINFORMATION DICTIONARY
userAge = get_float("Next, we need to know your age, " +str(userName) + ": ")
userInformation.update({"userAge":userAge})
print(horizontalRule_dashes + "\n")

# GET USER'S GENDER USING THE GET_GENDER FUNCTION, UPDATE USERINFORMATION DICTIONARY, AND DISPLAY A MESSAGE TO THE USER
userGender = get_gender("Excellent, " + str(userName) + "! Lastly, please enter your gender (m or f): ")
userInformation.update({"userGender":userGender})
print("Thank you, " + str(userName) + ".\n\n")
time.sleep(3)

# RMR CALCULATOR
# INFORM USER ABOUT RMR
print(horizontalRule_stars)
print("RMR CALCULATION")
print(horizontalRule_stars)
print("""Using the information provided above, we will first calculate you Resting Metabolic
Rate (RMR). Your RMR is essentially the calories your body burns while doing nothing. By simply living, your
body is burning calories on its own all the time. We will calculate approximately how many calories
your body burns on its own each day. One moment please...\n""")
time.sleep(5)

# CALCULATE RMR
# RMR = (10 * W) + (6.25 * H) - (5 * 9) + (M = + 5) (W = - 161)
if userGender == 'm':
    userRMR = (10 * userWeight_KG) + (6.25 * userHeight_CM) - (5 * userAge) + 5 
else:
    userRMR = (10 * userWeight_KG) + (6.25 * userHeight_CM) - (5 * userAge) - 161 
print("Done!\n")
# PRINT USERNAME AND RMR ROUNDED TO NEAREST 2 DECIMAL PLACES
print(str(userName) + f", your Resting Metabolic Rate is: {round(userRMR, 2)}.")
print(horizontalRule_dashes + "\n")
time.sleep(3)

# GOAL WEIGHT
# INFORMATION.
print(str(userName) + """, now it is time to figure out your goal weight. To do this, we need you to provide your
current body fat percentage. Additionally, you will need to provide a goal body fat percentage. This helps us calculate
a more realistic goal rather than picking an arbitrary number on the scale.

Some reality to know about setting your body fat goal:

Men
    * 4-6% Usually “stage ready” for physique athletes. Considered VERY lean. Often performance
    will be affected, especially in combat sports. It is nearly impossible to gain muscle when this
    lean also, though maintaining muscle is feasible.

    * 7-10% Optimum range for most men. Easy to maintain if you workout and keep your diet in
    check. Abs are prominent and 10 is good for staying lean and still gaining muscle.

    * 11-15% This is when an athlete should get on a “cutting” phase to get back under 10%. Look
    is a little squishy, abs are still visible, so not really “fat”.

    * 16-20% This is leaning more towards “chubby”. If you are comfortable here, that’s cool, but
    you probably aren’t reading this book if you want to stay “chubby”.

Women
    * 8-13% Super lean for women. Sometimes periods are interrupted. This is “stage ready” for
    physique athletes. Not recommended most women hang out this low.

    * 14-18% Still pretty lean, but good for athletes. Olympic sprinters usually hang around
    15-18%. Some women will find this almost impossible to maintain though.

    * 19-24 Lean and healthy. This is easy to maintain and won’t affect performance at all.

    * 25-30% This is still healthy, but most women would probably like to be a little leaner.\n\n""")
time.sleep(5)
print("Take your time, " +str(userName) + ", and read through the information above.\n")
userBodyFatPercentage = get_float("Please, provide your current body fat percentage as a decimal (15% = .15): ")
userInformation.update({"userBodyFatPercentage":userBodyFatPercentage})
print(horizontalRule_dashes + "\n")
userGoalBodyFatPercentage = get_float("Thank you, " +str(userName) + ". Now, please provide your GOAL body fat percentage as a decimal (10% = .10): ")
userInformation.update({"userGoalBodyFatPercentage":userGoalBodyFatPercentage})
print("Thank you! One moment while we calculate your goal weight... \n")
# GOAL WEIGHT(GOALWEIGHT) = WEIGHT(LB) * BODY FAT PERCENTAGE AS DECIMAL(BF) = X
# WEIGHT(W) - X = LEAN BODY MASS(LBM)
# LEAN BODY MASS(LBM) / (1 - GOAL BF) = GOAL WEIGHT(GOALWEIGHT)
x = userWeight_LBS * userBodyFatPercentage
userLBM = userWeight_LBS - x
userGoalWeight_LBS = userLBM / (1 - userGoalBodyFatPercentage)
time.sleep(3)
print("Okay, " + str(userName) + ", your goal weight is " + str(round(userGoalWeight_LBS, 1)) + "lbs.")
print(horizontalRule_dashes + "\n")

# GOAL CALORIES
# INFORMATION. WHAT? HOW? WHY?
print(horizontalRule_stars)
print(horizontalRule_stars)
print("GOAL CALORIES")
print(horizontalRule_stars)
print(horizontalRule_stars + "\n")
print("""In order to calculate your goal calories we need to know how actve you are each
week. Review the ranges below and select the multiplier that most accurately describes your
total minutes in cardio each week. Minutes in cardio is defined as the number of minutes you spend
each week with your heart rate between 65 - 85 percent of your max heart rate.""")
# MAX HEART RATE AND TARGET HEART RATE MINUTES = MINUTES IN CARDIO (HEART RATE AT 65-85% OF MAX HEART RATE)
userMaxHeartRate = 220 - int(userAge)
userInformation.update({"userMaxHeartRate":userMaxHeartRate})
userTargetHeartRateLower = int(userMaxHeartRate) * .65
userInformation.update({"userTargetHeartRateLower":userTargetHeartRateLower})
userTargetHeartRateUpper = int(userMaxHeartRate) * .85
userInformation.update({"userTargetHeartRateUpper":userTargetHeartRateUpper})
print(str(userName + ", based on your age, your max heart rate is approzimately: " + str(userMaxHeartRate) + " BPM, and your target heart rate is approximately between " + str(round(userTargetHeartRateLower)) + " - " + str(round(userTargetHeartRateUpper)) + " BPM"))
print(horizontalRule_dashes + "\n")
print(str(userName) + ", review the information below: ")
print("""
    0-30 MINUTES        10
    30-150 MINUTES      11
    150-240 MINUTES     12
    240-300 MINUTES     13
    300+ MINUTES        14 \n""")
userActivityLevel = get_float("Please enter a multiplier from above (10 - 14): ")
userInformation.update({"userActivityLevel":userActivityLevel})
userActivityMinutes = "10"
if userActivityLevel == 10:
    userActivityMinutes = "0 - 30 Minutes"
elif userActivityLevel == 11:
    userActivityMinutes = "30 - 150 Minutes"
elif userActivityLevel == 12:
    userActivityMinutes = "150 - 240 Minutes"
elif userActivityLevel == 13:
    userActivityMinutes = "240 - 300 Minutes"
elif userActivityLevel == 14:
    userActivityMinutes = "300+ Minutes"
else:
    print("huh...")

print("Thank you, " + str(userName) + ". One moment please... \n")
userGoalCalories = userGoalWeight_LBS * userActivityLevel
userInformation.update({'userGoalCalories':userGoalCalories})
time.sleep(3)
print("Your goal calorie intake per day is: " + str(round(userGoalCalories)) + " calories")
print(horizontalRule_dashes + "\n")
time.sleep(3)


# CALCULATING YOUR MACROS
# INFORMATION.
print(horizontalRule_stars)
print(horizontalRule_stars)
print("CALCULATING YOUR MACROS")
print(horizontalRule_stars)
print(horizontalRule_stars + "\n")
print("""To calculate your macros, we first start with protein. Your total grams of
protein intake per day is based on your lean body mass. We also need to know what your goals
are in terms of muscle mass. To do this we need you to provide another multiplier. This multiplier
will be between .8 and 3 (.8 being the lowest and 3 being the highest). Athletes and very
active people should use 3 as their multiplier.\n""")
userProteinMultiplier = get_float("Please provide a multiplier between .8 and 3: ")
userInformation.update({'userProteinMultiplier':userProteinMultiplier})
print(horizontalRule_dashes + "\n")

print()
# 1G PROTEIN = 4 CALORIES
# 1G CARBOHYDRATE = 4 CALORIES
# 1G FAT = 9 CALORIES

# CALCULATING PROTEIN
# PROTEIN = LEAN BODY MASS(LBM) / 2.2 * MULTIPLIER
userProteinGrams = userLBM / 2.2 * userProteinMultiplier

# CALCULATING FAT
# FAT = GOAL WEIGHT * .4
userFatGrams = userGoalWeight_LBS * .4

# CALCULATING CARBOHYDRATES
# INFORMATION
# PROTEIN CALORIES = GRAMS OF PROTEIN * 4
userProteinCalories = userProteinGrams * 4
# FAT CALORIES = GRAMS OF FAT * 9
userFatCalories = userFatGrams * 9 
# CARBOHYDRATES CALORIES = PROTEIN CALORIES + FAT CALORIES - GOAL CALORIES
userCarbohydrateCalories = userGoalCalories - (userProteinCalories + userFatCalories)
# CARBOHYDRATES = CARBOHYDRATES CALORIES / 4
userCarbohydrateGrams = userCarbohydrateCalories / 4
print(str(userName) + ", based upon the information you provided your goal daily macronutrients are as follows: \n")
print("Protein:         " + str(round(userProteinGrams)) + "g")
print("Fat :            " + str(round(userFatGrams)) + "g")
print("Carbohydrates :  " + str(round(userCarbohydrateGrams)) + "g")
print(horizontalRule_dashes  + "\n")
time.sleep(3)

print("Here is a complete list of all your numbers: \n")
time.sleep(3)
print(horizontalRule_stars)
print(horizontalRule_stars  + "\n")
print("NAME:                        " + str(userName))
print("AGE:                         " + str(userAge))
print("HEIGHT:                      " + str(userHeight_IN) + "in.")
print("CURRENT WEIGHT:              " + str(userWeight_LBS) + "lbs.")
print("LEAN BODY MASS:              " + str(round(userLBM)) + "lbs.")
print("CURRENT BODY FAT:            " + str(userBodyFatPercentage * 100))
print("GOAL BODY FAT:               " + str(userGoalBodyFatPercentage * 100))
print("GOAL WEIGHT:                 " + str(round(userGoalWeight_LBS)) + "lbs.")
print("MAX HEART RATE:              " + str(round(userMaxHeartRate)) + " BPM")
print("TARGET HEART RANGE:          " + str(round(userTargetHeartRateLower)) + " - " + str(round(userTargetHeartRateUpper)) + " BPM")
print("ACTIVE MINUTES:              " + str(userActivityMinutes) + " minutes per week")
print("RESTING METABOLIC RATE:      " + str(round(userRMR)) + " calories per day")
print("DAILY GOAL CALORIES:         " + str(round(userGoalCalories)) + " calories per day")
print("PROTEIN GRAMS:               " + str(round(userProteinGrams)) + " grams per day")
print("FAT GRAMS:                   " + str(round(userFatGrams)) + " grams per day")
print("CARBOHYDRATE GRAMS:          " + str(round(userCarbohydrateGrams)) + " grams per day\n")
print("Done.\n")
print(horizontalRule_stars)
print(horizontalRule_stars  + "\n")


# print(userInformation)
