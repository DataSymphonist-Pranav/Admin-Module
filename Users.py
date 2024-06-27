import mysql.connector as sql
from tabulate import  tabulate
from termcolor import colored

mydb = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "Pranav#28",
    database = "admins"
)

my_cursor = mydb.cursor(buffered=True)

def enable_disable(userid,name):
    my_cursor.execute("SELECT Status FROM users_database WHERE id ='%s' ",(userid,))
    result = my_cursor.fetchone()
    status=result[0]
    print("The selected user-",name,"is-",status)
    print("")
    if status=="In-Active":
        print("Are You sure you want to 'Enable' The User?")
        print("1. Yes          2. No")
        ask = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if ask=="1":
            my_cursor.execute("UPDATE users_database SET Status = 'Active' WHERE id ='%s' ", (userid,))
            mydb.commit()
            print(colored("Successfully Enabled the User",'green'))
        elif ask=="2":
            print("Your Request has been Terminated.")
        print("")
        print("""    Here's some operations you can perform:
        8. Go Back.
        9. To open Home page.
        """)
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while option!="9" and option!="8" and option!="1":
            print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
            print('''    Select an option to continue:
        8. Go Back.
        9. To open Home page.
        ''')
            option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if option=="8":
            #Go Back
            modify_users()
        elif option=="9":
            #Homepage
            users()

    elif status=="Active":
        print("Are You sure you want to 'Disable' The User?")
        print("1. Yes          2. No")
        ask = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if ask=="1":
            my_cursor.execute("UPDATE users_database SET Status = 'In-Active' WHERE id ='%s' ", (userid,))
            mydb.commit()
            print(colored("Successfully Disabled the User",'red'))
        elif ask=="2":
            print("Your Request has been Terminated.")
        print("")
        print("""    Here's some operations you can perform:
        8. Go Back.
        9. To open Home page.
        """)
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while option!="9" and option!="8" and option!="1":
            print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
            print('''    Select an option to continue:
        8. Go Back.
        9. To open Home page.
        ''')
            option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if option=="8":
            #Go Back
            modify_users()
        elif option=="9":
            #Homepage
            users()

def modify_user_info(userid):
    print("")
    print(colored("**- USER ACCOUNT NAME CHANGE -**",'blue',attrs=['underline','bold']))
    print("Please provide the required information")
    first_name=input("    Enter First Name: ")
    confirm_first_name=input("    Confirm First Name: ")    
    last_name=input("    Enter Last Name: ")
    confirm_last_name=input("    Confirm Last Name: ")
    while first_name != confirm_first_name and last_name != confirm_last_name:
        print(colored("First Name or Last Name Does not match with Confirmation First Name or Last Name: ",'red'))
        print("Please Try Again...!")
        first_name=input("    Enter First Name: ")
        confirm_first_name=input("    Confirm First Name: ")
        last_name=input("    Enter Last Name: ")
        confirm_last_name=input("    Confirm Last Name: ")
    if first_name == confirm_first_name and last_name == confirm_last_name:
        #Change In Database First Name & Last Name
        my_cursor.execute("UPDATE users_database SET first_name = %s WHERE id = %s", (first_name,userid,))
        my_cursor.execute("UPDATE users_database SET last_name = %s WHERE id = %s", (last_name,userid,))
        mydb.commit()
        print(colored("Succesfully Modified User's Name",'green'))
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
            modify_users()
        elif choice == "9":
            users()

def warning_mail(user_id,name):
    #mail code
    import smtplib
    import ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "nayrobi678@gmail.com"
    receiver_email = (input("Enter your mail id:"))
    password = "@nayrobi123@"
    message = """
            Subject: Warning Mail
            report:- .
            """
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message) #+ str(variable)
            print("please check your mail")
            print("Mail Successfully sent to-",user_id,name)
    except:
        print("you are not connected to internet")
        
def modify_users():
    print('''    Enter an User ID to perform Modifications:''')
    select_user = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    my_cursor.execute("SELECT id from users_database where id=%s", (select_user,))
    result=my_cursor.fetchall()
    if result:
        my_cursor.execute("select concat(first_name, ' ', last_name) from users_database where id=%s", (select_user,))
        result=my_cursor.fetchone()
        name=str(result[0])
        print("    User Selected-",name)
        print('''
        1. To View Selected User's Responses.
        2. To Send Warning E-mail.
        3. To Enable/Disable Selected User.
        4. To Modify Selected User Details.
        8. Go Back
        9. Homepage
        ''')
        ask= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while ask!="1" and ask!="2" and ask!="3" and ask!="8" and ask!="9":
            print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
            print('''        1. To View Selected User's Responses.
        2. To Send Warning E-mail.
        3. To Enable/Disable Selected User.
        4. To Modify Selected User Details.
        8. Go Back
        9. Homepage''')
            ask= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if ask == "1":
            my_cursor.execute("select Template from users_database where id=%s", (select_user,))
            result=my_cursor.fetchone()
            response=str(result[0])
            print(name,"'s Response:-\n")
            print(response)
            print("")
            print('''
        1. To Send Warning E-mail.
        2. To Enable/Disable Selected User.
        3. To Modify Selected User Details.
        8. Go Back
        9. Homepage
        ''')
            ask2= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
            while ask2!="1" and ask2!="2" and ask2!="3" and ask2!="8" and ask2!="9":
                print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
                print('''        1. To Send Warning E-mail.
            2. To Enable/Disable Selected User.
            3. To Modify Selected User Details.
            8. Go Back
            9. Homepage''')
                ask2= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
            if ask2=="1":
                select_user=int(select_user)
                warning_mail(select_user,name)
            elif ask2=="2":
                select_user=int(select_user)
                enable_disable(select_user,name)
            elif ask2=="3":
                modify_user_info(select_user)
            elif ask2=="8":
                users()
            elif ask2=="9":
                users()
        elif ask =="2":
            #Warning mail to selected input ID
            warning_mail(select_user,name)
        elif ask =="3":
            select_user=int(select_user)
            enable_disable(select_user,name)
        elif ask=="4":
            select_user=int(select_user)
            modify_user_info(select_user)
        elif ask=="8":
            users()
        elif ask=="9":
            users()

    else:
        print(colored("    Sorry Invalid User ID, Please try Again",'red'))
        print('''        1. To try Again.
        8. Go back
        9. Homepage''')
        choice= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        while choice!="1" and choice!="8" and choice!="9":
            print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
            print('''        1. To try Again.
        8. Go back
        9. Homepage''')
            choice= (input(colored(">>>",'yellow',attrs=['underline','bold'])))
        if choice == "1":
            modify_users()
        if choice == "8":
            users()
        if choice == "9":
            users()

