import tkinter as tk
from tkinter import messagebox as msgBox
import csv
from Employee import Employee

class EmployeeApp(tk.Tk):
    def __init__(self, login_file, employee_file):
        #Initialize tk
        tk.Tk.__init__(self)
        
        #Initialize container options
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Initialize list to hold frames
        self.frames = {}

        #For each page
        for page in (LandingPage, LoginPage, EmployeeList, AddEmployee, EditEmployee, EmployeeProfile):
            #Initialize frame values
            page_name = page.__name__

            if page_name == "LoginPage":
                frame = page(parent = container, controller = self, landingPage = self.frames["LandingPage"])
            else:
                frame = page(parent = container, controller = self)

            self.frames[page_name] = frame

            #Stack each frame in same grid cell
            frame.grid(row = 0, column = 0, sticky = "nesw")

        #Show the login page
        self.present_frame("LoginPage")

    def present_frame(self, page_name):
        #Set the frame
        frame = self.frames[page_name]
        #Raise the frame to top of list
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller, landingPage):
        #username and password text boxes plus labels, save inputs to variables for future use
        #Set up the frame and create all buttons

        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        usernameLabel = tk.Label(self, text = "User Name").grid(row=3, column = 3)
        username = tk.StringVar()
        usernameInput = tk.Entry(self, textvariable = username).grid(row = 3, column = 4)
        passwordLabel = tk.Label(self, text = "Password").grid(row = 3, column = 7)
        password = tk.StringVar()
        passwordInput = tk.Entry(self, textvariable = password, show = '*').grid(row = 3, column = 8)
        
        #add login button, calls checkLogin
        loginButton = tk.Button(self, text = "Login", command = lambda: controller.present_frame("LandingPage")).grid(row = 8, column = 5)
        
    #Will call up a warning box if the credentials are invalid
    def failLogin(self):
         msgBox.showwarning(title="Failed Login", message="Incorrect Username or Password")
         
    #Will call to remove the Frame
    def removeLogin(self):
        pass
        
    #Inputs will be passed in here to verify validity
    #Will finish implementation when username and password csv are completed
    def checkLogin(self, username, password):
       #placeholder for veryifying the user and password
       #results = checkCredential(username, password)
       #if results is true:
       #LandingPage.makePage(self)
       #loginPage.removeLogin()
       #else:
         
        #self.failLogin()
        return

class LandingPage(tk.Frame):
    #Constructor class
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        self.userID = None
        self.loginCommand = None
        
        #Set the format of the buttons and all of their locations
        logoutButton = tk.Button(self, text = "Logout", command = lambda: controller.present_frame("LoginPage"))
        logoutButton.grid(row = 5, column = 3)
        profileButton = tk.Button(self, text = "Go to Profile", command = lambda: controller.present_frame("EmployeeProfile"))
        profileButton.grid(row = 2, column = 0)
        employeeButton = tk.Button(self, text ="Go to Employee Page", command = lambda: controller.present_frame("EmployeeList"))
        employeeButton.grid(row = 2, column = 5)

    def setUserID(self, id):
        self.userID = id

    def setLoginCommand(self, command):
        self.loginCommand = command
    
    #Once implemented this command will take the user to his personal profile
    #Currently unavailable
    def onProfileClicked(self):
        return
    
    #Once implemented this command will take a user with higher permission to a list of Employees page
    #Currently unavailable
    def onEmployeeClicked(self):
        return
    
    #Construct the frame
    def makePage(self):
        self.frame.grid()
    
    #This command will return the user to the login page and remove the current frame
    def onLogoutClicked(self):
        self.removePage()
        self.loginCommand()
        
    #Command to remove frame
    def removePage(self):
        self.frame.grid_forget()

