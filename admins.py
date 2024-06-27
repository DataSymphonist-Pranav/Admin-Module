import mysql.connector as sql
from tabulate import tabulate
from termcolor import colored
import uuid

mydb = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "Pranav#28",
    database = "admins"
    )

my_cursor = mydb.cursor(buffered=True)

def passforgot():
    print("")
    print('''    1. Forgot password
    8. Go back
    ''')
    print("")
    choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while choice!="1" and choice!="8":
        print(colored("Sorry Invalid Selection, Please try Again",'red'))
        print('''    1. Forgot password
        8. Go back
        ''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if choice == "1":
        print("Create a new password")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        DOB = input("Enter DOB (DDMMYYYY): ")
        email = input("Email ID: ")
        Admin_id = input("Admin ID: ")
        my_cursor.execute("Select * From all_admins")
        result=my_cursor.fetchone()
        if first_name and last_name and DOB and email and Admin_id in result:
            print("Please Enter your new password")
            new_pass=input(">>>")
            print("Confirm Your Password")
            conf_new_pass=input(">>>")
            if new_pass==conf_new_pass:
                my_cursor.execute("UPDATE all_admins SET Password = %s WHERE ADMIN_ID = %s", (conf_new_pass,Admin_id,))
                mydb.commit()
                print("Thankyou, Your password has been Succesfully Changed")
                #Logout()
                print("Please log in with new password")
                print("Thankyou")
            else:
                print('''Sorry Credentials doesn't match.
                        Please try Again''')
                passforgot()
        else:
            print("No Details Found, Please Try Again.")
            passforgot()
    # elif choice=="2":
    #     menu()

def Login_credentials():
    print("")
    print(colored("**-CHANGE USER CREDENTIALS-**",'blue',attrs=['underline','bold']))
    print("")
    print('''    1. To change Password
    2. To change Username
    8. Go back
    9. Homepage''')
    choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while choice!="1" and choice!="2" and choice!="8" and choice!="9":
        print(colored("Sorry Invalid Selection, Please try Again",'red'))
        print('''
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if choice=="1":
        print("")
        print(colored("**-CHANGE PASSWORD-**",'blue',attrs=['underline','bold']))
        print("")
        print("Please provide the required information to follow up with your request-")
        first_name = input("    First Name: ")
        last_name = input("    Last Name: ")
        DOB = input("    Enter DOB (DDMMYYYY): ")
        email = input("    Email ID: ")
        Adminid = input("    Admin ID: ")
        my_cursor.execute("Select * From all_admins")
        result=my_cursor.fetchone()
        if first_name and last_name and DOB and email and Adminid in result:
            print("")
            print("    Please Enter your new password")
            new_pass=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
            print("    Confirm Your Password")
            conf_new_pass=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
            if new_pass==conf_new_pass:
                #Update Password in Admin Database
                my_cursor.execute("UPDATE all_admins SET Password = %s WHERE ADMIN_ID = %s", (conf_new_pass,Adminid,))
                mydb.commit()
                print(colored("Thankyou, Your password has been Succesfully Changed",'green'))
                #Logout()
                print(colored("    Please log in with New Credentials",'cyan'))
                print(colored("    Thankyou",'blue'))
            elif new_pass != conf_new_pass:
                print(colored('''Sorry Password doesn't match.
                Please try Again''','red'))
                Login_credentials()
            else:
                print(colored('''Something Went Wrong.
                Please Try Again''','red'))
                Login_credentials()
        elif first_name and last_name and email not in result:
            print(colored('''Sorry Credentials doesn't match.
                Please try Again''','red'))
            Login_credentials()
    elif choice=="2":
        print("")
        print(colored("**-CHANGE USERNAME-**",'blue',attrs=['underline','bold']))
        print("")
        print("Please provide the required information to follow up with your request-")
        first_name = input("    First Name: ")
        last_name = input("    Last Name: ")
        DOB = input("    Enter DOB (DDMMYYYY): ")
        email = input("    Email ID: ")
        Adminid = input("    Admin ID: ")
        my_cursor.execute("Select * From all_admins")
        result=my_cursor.fetchone()
        if first_name and last_name and DOB and email and Adminid in result:
            print("")
            print("    Please Enter your new username")
            new_user=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
            print("    Confirm Your new username")
            conf_new_user=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
            if conf_new_user==conf_new_user:
                #Update Password in Admin Database
                my_cursor.execute("UPDATE all_admins SET Username = %s, WHERE ADMIN_ID = %s", (conf_new_user,Adminid,))
                mydb.commit()
                print(colored("Thankyou, Your password has been Succesfully Changed",'green'))
                #Logout()
                print(colored("    Please log in with New Credentials",'cyan'))
                print(colored("    Thankyou",'blue'))
            elif new_user != conf_new_user:
                print(colored('''Sorry Password doesn't match.
                Please try Again''','red'))
                Login_credentials()
            else:
                print(colored('''Something Went Wrong.
                Please Try Again''','red'))
                Login_credentials()
        elif first_name and last_name and email not in result:
            print(colored('''Sorry Credentials doesn't match.
                Please try Again''','red'))
            Login_credentials()
    elif choice == "8":
        account_settings()
    elif choice == "9":
        main_admins()

def email_update():
    print("")   
    print(colored("**-CHANGE YOUR EMAIL-ID-**",'blue',attrs=['underline','bold']))
    print('')  
    print("For Security Reasons, please provide the required information.")
    print("    Enter Your Admin ID: ")
    id=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
    my_cursor.execute("SELECT ADMIN_ID from all_admins WHERE ADMIN_ID = %s", (id,))
    row = my_cursor.fetchone()
    if row:
        print(colored("    Thankyou...!",'blue'))
        print("")
        print("   Enter New Email ID")
        emailid=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
        my_cursor.execute("UPDATE all_admins SET email = %s WHERE ADMIN_ID = %s", (emailid,id,))
        mydb.commit()
        print(colored("Your Email-ID has been successfully updated.",'green'))
        print('''
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="8" and choice!="9":
            print(colored("Sorry Invalid Selection, Please try Again",'red'))
            print('''        1. To try Again.
        8. Go back
        9. Homepage''')
            choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "8":
            account_settings()
        elif choice == "9":
            main_admins()
    else:
        print(colored("Sorry Invalid Admin ID, Please try Again",'red'))
        print('''        1. To try Again.
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="1" and choice!="8" and choice!="9":
            print(colored("Sorry Invalid Selection, Please try Again",'red'))
            print('''        1. To try Again.
        8. Go back
        9. Homepage''')
            choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "1":
            email_update()
        if choice == "8":
            account_settings()
        if choice == "9":
            main_admins()

def mobile_update():
    print("")
    print(colored("**-CHANGE YOUR CONTACT NUMBER-**",'blue',attrs=['underline','bold']))
    print('')
    print("For Security Reasons, please provide the required information.")
    print("    Enter Your Admin ID: ")
    id=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
    my_cursor.execute("SELECT ADMIN_ID from all_admins WHERE ADMIN_ID = %s", (id,))
    row = my_cursor.fetchone()
    if row:
        print("    Thankyou...!")
        print("")
        print("   Enter New Contact Number")
        mobile_number=input(">>>")
        my_cursor.execute("UPDATE all_admins SET Mobile_number = %s WHERE ADMIN_ID = %s", (mobile_number,id,))
        mydb.commit()
        print(colored("Your Contact Number has been successfully updated.",'green'))
        print('''
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="8" and choice!="9":
            print(colored("Sorry Invalid Selection, Please try Again",'red'))
            print('''
        8. Go back
        9. Homepage''')
            choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "8":
            account_settings()
        elif choice == "9":
            main_admins()
    else:
        print(colored("Sorry Invalid Admin ID, Please try Again",'red'))
        print('''        1. To try Again.
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="1" and choice!="8" and choice!="9":
            print(colored("Sorry Invalid Selection, Please try Again",'red'))
            print('''        1. To try Again.
        8. Go back
        9. Homepage''')
            choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "1":
            mobile_update()
        if choice == "8":
            account_settings()
        if choice == "9":
            main_admins()

def modify_name():
    print("")
    print(colored("**-YOUR ACCOUNT NAME-**",'blue',attrs=['underline','bold']))
    print("")
    print("Please provide the required information")
    print("    Enter Your Admin ID: ")
    Adminid=(input(colored(">>>",'cyan',attrs=['underline','bold'])))
    my_cursor.execute("SELECT ADMIN_ID from all_admins WHERE ADMIN_ID = %s", (Adminid,))
    row = my_cursor.fetchone()
    if row:
        first_name=input("    Enter Your First Name: ")
        confirm_first_name=input("    Confirm Your First Name: ")    
        last_name=input("    Enter Your Last Name: ")
        confirm_last_name=input("    Confirm Your Last Name: ")
        while first_name != confirm_first_name and last_name != confirm_last_name:
            print(colored("First Name Dose not match with Confirmation First Name: ",'red'))
            print("Please Try Again...!")
            first_name=input("    Enter Your First Name: ")
            confirm_first_name=input("    Confirm Your First Name: ")
            last_name=input("    Enter Your Last Name: ")
            confirm_last_name=input("    Confirm Your Last Name: ")
        if first_name == confirm_first_name and last_name == confirm_last_name:
            #Change In Database First Name & Last Name
            my_cursor.execute("UPDATE all_admins SET First_name = %s WHERE ADMIN_ID = %s", (first_name,Adminid,))
            my_cursor.execute("UPDATE all_admins SET Last_name = %s WHERE ADMIN_ID = %s", (last_name,Adminid,))
            mydb.commit()
            print(colored("Succesfully Modified Your Name",'green'))
            print("")
            print("""Here's some operations you can perform:
        8. Go Back.
        9. To open Home page.
        """)
            choice= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
            while choice!="8" and choice!="9":
                print(colored("Invalid Selection,Please Select appropriate option.",'red'))
                print('''    Select an option to continue:
            8. Go Back.
            9. To open Home page.
            ''')
                choice = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
            if choice == "8":
                account_settings()
            elif choice == "9":
                main_admins()
    else:
        print(colored("Sorry Invalid Admin ID, Please try Again",'red'))
        print('''        1. To try Again.
        8. Go back
        9. Homepage''')
        choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="1" and choice!="8" and choice!="9":
            print(colored("Sorry Invalid Selection, Please try Again",'red'))
            print('''        1. To try Again.
        8. Go back
        9. Homepage''')
            choice=(input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "1":
            modify_name()
        elif choice == "8":
            account_settings()
        elif choice == "9":
            main_admins()

def account_settings():
    print("")
    print(colored("**-Your Account Setting-**",'blue',attrs=['underline','bold']))
    print('''
    1. To Modify Your Name.
    2. To modify Your Login Credentials.
    3. To update Your Email ID.
    4. To update Your Contact Number.
    8. Go Back.
    9. To open Home page.

    ''')
    option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while option!="1" and option!="2" and option!="3" and option!="4" and option!="8" and option!="9":
        print(colored("Invalid Selection,Please Select appropriate option.",'red'))
        print('''    Select an option to continue:
    1. To Modify Your Name.
    2. To modify Your Login Credentials.
    3. To update Your Email ID.
    4. To update Your Contact Number.
    8. Go Back.
    9. To open Home page.

    ''')
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if option == "1":
        modify_name()
    elif option == "2":
        #To update Login Credentials. 
        Login_credentials()
    elif option == "3":
        #To update Email ID.
        email_update()
    elif option =="4":
        #To Update Contact Number
        mobile_update()
    elif option=="9":
        main_admins()
    elif option=="8":
        main_admins()

def add_admins():
    #Connect This data with Database of All_admins
    print("")
    print(colored("**-ADD AN ADMIN-**",'blue',attrs=['underline','bold']))
    print('')
    print("Please Provide the required information about the admin to add it:")
    first_name = input("    First Name: ")
    last_name = input("    Last Name: ")
    Mobile_number=input("    Contact Number: ")
    DOB = input("    Enter DOB (in DDMMYYYY): ")
    admin_id= str((uuid.uuid4().hex[:8]))
    email = input("    Email ID: ")
    username= first_name+"123"
    password= last_name+"123"
    mySql_insert_data = """INSERT INTO all_admins (First_name, Last_name, Mobile_number, DOB, ADMIN_ID, email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
    insert_data = (first_name,last_name,Mobile_number,DOB,admin_id,email,username,password)
    result = my_cursor.execute(mySql_insert_data, insert_data)
    mydb.commit()
    #Send this info to Authentication Centre and add into Admin Database
    print("")
    print(colored("Admin details Added Succesfully",'green'))
    print("")
    print("""Here's some operations you can perform:
    1. Add Another Admin.
    8. Go Back.
    9. To open Home page.
    """)
    option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while option!="9" and option!="8" and option!="1":
        print(colored("Invalid Selection,Please Select appropriate option.",'red'))
        print('''    Select an option to continue:
    1. Add Another Admin.
    8. Go Back.
    9. To open Home page.
    ''')
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if option=="9":
        main_admins()
    elif option=="8":
        main_admins()
    elif option=="1":
        add_admins()

def main_admins():
    print("")
    print(colored("**-ADMIN PAGE-**",'blue',attrs=['underline','bold']))
    print("")
    print('''You Have succesfully entered admin control page.
    Select an option to continue:
    1. View all Admins
    2. Add Admin
    3. Support Numbers
    4. Your Account Settings
    ''')
    ask_admin = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while ask_admin!="4" and ask_admin!="3" and ask_admin!="2" and ask_admin!="1":
        print("")
        print(colored("Invalid Selection,Please Select appropriate option.",'red'))
        print('''    Select an option to continue:
    1. View all Admins
    2. Add Admin
    3. Support Numbers
    4. Your Account Settings
    ''')
        ask_admin = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if ask_admin == "1":
        #Fetch details of Admins.
        print("")
        print(colored("**-ALL-ADMIN's-**",'blue',attrs=['underline','bold']))
        print("")
        print(colored("    Here's a Data of all admins:",'magenta'))
        my_cursor.execute("SELECT Serial_Number,First_name,Last_name,Mobile_number,ADMIN_ID,email FROM all_admins")
        result = my_cursor.fetchall()
        x=colored("Sr.no.",'green')
        y=colored("First Name",'green')
        z=colored("Last Name",'green')
        zz=colored("Contact Number",'green')
        zzz=colored("Admin ID",'green')
        zzzz=colored("Email ID",'green')
        print(tabulate(result, headers=[x,y,z,zz,zzz,zzzz], tablefmt='psql'))
        print("")
        print("""Here's some operations you can perform:
    1. Open Your Account Settings.
    8. Go Back.
    9. To open Home page.
    """)
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while option!="9" and option!="8" and option!="1":
            print(colored("Invalid Selection,Please Select appropriate option.",'red'))
            print('''    Select an option to continue:
    1. Open Your Account Settings.
    8. Go Back.
    9. To open Home page.
    ''')
            option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if option=="9":
            main_admins()
        elif option=="8":
            main_admins()
        elif option=="1":
            account_settings()

    elif ask_admin == "2":
        #To add an admin in database.        
        add_admins()

    elif ask_admin == "3":
        #support Numbers.
        print("")
        print(colored("**-SUPPORT CONTACTS-**",'blue',attrs=['underline','bold']))
        print("")
        print(colored("Here's a list of Support Contacts.",'magenta'))
        my_cursor.execute("SELECT Sr_number, First_name, Last_name, Contact_number, Email_ID FROM support_numbers")
        result = my_cursor.fetchall()
        x=colored("Sr.no.",'green')
        y=colored("First Name",'green')
        z=colored("Last Name",'green')
        zz=colored("Contact Number",'green')
        zzzz=colored("Email ID",'green')
        print(tabulate(result, headers=[x, y, z, zz, zzzz], tablefmt='psql'))
        print("")
        print("9. To open Home page")
        get= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while get != "9":
            print(colored("Invalid Selection,Please Select appropriate option.",'red'))
            print("9. To open Home page")
            get= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        main_admins()
    elif ask_admin =="4":
        # jump to Account Settings
        account_settings()

main_admins()