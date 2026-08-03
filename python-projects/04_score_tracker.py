#storing my_class students result in dic
students = {
    "my_class1" : [("talha",99),("fatima", 95),("tayyab",80),("ahmad",65)],
    "my_class2" : [("umer",90),("ali", 67),("hania",86),("usman",65)]
}



for classes in students:
    print(f"\n{classes} :")

    data = students[classes]
    top_scorer = []
    highest_marks = 0
    for name,marks in data:
        
        
        if marks > highest_marks:
            highest_marks = marks
            top_scorer = [name]
        elif marks == highest_marks:
            top_scorer.append(name)
    print(f"The top scorer of class is {"".join(top_scorer)} with {highest_marks}")

    

    
    

     
