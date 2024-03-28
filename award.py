#Obtain input for the time taken in minutes for all three events of a triathlon
#and store result in their respective variables: swimTime, cycTime and runtTime.
swimTime = float(input("Enter the time taken in minutes for swimming: "))
cycTime = float(input("Enter the time taken in minutes for cycling: "))
runTime = float(input("Enter the time taken in minutes for running: "))

#Calculate total time taken to complete the triathlon.
totalTime = swimTime + cycTime + runTime
#Print result to the screen
print(f"\nTotal time taken to complete the triathlon: {totalTime} minutes")

#Identify which award is given in relation to total time entered earlier.
if totalTime <= 100:
    award = "Provincial Colours"
elif 100 < totalTime <= 105:
    award = "Provincial Half Colours"
elif 105 < totalTime <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

#Print the award achieved to the screen.
print(f"You have achieved the following award: {award}")
