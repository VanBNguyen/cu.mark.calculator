from final_mark import percentages

def main():

    flag = True

    marks_needed = {}

    try:
        num_courses = int(input("Number of courses: "))
    except Exception:
        print("\n\nlol misinput TRY AGAIN\n\n")

    for _ in range(num_courses):
        course = input("Course Name: ")
        course_mark = percentages()
        marks_needed[course] = course_mark

    with open("marks_needed.txt", "w") as file:
        for course in marks_needed:
            file.write(f"{course}\n")
            file.write(f"A+ --> {marks_needed[course][0]}%\n")
            file.write(f"A  --> {marks_needed[course][1]}%\n")
            file.write(f"A- --> {marks_needed[course][2]}%\n")
            file.write("")

if __name__ == "__main__":
    main()



