# Project Name : Automating Decison Making
# Skills Required : Python , Lists , Random Module , Input Function
# Advanced Skills Required : Pandas , APIs
# Advanced Project Idea : Utilize APIs For automatio

from random import choice

# Create List Of SoftWare

webSeries=["Photoshop","Premium pro","Visual Studio Code","Lightroom"]
#["shub","hey"]]

# Print a random Movie  from Lits

# print(choice(webSeries))

# Input Mood

print("What Mood Are You In ? ")
mood = input()

# Loop through and find a matching mood.

for item in webSeries:
    if item[1] == mood:
        print(mood + "WebSeries"+ item[0])
