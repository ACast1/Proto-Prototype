class Employee:
    def __init__(self, id, name, payType, rate, startDate):
        self.id = id
        self.name = name
        self.payType = payType
        self.rate = rate
        self.startDate = startDate

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPayType(self, payType):
        self.payType = payType

    def getPayType(self):
        return self.payType

    def setPayRate(self, rate):
        self.rate = rate

    def getPayRate(self):
        return self.rate

    def setStartDate(self, startDate):
        self.startDate = startDate

    def getStartDate(self):
        return self.startDate

    def getEmployeeInfo(self):
        payType = ""

        if self.payType == "salary":
            payType = "Annual Salary: "
        else:
            payType = "Hourly Wage: "

        return "ID: " + str(self.id) + "\n" + "Name: " + self.name + "\n" + payType + str(self.rate) + "\n" + "Date Hired: " + str(self.startDate)
