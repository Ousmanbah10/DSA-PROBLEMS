# this is what i did.. # LAB 4

# text = "Info System Mgt,Business App Development,Bus Process Analysis,Systems Analy & Des,Database Applications,Business Telecomm Systems,Info Systems Security,Project Management,Manage Digital Srvc Innov"
# print(len(text))

# majorCourses = text.split(",")
# print(majorCourses)

# len(majorCourses)
# print(majorCourses[-3:])
# print(majorCourses[2:5])

# majorCourses.append("Capstone course")
# print(majorCourses)
# print(len(majorCourses))

# sanIndex = majorCourses.index("Systems Analy & Des")
# print(sanIndex)

# majorCourses.insert(3,"Systems Analysis and Design")
# print(majorCourses)

# to_remove = majorCourses.pop(4)
# print(to_remove)

# print(majorCourses)

# year1 = majorCourses[:5]
# print(year1)

# year2 = majorCourses[5:]
# print(year2)

# baTrack = ["Database System and Physical Design", "Business Intelligence and Reporting", "Business Analytics"]
# print(baTrack)

# majorCoursesWithTrack = majorCourses.copy()
# print(majorCoursesWithTrack)

# majorCoursesWithTrack.extend(baTrack)
# print(majorCoursesWithTrack)

# print(majorCourses)

# sortedCourseList = majorCourses[:]
# sortedCourseList.sort()
# print(sortedCourseList)

# sortedCourseList.sort(reverse=True)
# print(sortedCourseList)

#JOIN
words = [
    "Python", "is", "a", "powerful", "and", "fun", 
    "programming", "language", "used", "for", 
    "data", "science", "web", "development", 
    "artificial", "intelligence", "and", "automation"
]


words = ", ".join(words)

print(words)

