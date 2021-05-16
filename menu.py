import database
import PasswordGenerator

menu_prompt = '''--Password Manager--

Please, choose one of these options:

1. Add new data
2. See all the Apps, Users and Passwords
3. Delete App, User and Password
4. Modify App, User or Password
5. Find by user name
6. Find by app
7. Exit

Your selection: '''

def menu():
    connection = database.connect()
    database.create_database(connection)

    while (user_input := input(menu_prompt)) != "7":
        if user_input == "1":
            app = input("Type the name of the app or website: ")
            user = input("Type the user name: ")
            pw_choice = input('''Please, choose one of these options
            1. Type my own password
            2. Use the 'Secure Password Generator 
            Your choice is: ''')
            if pw_choice == "1":
                password = input("Type your password: ")
            elif pw_choice == "2":
                PasswordGenerator.pw_lenght()
                psswrd = input('''If you want to try a new password type "1".
You can still write your own password or if you like the password, you can copy it and paste it here: ''')
                if psswrd != "1":
                    password = psswrd
                else:
                    continue
            else:
                print("Sorry, invalid input")

            database.add_data(connection, app, user, password)

        elif user_input == "2":
            data = database.get_all_data(connection)

            for info in data:
                print(info)

        elif user_input == "3":
            app = input("Please, type the app you want to delete: ")

            database.delete_info(connection, app)

        elif user_input == "4":
            update = input("Please, type the app you want to update: ")
            new_app = input("The new name will be: ")
            new_user = input("The new user name will be: ")
            new_pw = input("The new password will be: ")

            database.modify_column(connection, new_app, new_user, new_pw, update)

        elif user_input == "5":
            username = input("Type the user name you are looking for: ")
            find_user = database.get_by_user(connection, username)

            for user in find_user:
                print(user)

        elif user_input == "6":
            appname = input("Type the app you are looking for: ")
            find_app = database.get_by_app(connection, appname)

            for app in find_app:
                print(app)

        else:
            print("Invalid input, please try again.")

menu()