class EmployeeList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #self.employees_database = employees_database
        tk.Label(self, text = "Search Employee ", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = tk.W)
        self.searchBox = tk.Entry(self, width = 73, bg = "white").grid(row=2, column =0, sticky = tk.NW)
        self.searchButton = tk.Button(self, text = "Search", width = 20, bg = "white", command = self.searchEmployee)
        self.searchButton.grid(row= 2, column = 0, sticky = tk.NE)
        
        self.search_Results = ["John Morgan        #91423", "Spencer Crow       #83523"]
        self.resultBox = tk.Listbox(self, width = 100, bg = "white")
        self.resultBox.grid(row=3, column =0, sticky = tk.NW)
        self.selectedEmployee = None
        
        #populate the search Results
        for item in self.search_Results:
            self.resultBox.insert(tk.END, item)
        #event handler for when clicked. selectEmployee()
        self.resultBox.bind("<<ListboxSelect>>", self.selectEmployee)
        
        self.addEmployeeButton = tk.Button(self, text = "Add Employee", width = 20, bg = "white", command = lambda: controller.present_frame("AddEmployee"))
        self.addEmployeeButton.grid(row=4, column= 0, sticky = tk.NW)
        
        self.editEmployeeButton = tk.Button(self, text = "Edit Employee", width = 20, bg = "white", command = lambda: controller.present_frame("EditEmployee"))
        self.editEmployeeButton.grid(row=5, column= 0, sticky = tk.NW)

        self.payrollButton = tk.Button(self, text = "Payroll", width = 20, bg = "white", command = lambda: controller.preset_frame("payrollFrame"))
        self.payrollButton.grid(row=4, column= 0, sticky = tk.E)

        self.exportEmployeeButton = tk.Button(self, text = "Export Employee", width = 20, bg = "white", command = lambda: controller.present_frame("exportEmployee"))
        self.exportEmployeeButton.grid(row=5, column= 0, sticky = tk.E)

        
        #copys the selected employee to selectedEmployee
    def selectEmployee(self, event):
        self.selectedEmployee = self.resultBox.get(tk.ACTIVE)
        print(self.selectedEmployee)
        
    def searchEmployee(self):
        pass

class AddEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        title_label = tk.Label(self, text="Add Employee").grid(row=0, columnspan=2, pady=10, sticky= tk.N)

        edit_first_name_label = tk.Label(self, text="First Name:").grid(row=1, column=0, pady=5, sticky= tk.W)
        edit_first_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=1, column=1)
        edit_last_name_label = tk.Label(self, text="Last Name:").grid(row=2, column=0, pady=5, sticky=tk.W)
        edit_last_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=2, column=1)
        edit_street_label = tk.Label(self, text="Street:").grid(row=3, column=0, pady=5, sticky=tk.W)
        edit_street_entry = tk.Entry(self, width = 15, bg = "white").grid(row=3, column=1)
        edit_city_label = tk.Label(self, text="City:").grid(row=4, column=0, pady=5, sticky=tk.W)
        edit_city_entry = tk.Entry(self, width = 15, bg = "white").grid(row=4, column=1)
        edit_state_label = tk.Label(self, text="State:").grid(row=5, column=0, pady=5, sticky=tk.W)
        edit_state_entry = tk.Entry(self, width = 15, bg = "white").grid(row=5, column=1)
        edit_zip_label = tk.Label(self, text="Zip:").grid(row=6, column=0, pady=5, sticky=tk.W)
        edit_zip_entry = tk.Entry(self, width = 15, bg = "white").grid(row=6, column=1)
        edit_phone_label = tk.Label(self, text="Phone:").grid(row=7, column=0, pady=5, sticky=tk.W)
        edit_phone_entry = tk.Entry(self, width = 15, bg = "white").grid(row=7, column=1)
        edit_routing_number_label = tk.Label(self, text="Routing Number:").grid(row=8, column=0, pady=5, sticky=tk.W)
        edit_routing_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=8, column=1)
        edit_account_number_label = tk.Label(self, text="Accounting Number:").grid(row=9, column=0, pady=5, sticky=tk.W)
        edit_account_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=9, column=1)
        edit_payment_method_label = tk.Label(self, text="Pay Method:").grid(row=10, column=0, pady=5, sticky=tk.W)
        edit_payment_method_entry = tk.Entry(self, width = 15, bg = "white").grid(row=10, column=1)
        submit_button = tk.Button(self, text="Submit", command = self.save_info).grid(row=11, column=1, pady=15)
        cancel_button = tk.Button(self, text="Cancel", command = self.save_info).grid(row=11, column=0)

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
        popup = tk.Tk()
        popup.wm_title("Saved")
        label = tk.Label(popup, text="Employee data will be saved")
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        #todo
        #Save data to database
        #Return to previous frame

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False

class EditEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        title_label = tk.Label(self, text="Edit Employee - Will be populated with employee info").grid(row=0, columnspan=2, pady=10, sticky=tk.N)

        edit_first_name_label = tk.Label(self, text="First Name:").grid(row=1, column=0, pady=5, sticky=tk.W)
        edit_first_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=1, column=1)
        edit_last_name_label = tk.Label(self, text="Last Name:").grid(row=2, column=0, pady=5, sticky=tk.W)
        edit_last_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=2, column=1)
        edit_street_label = tk.Label(self, text="Street:").grid(row=3, column=0, pady=5, sticky=tk.W)
        edit_street_entry = tk.Entry(self, width = 15, bg = "white").grid(row=3, column=1)
        edit_city_label = tk.Label(self, text="City:").grid(row=4, column=0, pady=5, sticky=tk.W)
        edit_city_entry = tk.Entry(self, width = 15, bg = "white").grid(row=4, column=1)
        edit_state_label = tk.Label(self, text="State:").grid(row=5, column=0, pady=5, sticky=tk.W)
        edit_state_entry = tk.Entry(self, width = 15, bg = "white").grid(row=5, column=1)
        edit_zip_label = tk.Label(self, text="Zip:").grid(row=6, column=0, pady=5, sticky=tk.W)
        edit_zip_entry = tk.Entry(self, width = 15, bg = "white").grid(row=6, column=1)
        edit_phone_label = tk.Label(self, text="Phone:").grid(row=7, column=0, pady=5, sticky=tk.W)
        edit_phone_entry = tk.Entry(self, width = 15, bg = "white").grid(row=7, column=1)
        edit_routing_number_label = tk.Label(self, text="Routing Number:").grid(row=8, column=0, pady=5, sticky=tk.W)
        edit_routing_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=8, column=1)
        edit_account_number_label = tk.Label(self, text="Accounting Number:").grid(row=9, column=0, pady=5, sticky=tk.W)
        edit_account_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=9, column=1)
        edit_payment_method_label = tk.Label(self, text="Pay Method:").grid(row=10, column=0, pady=5, sticky=tk.W)
        edit_payment_method_entry = tk.Entry(self, width = 15, bg = "white").grid(row=10, column=1)
        submit_button = tk.Button(self, text="Submit", command = self.save_info).grid(row=11, column=1, pady=15)
        cancel_button = tk.Button(self, text="Cancel", command= self.save_info).grid(row=11, column=0)

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
        popup = tk.Tk()
        popup.wm_title("Saved")
        label = tk.Label(popup, text="Employee data will be saved")
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        #todo
        #Save data to database
        #Return to previous frame


    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False

class EmployeeProfile(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller
       
        tk.Label(self, text="[Employee Name]",justify='center').grid(column=0, row=0, columnspan=3)
        tk.Label(self, text="[Employee ID number]",justify='center').grid(column=0, row=1, columnspan=3)
        tk.Label(self, text="[position] -- [department]").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self, text="Office Phone: (555) 555-5555").grid(column=0, row=3, columnspan=1, sticky=tk.W)
        tk.Label(self, text="Email: sample@uvu.edu").grid(row=4, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self, text=' ').grid(row=5,column=0)

        if self.check_permission(23): #the logged-in employee's number will be passed in
            tk.Label(self, text='<<Other employee info>>').grid(row=6, column=0, sticky=tk.W)
            tk.Button(self, text="Edit Employee", command=self.standIn).grid(column=1, row=10)

        tk.Button(self, text="Back", command = lambda: controller.present_frame("LandingPage")).grid(column=2, row=10)
    
    def standIn():
        pass

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False

