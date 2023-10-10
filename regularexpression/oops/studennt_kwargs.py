def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_student(name="jeevan",course="django",roll=1000,gender="male")