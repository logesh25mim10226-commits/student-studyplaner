subjects = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input(f"Enter name of subject {i+1}: ")
    difficulty = input("Enter difficulty (easy/medium/hard): ").lower()
    days_left = int(input("Enter days left for exam: "))
    subjects.append([name, 3 if difficulty=="hard" else 2 if difficulty=="medium" else 1, days_left, 0, 0, "pending"])

total_hours = int(input("Enter total study hours per day: "))
days_plan = int(input("Enter number of days to plan: "))
energy = input("When are you most active? (morning/evening): ").lower()
speed = input("Learning speed (fast/slow): ").lower()
weak = input("Enter weak subject (or 'none'): ").lower()

performance = []
distractions = []

print("\nNow enter performance and distraction for each day:")
for day in range(1, days_plan+1):
    perf = input(f"Day {day} - Did you complete plan? (yes/no): ").lower()
    performance.append(perf)
    distraction = int(input(f"Day {day} - Distraction level (1-10): "))
    distractions.append(distraction)

streak = 0

print("\nSTUDENT STUDY PLANNER SYSTEM")
print("Total Subjects:", len(subjects))
print("Planning Days:", days_plan)
print("Weak Subject:", weak)
print("Energy Preference:", energy)
print("Learning Speed:", speed)

for day in range(1, days_plan + 1):

    print("\n********************")
    print("DAY", day, "STUDY PLAN")
    print("********************")

    for s in subjects:
        urgency = 2 if s[2] <= 2 else 0
        s[3] = (s[1] * 2) + (1 / s[2]) + urgency

    total_priority = sum(s[3] for s in subjects)

    for s in subjects:
        s[4] = (s[3] / total_priority) * total_hours
        if weak != "none" and s[0].lower() == weak:
            s[4] += 1
        if speed == "slow":
            s[4] += 0.5
        elif speed == "fast":
            s[4] -= 0.3
        if s[4] < 1:
            s[4] = 1

    subjects.sort(key=lambda x: x[3], reverse=True)

    print("\n--- Subject Allocation ---")
    for s in subjects:
        if s[5] == "done":
            continue
        name = s[0]
        hours = round(s[4], 2)
        difficulty = s[1]
        days_left = s[2]

        if energy == "morning" and difficulty == 3:
            slot = "Morning (High Energy)"
        elif energy == "evening" and difficulty == 3:
            slot = "Evening (High Energy)"
        else:
            slot = "Flexible Time"

        print("\nSubject:", name)
        print("Study Hours:", hours)
        print("Time Slot:", slot)

        print("Explanation:")
        if difficulty == 3:
            print("- Hard subject")
        if difficulty == 2:
            print("- Medium subject")
        if difficulty == 1:
            print("- Easy subject")
        if days_left <= 2:
            print("- Exam is very near")
        if weak != "none" and name.lower() == weak:
            print("- Weak subject priority increased")

    print("\n--- Special Notes ---")
    if day % 3 == 0:
        print("Revision Day Activated")
    if total_hours > 6:
        print("Break Plan: 20 min break after every 2 hours")
    else:
        print("Break Plan: 10 min break after 2 hours")

    completed = performance[day - 1]
    distraction = distractions[day - 1]

    print("\n--- Performance Tracking ---")
    if completed == "yes":
        streak += 1
        print("Task Completed: YES")
        print("Current Study Streak:", streak)
        print("Motivation: Keep it up!")
    else:
        streak = 0
        print("Task Completed: NO")
        print("Streak Reset")
        print("Motivation: Try to focus more tomorrow!")
    print("Distraction Level:", distraction)

    print("\n--- Updating System for Next Day ---")
    for s in subjects:
        s[2] -= 1
        if s[2] <= 0:
            s[5] = "done"
            s[2] = 1
            print(s[0], "marked as completed")
        if completed == "no":
            s[4] += 0.5
        if distraction > 7:
            s[4] -= 0.5

print("\n********************")
print("FINAL ADVICE")
print("********************")
print("Stay consistent in your studies.")
print("Focus more on weak subjects.")
print("Revise regularly before exams.")
print("Maintain a good study-life balance.")


