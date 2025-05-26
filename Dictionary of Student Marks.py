sheet = {'Henry':60,'Peter':90,'Jake':75}
a = input("Enter the student's name: ")
if a not in sheet:
    print('Student not found.')
else:
    print(f"{a}'s marks: {sheet[a]}")
