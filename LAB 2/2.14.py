def grade(marks):
    if marks == 'absent':
        return 'NA'
    marks = int(marks)
    if marks <= 39:
        return 'F'
    elif marks <= 44:
        return 'P'
    elif marks <= 49:
        return 'C'
    elif marks <= 54:
        return 'B'
    elif marks <= 59:
        return 'B+'
    elif marks <= 69:
        return 'A'
    elif marks <= 79:
        return 'A+'
    elif marks <= 100:
        return 'O'
    else:
        return 'Invalid'

def main():
    subjects = ['Math', 'Science', 'English']
    marks = []
    total = 0
    fail = False

    for subject in subjects:
        mark = input(f"Enter marks for {subjects} (or 'Absent'): ")
        if mark != 'Absent':
            mark = int(mark)
            if mark <= 39:
                fail = True
            total = total + mark
        marks.append(mark)

    average = total / len(subjects)
    result = "fail" if fail else "pass"

    print("results:")
    for i, mark in enumerate(marks):
        print(f"{subjects[i]}: Marks = {mark}, Grade = {grade(mark)}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()