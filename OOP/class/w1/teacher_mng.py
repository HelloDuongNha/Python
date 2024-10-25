list_id = [1, 2, 3]
list_names = ['John', 'Alain', 'Donald']
list_subjects = ['Network, Security', "Python, C++, Network", 'C++, Web Develop, Java']

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_teacher()
        elif choice == 2:
            edit_teacher()
        elif choice == 3:
            delete_teacher()
        elif choice == 4:
            show_teacher()
        elif choice == 5:
            search_teacher()
        elif choice == 0:
            print(' thank you for using Teacher Management Appliation')
            running = False
        else:
            print('invalid value')


def print_menu():
    print('selection 0: exit')
    print('selection 1: Add the new teacher')
    print('selection 2: Edit the teacher')
    print('selection 3: Delete the teacher')
    print('selection 4: Show all the teacher')
    print('selection 5: Search the teacher by subject')

def add_teacher():
    id = int(input('ID of teacher: '))
    if check_id(id) == -1:
        print('****add new teacher*****')
        name = input('teacher name: ')
        subject = input('subject of new teacher: ')
        list_id.append(id)  
        list_names.append(name)
        list_subjects.append(subject)
        print(f'teacher {name} added successfully')
    else: 
        print('invalid ID')

def check_id(id):
    for i in range(len(list_id)):
        if list_id[i] == id:
            return i
    return -1

def edit_teacher():
    id = input('ID of teacher to edit: ')
    if check_id(id) != -1:
        subject = ('enter new subject: ')
        list_subjects[check_id(id)] = subject
    else:
        print('invalid ID')

def delete_teacher():
    id = input('ID of teacher to delete: ')
    if check_id(id) != -1:
        name = list_names[check_id(id)]
        subject = list_subjects[check_id(id)]
        list_id.remove(id)
        list_names.remove(name)
        list_subjects.remove(subject)
        print(f'teacher ID {id}:{name[check_id(id)]} is deleted')
    else:
        print('not found ID')

def show_teacher():
    for i in range(len(list_id)):
        print(f'teacher ID: {list_id[i]}, name: {list_names[i]}')
        print(f'subject: {list_subjects[i]}')

def search_teacher():
    subject = input('enter a subject: ')
    print(f'list of teacher who can teach {subject}: ')
    count = 0
    for i in range(len(list_subjects)):
        if subject in list_subjects[i]:
            print(f' teacher ID {list_id[id]}, name: {list_names[id]}')
            count += 1
    if count == 0:
        print(f' no teacher available for subject {subject}')



run()
