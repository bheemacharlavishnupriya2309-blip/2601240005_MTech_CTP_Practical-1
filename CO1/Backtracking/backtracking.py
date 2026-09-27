# List of subjects
subjects = ["Python", "DBMS", "Networks"]

# Teacher for each subject
teachers = ["T1", "T2", "T1"]

# List of classrooms
rooms = ["R1", "R2"]

# List of time slots
slots = ["9AM", "10AM", "11AM"]

# Empty timetable
schedule = []


# Function to assign subjects
def assign(subjects, rooms, slots):

    # If all subjects are assigned
    if not subjects:
        return True

    # Select the first subject
    subject = subjects[0]

    # Get the teacher of the subject
    teacher = teachers[len(schedule)]

    # Start checking time slots
    s = 0

    while s < len(slots):

        # Start checking rooms
        r = 0

        while r < len(rooms):

            # Select current slot and room
            slot = slots[s]
            room = rooms[r]

            # Assume there is no conflict
            ok = True

            # Check previous assignments
            i = 0

            while i < len(schedule):

                # Check room conflict
                if schedule[i][1] == slot and schedule[i][2] == room:
                    ok = False

                # Check teacher conflict
                if schedule[i][1] == slot and schedule[i][3] == teacher:
                    ok = False

                i += 1

            # If there is no conflict
            if ok:

                # Add subject to timetable
                schedule.append([subject, slot, room, teacher])

                # Assign the next subject
                if assign(subjects[1:], rooms, slots):
                    return True

                # Backtrack
                schedule.pop()

            # Try next room
            r += 1

        # Try next time slot
        s += 1

    # No valid assignment
    return False


# Start the assignment
if assign(subjects, rooms, slots):

    # Print the timetable
    print(schedule)

else:

    # Print if no timetable is possible
    print("No solution")