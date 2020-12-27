# class 1
class Group_1:
    def __init__(self, V1):
        self.SCHOOL_YEAR = V1[0]
        self.DATA_LEVEL = V1[1]
        self.PUBLIC_OR_INDEPENDENT = V1[2]
        self.DISTRICT_NUMBER = V1[3]
        self.DISTRUCT_NAME = V1[4]
        self.SCHOOL_NUMBER = V1[5]
        self.SCHOOL_NAME = V1[6]
        self.FACILTY_TIPE = V1[7]
# class 2
class Group_2:
    def __init__(self, V2):
        self.SUBJECT_CATEGORY = V2[8]
        self.EXAM_SUBJECT = V2[9]
        self.COURSE_CODE = V2[10]
        self.GRADE = V2[11]
        self.SUB_POPULATION = V2[12]
        self.REQUIRED_OR_OPTIONAL = V2[13]
        self.MARK_TYPE = V2[14]
        self.NUMBER_OF_MARKS = V2[15]
# class 3
class Group_3:
    def __init__(self, V3):
        self.AVERAGE_PERCENT = V3[16]
        self.SUM_OF_MARKS = V3[17]
        self.NUMBER_OF_C_MINUS_OR_BETTER = V3[18]
        self.PERCENT_OF_C_MINUS_OR_BETTER = V3[19]
        self.NUMBER_OF_A = V3[20]
        self.PERCENT_OF_A = V3[21]
        self.NUMBER_OF_B = V3[22]
        self.PERCENT_OF_B = V3[23]
# class 4
class Group_4:
    def __init__(self, V4):
        self.NUMBER_OF_C_PLUS = V4[-8]
        self.PERCENT_OF_C_PLUS = V4[-7]
        self.NUMBER_OF_C = V4[-6]
        self.PERCENT_OF_C = V4[-5]
        self.NUMBER_OF_C_MINUS = V4[-4]
        self.PERCENT_OF_C_MINUS = V4[-3]
        self.NUMBER_OF_F = V4[-2]
        self.PERCENT_OF_F = V4[-1]
# Result class , which is inherited from above classes
class Result(Group_1, Group_2, Group_3, Group_4):
    def __init__(self, V1, V2, V3, V4):
        Group_1.__init__(self, V1)
        Group_2.__init__(self, V2)
        Group_3.__init__(self, V3)
        Group_4.__init__(self, V4)
# static method, which the six data given in the condition
    @staticmethod
    def ShowData(line):
        SCHOOL_YEAR = line[0]
        DISTRICT_NAME = line[4]
        SCHOOL_NAME = line[6]
        FACILITY_TYPE = line[7]
        GRADE = line[11]
        PERCENT_OF_A = line[21]
        PERCENT_OF_B = line[23]
        PERCENT_OF_C = line[-5]
        PERCENT_OF_F = line[7]

        print(" SCHOOL_YEAR : ", SCHOOL_YEAR,'\n',"DISTRICT_NAME : ", DISTRICT_NAME,'\n'
             , "FACILITY_TYPE : ", FACILITY_TYPE,'\n',"SCHOOL_NAME : ", SCHOOL_NAME,'\n'
             ,"GRADE : ", GRADE,'\n',"PERCENT_OF_A : ", PERCENT_OF_A,'\n',"PERCENT_OF_B : ", PERCENT_OF_B,'\n'
             ,"PERCENT_OF_C : ", PERCENT_OF_C,'\n',"PERCENT_OF_F : ", PERCENT_OF_F )

# static method, which prints only SCHOOL_YEAR 's data
    @staticmethod
    def S_SCHOOL_YEAR(line):
        SCHOOL_YEAR = line[0]
        print("SCHOOL_YEAR :", SCHOOL_YEAR)

# static method, which prints only DISTRICT_NAME 's data
    @staticmethod
    def S_DISTRICT_NAME(line):
        DISTRICT_NAME = line[4]
        print("DISTRICT_NAME :", DISTRICT_NAME)

