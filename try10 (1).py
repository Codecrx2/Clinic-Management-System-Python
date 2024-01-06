# Importing the necessary Libraries
from datetime import date as dt
import pandas as pd
import matplotlib.pyplot as plt

# Reading and storing the necessary CSV files into dataframes
patient_data = pd.read_csv('Patients_main.csv')
admin_data = pd.read_csv('Admin_Data.csv')


def create_patient_account():
    # Add the patient's details to the dataframe
    pid = len(patient_data) + 1
    pname = input("Enter Patient First Name: ")
    plname = input("Enter Patient Last Name: ")
    pgender = input("Enter Patient Gender(M/F): ")
    pbday = input("Enter Patient Date of Birth (dd-mm-yyyy): ")
    pcontact = input("Enter Patient Contact Number: ")
    pemail = input("Enter Patient Gmail Address: ")
    pallergies = input("Enter Patient Allergies(If Any): ")
    patient_data.loc[len(patient_data.index)] = [pid,
                                                 pname,
                                                 plname,
                                                 pgender,
                                                 dt.today(),
                                                 pbday,
                                                 pcontact,
                                                 pemail,
                                                 pallergies]
    # Save the dataframe to the CSV file
    patient_data.to_csv('Patients_main.csv', index=False)
    print("Congratulations")
    print("New Account Created")



def update_patient_details():
    pid_to_update = input("Enter Patient ID to update details: ")
    
    if int(pid_to_update) in patient_data['Patient_ID'].values:
        # Get the index of the patient to update
        index_to_update = patient_data.index[patient_data
                                             ['Patient_ID'] == int(pid_to_update)].tolist()[0]
        print("Which information you would like to update:")
        print("1. Name")
        print("2. Last Name")
        print("3. Gender")
        print("4. DOB")
        print("5. Phone")
        print("6. Mail")
        which_info = int(input("Enter Option Number: "))
        # Get the updated details from the user
        if which_info == 1:
            pname = input("Enter Updated Patient First Name: ")
            patient_data.at[index_to_update, 'Name'] = pname
        elif which_info == 2:
            plname = input("Enter Updated Patient Last Name: ")
            patient_data.at[index_to_update, 'Lname'] = plname
        elif which_info == 3:
            pgender = input("Enter Updated Patient Gender(M/F): ")
            patient_data.at[index_to_update, 'Gender'] = pgender
        elif which_info == 4:
            pbday = input("Enter Updated Patient Date of Birth (dd-mm-yyyy): ")
            patient_data.at[index_to_update, 'DOB'] = pbday
        elif which_info == 5:
            pcontact = input("Enter Updated Patient Contact Number: ")
            patient_data.at[index_to_update, 'Phone_no'] = pcontact
        elif which_info == 6:
            pemail = input("Enter Updated Patient Gmail Address: ")
            patient_data.at[index_to_update, 'Mail'] = pemail

        # Save the dataframe to the CSV file
        patient_data.to_csv('Patients_main.csv', index=False)
        print("Patient details updated successfully.")
    else:
        print("Patient ID not found. Please enter a valid Patient ID.")


def patient_login():
    email = input("Enter Patient Email: ")
    password = input("Enter Patient Password: ")
    if (patient_data['Gmail_Address'] == email).any():
        if (patient_data['Password'] == password).any():
            print("Patient Logged In Successfully")
        else:
            print("Incorrect Patient Password")
    else:
        print("Incorrect Patient Email")




def admin_details():
    data_change_choice = input("Do You Wish To Change Any Above Data?(Yes/No)")
    if data_change_choice.lower() == 'yes':
        for i in range(len(admin_data.columns)):
            dcc = input(f"Enter new value for {admin_data.columns[i]}: ")
            # Update the admin's details in the dataframe
            admin_data.at[0, admin_data.columns[i]] = dcc

        # Save the dataframe to the CSV file
        admin_data.to_csv('Admin_Data.csv', index=False)
        print("Admin details updated successfully.")
    elif data_change_choice.lower() == 'no':
        print("No changes made to admin details.")
    else:
        print("Invalid Option")


def graph():
    ad = patient_data['Gender'].tolist()
    mno = 0
    fno = 0
    for i in range(len(patient_data.Gender)):
        if ad[i] == 'M':
            mno += 1
        elif ad[i] == 'F':
            fno += 1
    l = ['M', "F"]
    l2 = [mno, fno]
    graph_choice = input("Which Type of Graph Do You Want For The Number of Patients(Bar/Line)?")
    if graph_choice.lower() == 'bar':
        plt.bar(l, l2, color=['blue', 'pink'], label=["BOYS", "GIRLS"])
        plt.title("Number of Patients Gender Wise(Bar)")
        plt.grid()
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.legend()
        plt.show()
    elif graph_choice.lower() == 'line':
        # Plotting the line graph
        plt.plot( l, l2, marker='o', linestyle='-', color='b', label=["Boys","Girls"])

        # Adding labels and title
        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title('Number of Patients Gender Wise(Line)')

        # Displaying legend
        plt.legend()

        # Show plot
        plt.grid(True)
        plt.show()
    else:
        print("Invalid Option")


def menu():
    while True:
        print("Select an Option:")
        print("1. Create Patient Account")
        print("2. Patient Login")
        print("3. Admin Login")
        print("4. Update Patient Details")
        print("5. Update Patient Details")
        print("6. Graph")
        print("7. Exit")
        option = int(input("Enter Option Number: "))

        if option == 1:
            create_patient_account()
        elif option == 2:
            create_admin_account()
        elif option == 3:
            patient_login()
        elif option == 4:
            update_patient_details()
        elif option == 5:
            graph()
        elif option == 6:
            graph()
        elif option == 7:
            break
        else:
            print("Invalid Option")





def admin_login():
    # Search for the admin in the dataframe
    login_id = int(input("Enter Your Login ID: "))
    login_pass = input("Enter your Password: ")
    result = admin_data[(admin_data["Admin_ID"] == login_id)
                        &
                        (admin_data["Admin_Password"] == login_pass.lower())]
    if result.empty:
        # Print the result
        print("You Are Not Registered Here")
        print("Please Register First")
    else:
        # Print the admin's details
        print("You Are Now Logged In")
        menu()
        

admin_login()