def main():
    login_file = 'login.csv'
    data_file = 'data.csv'

    app = EmployeeApp(login_file, data_file)
    app.mainloop()

if __name__ == "__main__":
    main()






































#class EditPage(tk.Frame):
#    def __init__(self, parent, controller, employees):
#        #Initialize tk
#        tk.Frame.__init__(self, parent)

#        #Initialize controller
#        self.controller = controller

#        #Set window title
        

#        #Initialize values
#        self.CLEARED_STATE = True
#        self.EMPLOYEES = employees
#        self.LAST_FIVE_EMPLOYEES = []
#        self.CURRENT_EMPLOYEE = "none"

#        #Design frame

#        #Create a textbox prompt
#        tk.Label(self, text = "Enter an employee ID: ", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = tk.W)
#        self.inputbox = tk.Entry(self, width = 15, bg = "white")
#        self.inputbox.grid(row = 2, column = 0, sticky = tk.W)
#        tk.Button(self, text = "SUBMIT", width = 6, command = self._click_input).grid(row = 3, column = 0, sticky = tk.W)
#        tk.Button(self, text = "CLEAR", width = 6, command = self._clear_textboxes).grid(row = 3, column = 0, sticky = tk.N)
#        tk.Button(self, text = "DELETE", fg = "red", width = 6, command = self._click_delete).grid(row = 3, column = 1, sticky = tk.E)

#        #Create text for employee information title
#        tk.Label(self, text="\nEmployee information: ", fg = "black", font = "none 12 bold").grid(row = 5, column = 0, sticky = tk.W)

#        #Create textbox for employee id
#        tk.Label(self, text = "\nEmployee ID: ", fg = "black", font = "none 12").grid(row = 6, column = 0, sticky = tk.W)
#        self.outputbox_id = tk.Entry(self, width = 15, background = "white")
#        self.outputbox_id.grid(row = 7, column = 0, columnspan = 2, sticky = tk.W)
#        tk.Button(self, text = "SAVE", width = 6, command = self._new_click_id).grid(row = 7, column = 0, sticky = tk.E)

#        #Create texbox for employee name
#        tk.Label(self, text = "\nEmployee Name: ", fg = "black", font = "none 12").grid(row = 8, column = 0, sticky = tk.W)
#        self.outputbox_name = tk.Entry(self, width = 15, background = "white")
#        self.outputbox_name.grid(row = 9, column = 0, columnspan = 2, sticky = tk.W)
#        tk.Button(self, text = "SAVE", width = 6, command = self._click_name).grid(row = 9, column = 0, sticky = tk.E)

#        #Create textbox for employee pay type
#        tk.Label(self, text = "\nEmployee Pay Type: ", fg = "black", font = "none 12").grid(row = 10, column = 0, sticky = tk.W)
#        self.outputbox_pay_type = tk.Entry(self, width = 15, background = "white")
#        self.outputbox_pay_type.grid(row = 11, column = 0, columnspan = 2, sticky = tk.W)
#        tk.Button(self, text = "SAVE", width = 6, command = self._click_pay_type).grid(row = 11, column = 0, sticky = tk.E)

#        #Create textbox for employee pay rate
#        tk.Label(self, text = "\nEmployee Pay Rate: ", fg = "black", font = "none 12").grid(row = 12, column = 0, sticky = tk.W)
#        self.outputbox_pay_rate = tk.Entry(self, width = 15, background = "white")
#        self.outputbox_pay_rate.grid(row = 13, column = 0, columnspan = 2, sticky = tk.W)
#        tk.Button(self, text = "SAVE", width = 6, command = self._click_pay_rate) .grid(row = 13, column = 0, sticky = tk.E)

#        #Create textbox for employee start date
#        tk.Label(self, text = "\nEmployee Start Date: ", fg = "black", font = "none 12").grid(row = 14, column = 0, sticky = tk.W)
#        self.outputbox_start_date = tk.Entry(self, width = 15, background = "white")
#        self.outputbox_start_date.grid(row = 15, column = 0, columnspan = 2, sticky = tk.W)
#        tk.Button(self, text = "SAVE", width = 6, command = self._click_start_date).grid(row = 15, column = 0, sticky = tk.E)