def view_all_inactive():
    print("    Here's  Data of all In-Active Users:")
    my_cursor.execute("SELECT id, first_name, last_name, email, gender, Status FROM users_database WHERE Status ='In-Active'")
    result = my_cursor.fetchall()
    x=colored("ID",'green')
    y=colored("First Name",'green')
    z=colored("Last Name",'green')
    zz=colored("Email",'green')
    zzz=colored("Gender",'green')
    xyz=colored("Status",'green')
    print(tabulate(result, headers=[x,y,z,zz,zzz,xyz], tablefmt='psql'))
    print("""    Here's some operations you can perform:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    """)
    option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while option!="9" and option!="8" and option!="1":
        print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
        print('''    Select an option to continue:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    ''')
        option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if option=="1":
        #To view About Any user
        modify_users()
    elif option=="8":
        #Go Back
        users()
    elif option=="9":
        #Homepage
        users()

def view_all_active():
    print("    Here's Data of all Active Users:")
    my_cursor.execute("SELECT id, first_name, last_name, email, gender, Status FROM users_database WHERE Status ='Active'")
    result = my_cursor.fetchall()
    x=colored("ID",'green')
    y=colored("First Name",'green')
    z=colored("Last Name",'green')
    zz=colored("Email",'green')
    zzz=colored("Gender",'green')
    xyz=colored("Status",'green')
    print(tabulate(result, headers=[x,y,z,zz,zzz,xyz], tablefmt='psql'))
    print("""    Here's some operations you can perform:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    """)
    option =(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while option!="9" and option!="8" and option!="1":
        print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
        print('''    Select an option to continue:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    ''')
        option =(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if option=="1":
        #To view About Any user
        modify_users()
    elif option=="8":
        #Go Back
        users()
    elif option=="9":
        #Homepage
        users()

def view_all():
    print("")
    print(colored("    Here's a Data of all Users-",'magenta'))
    my_cursor.execute("SELECT id, first_name, last_name, email, gender, Status FROM users_database")
    result = my_cursor.fetchall()
    x=colored("ID",'green')
    y=colored("First Name",'green')
    z=colored("Last Name",'green')
    zz=colored("Email",'green')
    zzz=colored("Gender",'green')
    xyz=colored("Status",'green')
    print(tabulate(result, headers=[x,y,z,zz,zzz,xyz], tablefmt='psql'))
    print("")
    print("""    Here's some operations you can perform:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    """)
    option = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while option!="9" and option!="8" and option!="1":
        print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
        print('''    Select an option to continue:
    1. To View About any user.
    8. Go Back.
    9. To open Home page.
    ''')
        option =(input(colored(">>>",'yellow',attrs=['underline','bold'])))
    if option=="1":
        #To view About Any user
        modify_users()
    elif option=="8":
        #Go Back
        users()
    elif option=="9":
        #Homepage
        users()

def users():
    print("")
    print(colored("**-USER's Page-**",'blue',attrs=['underline','bold']))
    print('''
    You Have succesfully entered users page.

        Select an option to continue:
        1. View all Users.
        2. View all Active Users.
        3. View all Inactive Users.
        4. To View About any user.
        8. Go back.
        9. Homepage.
        ''')
    choice = (input(colored(">>>",'yellow',attrs=['underline','bold'])))
    while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="8" and choice!="9":
        print(colored('''Invalid Selection, Please Select Appropriate option-''','red'))
        print('''    Select an option to continue:
        1. View all Users.
        2. View all Active Users.
        3. View all Inactive Users.
        4. To View About any user.
        8. Go back.
        9. Homepage.
        ''')
        choice = (input(colored(">>>",'yellow',attrs=['underline','bold'])))

    if choice == "1":
        #Fetch details of all Users
        view_all()
        
    elif choice == "2":
        #Fetch details of Active Users
        view_all_active()

    elif choice == "3":
        #Fetch details of In-Active-Users
        view_all_inactive()

    elif choice == "4":
        #To View About any user
        modify_users()

    elif choice == "8":
        #Go Back
        users()
    
    elif choice == "9":
        #Homepage
        users()

users()