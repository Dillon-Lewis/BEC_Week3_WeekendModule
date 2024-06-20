import re
contacts = {}

def main():
    while True:
        choice = input('''
Welcome to your contacts list, how can we help you today?
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display contact list                   
6. Import contacts
7. Quit program
''')
        if choice == '1':
            add()
        elif choice == '2':
            edit()
        elif choice == '3':
            delete()
        elif choice == '4':
            search()
        elif choice == '5':
            view()
        elif choice == '6':
            import_cons()
        elif choice == '7':
            print('Enjoy your day!!')
            break 
        else:
            print('Enter a valid numbered selection')
            continue



def add():
    while True:
        try:
            name = input('Enter name of person you would like to add: \n').title()
            phone = input("What is the phone number you would like to add: \n")
            contact_number = re.search(r'\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}', phone)
            email = input('what is the contacts email\n')
            contact_email = re.search(r"[\w.-]+@[\w-]+.[a-z]{2,3}", email)
            contacts.update({contact_number.group(): {"Name": name, "Phone number" : contact_number.group(), "Email" : contact_email.group()}})
            print(f'{name} has been successfuly added to your contacts list!')
            break
        except AttributeError:
            print("formattting not correct")  
        except Exception as e:
            print(e)

        with open('contacts.txt', 'w') as file:
            for number, info in contacts.items():
                file.write(f"{number}-:-{info["name"]}-:-{info["phone_number"]}-:-{info["email_address"]}\n")




            

def delete():
    while True:
        delete = input("Please enter the name of the contact you want to delete: \n").title()
        if delete in contacts:
            print(contacts[delete])
            confirmation = input("Before proceeding, are you sure you would like to delete this contact: YES or NO \n").upper()
            if confirmation == "YES":
                del contacts[delete]
                print("Contact has been deleted.")
                break
            elif confirmation == "NO":
                continue
            else:
                print('Please enter a valid entry!')
                continue
        else:
            print('Invalid entry, try again')
            continue


def view():
    while True:
        [print(f"{key}: {value}") for key, value in contacts.items()]
        go_back = input("Return to main menu?\n YES").upper()
        if go_back == 'YES':
            break
        else:
            print('Are you sure you spelt yes right?')
            continue


def search():
    while True:
        Number = input('Please enter the phone number of the persons you are trying to pull up:\n').title()
        if Number in contacts:
            print(contacts[Number])
            break
        else:
            print("Contact not found, please enter a valid number as it was orginally entered")


def edit():
    while True:
        try:
            number = input('Please enter the phone number of the contact you would like to edit')
            if number in contacts:
                print(contacts[number])
                edit = input('What would you like to change: Name or Email\n').title()
                if edit == "Name":
                    new_name = input('What would you like the new name to be: \n')
                    contacts[number]["Name"] = new_name
                    print(contacts[number])
                    break
                elif edit == "Email":
                    new_email = input('What would you like the new email to be: \n')
                    updated_email = re.search(r"[\w.-]+@[\w-]+.[a-z]{2,3}", new_email)
                    contacts[number]["Email"] = updated_email.group()
                    print(contacts[number])
                    break
        except AttributeError:
            print("formattting not correct, please try again")


def import_cons():
    with open("contacts.txt", "r") as file:                                
        for line in file:                                   
            number, name, phone_number, email_address = line.strip().split('-:-')
            contacts[number] = {'name': name, "phone_Number": phone_number, "email_address": email_address}
        print(contacts)




main()