#        #Create textbox for last 5 employees
#        tk.Label(self, text = "\nLast 5 Employees: ", fg = "black", font = "none 12").grid(row = 16, column = 0, sticky = tk.W)
#        self.outputbox_five_ids = tk.Entry(self, width = 20, background = "white")
#        self.outputbox_five_ids.grid(row = 17, column = 0, columnspan = 2, sticky = tk.W)

#    #Validate name input
#    def is_valid_name(self, str):
#        for c in str:
#            if not (c.isalpha() or c.isspace()):
#                return False

#        return True

#    #Fetch employee
#    def get_employee(self, id):
#        #Initialize CSV reader
#        with open(self.EMPLOYEES, 'r', newline = '') as read_file:
#            reader = csv.reader(read_file, delimiter = ',')

#            #If there is a current employee and current employee ID is the same as inputed ID
#            if (self.CURRENT_EMPLOYEE != 'none') and (self.CURRENT_EMPLOYEE.getID() == id):

#                return True

#            #For each line in CSV file
#            for row in reader:
#                #If ID is found
#                if row[0] == id:
#                    #Update current employee
#                    self.CURRENT_EMPLOYEE = Employee(row[0], row[1], row[2], row[3], row[4])

#                    return True

#            return False

#    #Submit button functionality
#    def _click_input(self):
#        #Clear previous info
#        self._clear_textboxes()

#        #Save textbox contents
#        entered_text = self.inputbox.get()

#        #If able to fetch an employee
#        if self.get_employee(entered_text):
#            #Display employee info
#            self._output_info()
#            #Frame display state not cleared
#            self.CLEARED_STATE = False

#            #If inputed ID is not in last five list
#            if self.LAST_FIVE_EMPLOYEES.count(int(entered_text)) == 0:
#                #Insert inputed ID in last five list
#                self.LAST_FIVE_EMPLOYEES.insert(0, int(entered_text))

#            #If last five list length more than 5
#            if len(self.LAST_FIVE_EMPLOYEES) > 5:
#                #Remove the last element
#                self.LAST_FIVE_EMPLOYEES.pop()

#            #Display last 5 IDs
#            self._output_last_five_ids()

#        #Unable to fetch employee
#        else:
#            #Clear previous info
#            self._clear_textboxes()

#            #If no ID entered
#            if entered_text == "":
#                msgBox.showerror("Error", "No ID entered")
#            #If invalid number
#            elif not entered_text.isdigit():
#                msgBox.showerror("Error", "Invalid ID entered")
#            #Employee is not in data file
#            else:
#                msgBox.showerror("Error", "Employee not found")

#    #New click delete
#    def _click_delete(self):
#        #If there is no current employee
#        if self.CLEARED_STATE == True or self.CURRENT_EMPLOYEE == "none":
#            #Show error
#            msgBox.showerror("Error", "No ID entered")
#        #There is a current employee
#        else:
#            #Create list to hold data
#            data = list()

#            #Open file to read in
#            with open(self.EMPLOYEES, 'r', newline = '') as read_file:
#                #Initialize CSV reader
#                reader = csv.reader(read_file, delimiter = ',')

#                #For each line in CSV file
#                for row in reader:
#                    #If ID is not ID to delete
#                    if row[0] != self.CURRENT_EMPLOYEE.getID():
#                        #Add row to data list
#                        data.append(row)

#            #Open file to write in
#            with open(self.EMPLOYEES, 'w', newline = '') as write_file:
#                #Inititalize writer
#                writer = csv.writer(write_file)
#                #Write data list to file
#                writer.writerows(data)

#            #Reset current employee
#            self.CURRENT_EMPLOYEE = "none"
#            #Clear entry boxes
#            self._clear_textboxes()

#            #Show message
#            msgBox.showinfo("Info", "Employee deleted")
    
