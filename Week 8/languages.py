from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java", "Static", True, 1995)
c = ProgrammingLanguage("C++", "Static", False, 1983)
print(ruby)
print(python)
print(vb)

list_of_language = [ruby, python, vb, java, c]

print("The dynamically typed language are:")
for each in list_of_language:
    if each.is_dynamic():
        print(each.name)