# static method, which prints only SCHOOL_NAME 's data
    @staticmethod
    def S_SCHOOL_NAME(line):
        SCHOOL_NAME = line[6]
        print("SCHOOL_NAME :", SCHOOL_NAME)

# static method, which prints only FACILITY_TYPE 's data
    @staticmethod
    def S_FACILITY_TYPE(line):
        FACILITY_TYPE = line[7]
        print("FACILITY_TYPE :", FACILITY_TYPE)

# static method, which prints only GRADE 's data
    @staticmethod
    def S_GRADE(line):
        GRADE = line[11]
        print("GRADE :", GRADE)

# static method, which prints only OERCENT_OF_A 's data
    @staticmethod
    def S_PERCENT_OF_A(line):
        PERCENT_OF_A = line[21]
        print("PERCENT_OF_A :", PERCENT_OF_A)

# static method, which prints only PERCENT_OF_B 's data
    @staticmethod
    def S_PERCENT_OF_B(line):
        PERCENT_OF_B = line[23]
        print("PERCENT_OF_B :", PERCENT_OF_B)

# static method, which prints only PERCENT_OF_C 's data
    @staticmethod
    def S_PERCENT_OF_C(line):
        PERCENT_OF_C = line[-5]
        print("PERCENT_OF_C :", PERCENT_OF_C)

# static method, which prints only PERCENT_OF_F 's data
    @staticmethod
    def S_PERCENT_OF_F(line):
        PERCENT_OF_F = line[7]
        print("PERCENT_OF_F :", PERCENT_OF_F)

# main prog

#reading from file
with open("BC_data.in", "r") as f:
    arr = f.readlines()
# Enter the data we want to print from the keyboard
x = str(input("choose which data you need : "
                        "\n1) SCHOOL_YEAR"
                        "\n2) DISTRICT_NAME"
                        "\n3) SCHOOL_NAME"
                        "\n4) FACILITY_TYPE"
                        "\n5) GRADE"
                        "\n6) PERCENT_OF_A"
                        "\n7) PERCENT_OF_B"
                        "\n8) PERCENT_OF_C"
                        "\n9) PERCENT_OF_F "
                        "\n10) All Data"
                        "\n11) exit program\n"))
# for Loop, which makes it possible to convert data into an array into indexes
for line in arr:
    ResultClass = Result(line.split(), line.split(), line.split(), line.split())
# result Create a class object
     # ResultClass.S_SCHOOL_YEAR (line.split ()) # I call a static function that prints SCHOOL_YEAR data
     # ResultClass.S_DISTRICT_NAME (line.split ()) # I call a static function that prints DISTRICT_NAME data
# Conditions under which we select the in data we want to print
    if x == '1' or x == 'SCHOOL_YEAR':
       ResultClass.S_SCHOOL_YEAR(line.split())
    elif x == '2' or x == 'DISTRICT_NAME':
        ResultClass.S_DISTRICT_NAME(line.split())
    elif x == '3' or x == 'SCHOOL_NAME':
        ResultClass.S_SCHOOL_NAME(line.split())
    elif x == '4' or x == 'FACILITY_TYPE':
        ResultClass.S_FACILITY_TYPE(line.split())
    elif x == '5' or x == 'GRADE':
        ResultClass.S_GRADE(line.split())
    elif x == '6' or x == 'PERCENT_OF_A':
        ResultClass.S_PERCENT_OF_A(line.split())
    elif x == '7' or x == 'PERCENT_OF_B':
        ResultClass.S_PERCENT_OF_B(line.split())
    elif x == '8' or x == 'PERCENT_OF_C':
        ResultClass.S_PERCENT_OF_C(line.split())
    elif x == '9' or x == 'PERCENT_OF_F':
        ResultClass.S_PERCENT_OF_F(line.split())
    elif x == '10' or x == 'All Data':
        ResultClass.ShowData(line.split())
    elif x == '11' or x == 'exit':
        exit(-1)


