#    #ID save button functionality
#    def _click_id(self):
#        #Save textbox contents
#        entered_text = self.outputbox_id.get()

#        found = False

#        if self.CLEARED_STATE == False:
#            for x in self.EMPLOYEES:
#                if str(x.getID()) == entered_text:
#                    self._clear_textboxes()
#                    msgBox.showerror("Error", "Employee ID already in use")
#                    found = True
#                    break;

#            if found == False:
#                if entered_text.isdigit():
#                    #Set employee id
#                    self.CURRENT_EMPLOYEE.setID(entered_text)
#                else:
#                    self._clear_textboxes()
#                    msgBox.showerror("Error", "Invalid ID entered")

#    def _new_click_id(self):
#        #Save textbox contents
#        entered_text = self.outputbox_id.get()

#        #If frame state is cleared
#        if self.CLEARED_STATE == True or self.CURRENT_EMPLOYEE == "none":
#            #Show error
#            msgBox.showerror("Error", "No ID entered")

#        #Current valid employee
#        else:
#            #Initialize list to hold data
#            data = List()
#            error = False

#            #Open file to read
#            with open(self.EMPLOYEES, 'r', newline = '') as read_file:
#                #Initialize CSV reader
#                reader = csv.reader(read_file, delimiter = ',')

#                #For each lrow in CSV file
#                for row in reader:
#                    #Add row to data list
#                    data.append(row)

#                    #If new ID is in use 
#                    if row[0] == entered_text:
#                        #Set error
#                        error = True

#                        break

#            if error == False:
#                #Open file to write
#                with open(self.EMPLOYEES, 'w', newline = '') as write_file:
#                    #Initialize CSV writer
#                    writer = csv.writer(write_file)


#            else:
#                #Show error
#                msgBox.showerror("Error", "ID already in use")
#                #Clear textboxes
#                self._clear_textboxes()
        
#    #Name save button funcitonality
#    def _click_name(self):
#        #Save textbox contents
#        entered_text = self.outputbox_name.get()

#        if self.CLEARED_STATE == False:
#            if not self.is_valid_name(entered_text):
#                self._clear_textboxes()
#                msgBox.showerror("Error", "Invalid name")
#            else:
#                entered_text = entered_text.title()
#                self.CURRENT_EMPLOYEE.setName(entered_text)

#    #Pay type save button functionality
#    def _click_pay_type(self):
#        #Save textbox contents
#        entered_text = self.outputbox_pay_type.get()

#    #Pay rate save button functionality
#    def _click_pay_rate(self):
#        #Save textbox contents
#        entered_text = self.ouputBoxPayRate.get()

#    #Start date save button functionality
#    def _click_start_date(self):
#        #Save textbox contents
#        entered_text = self.ouputboxPayRate.get()

#    #Fill employee info in entry boxes
#    def _output_info(self):
#        self.outputbox_id.insert(0, self.CURRENT_EMPLOYEE.getID())
#        self.outputbox_name.insert(0, self.CURRENT_EMPLOYEE.getName())
#        self.outputbox_pay_type.insert(0, self.CURRENT_EMPLOYEE.getPayType())
#        self.outputbox_pay_rate.insert(0, self.CURRENT_EMPLOYEE.getPayRate())
#        self.outputbox_start_date.insert(0, self.CURRENT_EMPLOYEE.getStartDate())

#    #Clear entry boxes
#    def _clear_textboxes(self):
#        self.outputbox_id.delete(0, tk.END)
#        self.outputbox_name.delete(0, tk.END)
#        self.outputbox_pay_type.delete(0, tk.END)
#        self.outputbox_pay_rate.delete(0, tk.END)
#        self.outputbox_start_date.delete(0, tk.END)
#        self.CLEARED_STATE = True

#    #Fill last 5 employee IDs
#    def _output_last_five_ids(self):
#        self.outputbox_five_ids.delete(0, tk.END)
#        self.outputbox_five_ids.insert(0, str(self.LAST_FIVE_EMPLOYEES))