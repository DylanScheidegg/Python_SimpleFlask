import os
import json
import re

# Change direct to program's folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open("Sixers.json") as f:
   json_data = f.read()

sixers = json.loads(json_data)  # json loads method

open("SixersFixed.json", "w").close()


class SixersCheck(object):
    def __init__(self, url, name, pos, age, height, weight, college, salary):
        self.id = 0
        self.num = 0
        self.fName = ""
        self.lName = ""
        self.url = url
        self.name = name
        self.pos = pos
        self.age = age
        self.height = height
        self.weight = weight
        self.college = college
        self.salary = salary
        self.imgURL = ""

    def update(self):
        self.splitUrlId()
        self.splitName()
        self.splitNum()
        self.convertHeightMeters()
        self.convertWeightKilo()
        self.fixSalary()
        self.createURL()

        sixFixed = []
        try:
            with open("SixersFixed.json") as f:
                jsonFixed = f.read()

            sixFixed = json.loads(jsonFixed)  # json loads method
        except:
            pass

        dataSet = {"FNAME": self.fName, "LNAME": self.lName, "ID": self.id, "NUM": self.num, "POS": self.pos, "AGE": self.age, "HT": self.height, "WT": self.weight, "COLLEGE": self.college, "IMGURL": self.imgURL, "PROFURL": self.profURL, "SALARY": self.salary}

        sixFixed.append(dataSet)

        # Writes remaining data to json file
        with open("SixersFixed.json", "w") as f:
            f.write(json.dumps(sixFixed, indent=4))

    def splitUrlId(self):
        url = re.sub(r"https://a.espncdn.com/i/headshots/nba/players/full/", "", self.url)
        url = re.sub(r".png", "", url)
        self.id = int(url)

    def splitName(self):
        name = re.sub(r"\d", "", self.name)
        name = name.split(" ")
        self.fName = name[0]
        self.lName = name[1]

    def splitNum(self):
        num = re.sub(r"[A-Za-z]", "", self.name)
        num = re.sub(r"\s+", "", num)
        self.num = num

    def convertHeightMeters(self):
        height = re.sub(r"\"", "", self.height)
        height = height.split("'")

        inch = int(height[0]) * 12 + int(height[1])
        self.height = inch

    def convertWeightKilo(self):
        weight = re.sub(r"lbs", "", self.weight)
        self.weight =  int(weight) / 2.205
    
    def fixSalary(self):
        sal = ""
        for x in self.salary:
            # print(x)
            try:
                salMoney = re.sub(r"\$", '', str(x))
                sal += salMoney  
            except:
                pass
    
        try:
            self.salary = "${:,.2f}".format(int(sal))
        except:
            self.salary = sal
        # print(self.salary)

    def createURL(self):
        self.imgURL =  "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/" + str(self.id) + ".png&w=350&h=254"
        self.profURL = "https://www.espn.com/nba/player/_/id/" + str(self.id) + "/" + self.fName + "-" + self.lName


for x in sixers:
    sixer = SixersCheck(x["URL"], x["NAME"], x["POS"], x["AGE"], x["HT"], x["WT"], x["COLLEGE"], [x["SALARY"], x[""], x["__1"]])
    sixer.update()
