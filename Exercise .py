class School:
    def __init__(self, SCHOOL_YEAR ,DATA_LEVEL ,PUBLIC_OR_INDEPENDENT ,DISTRICT_NUMBER ,DISTRUCT_NAME ,SCHOOL_NUMBER ,SCHOOL_NAME ,FACILTY_TIPE):
        self.SCHOOL_YEAR = SCHOOL_YEAR
        self.DATA_LEVEL = DATA_LEVEL
        self.PUBLIC_OR_INDEPENDENT = PUBLIC_OR_INDEPENDENT
        self.DISTRICT_NUMBER = DISTRICT_NUMBER
        self.DISTRUCT_NAME =DISTRUCT_NAME
        self.SCHOOL_NUMBER =SCHOOL_NUMBER
        self.SCHOOL_NAME = SCHOOL_NAME
        self.FACILTY_TIPE =FACILTY_TIPE

class Subject:
    def __init__(self, SUBJECT_CATEGORY,EXAM_SUBJECT ,COURSE_CODE ,GRADE,SUB_POPULATION ,REQUIRED_OR_OPTIONAL, MARK_TYPE ,NUMBER_OF_MARKS):
        self.SUBJECT_CATEGORY = SUBJECT_CATEGORY
        self.EXAM_SUBJECT = EXAM_SUBJECT 
        self.COURSE_CODE = COURSE_CODE
        self.GRADE = GRADE
        self.SUB_POPULATION = SUB_POPULATION
        self.REQUIRED_OR_OPTIONAL = REQUIRED_OR_OPTIONAL
        self.MARK_TYPE =MARK_TYPE
        self.NUMBER_OF_MARKS = NUMBER_OF_MARKS
        
class Average:
    def __init__(self,AVERAGE_PERCENT ,SUM_OF_MARKS ,NUMBER_OF_C_MINUS_OR_BETTER ,PERCENT_OF_C_MINUS_OR_BETTER , NUMBER_OF_A ,PERCENT_OF_A, NUMBER_OF_B,PERCENT_OF_B):
        self.AVERAGE_PERCENT = AVERAGE_PERCENT
        self.SUM_OF_MARKS =SUM_OF_MARKS 
        self.NUMBER_OF_C_MINUS_OR_BETTER = NUMBER_OF_C_MINUS_OR_BETTER
        self.PERCENT_OF_C_MINUS_OR_BETTER =PERCENT_OF_C_MINUS_OR_BETTER
        self.NUMBER_OF_A = NUMBER_OF_A 
        self.PERCENT_OF_A = PERCENT_OF_A
        self.NUMBER_OF_B = NUMBER_OF_B
        self.PERCENT_OF_B = PERCENT_OF_B
        
class Numbers:
    def __init__(self, NUMBER_OF_C_PLUS,PERCENT_OF_C_PLUS ,NUMBER_OF_C ,PERCENT_OF_C,NUMBER_OF_C_MINUS,PERCENT_OF_C_MINUS,NUMBER_OF_F ,PERCENT_OF_F  ):
        self.NUMBER_OF_C_PLUS = NUMBER_OF_C_PLUS
        self.PERCENT_OF_C_PLUS = PERCENT_OF_C_PLUS
        self.NUMBER_OF_C = NUMBER_OF_C
        self.PERCENT_OF_C = PERCENT_OF_C
        self.NUMBER_OF_C_MINUS = NUMBER_OF_C_MINUS
        self.PERCENT_OF_C_MINUS =PERCENT_OF_C_MINUS 
        self.NUMBER_OF_F = NUMBER_OF_F
        self.PERCENT_OF_F = PERCENT_OF_F 
# Result class , which is inherited from above classes
class Result(School, Subject, Average, Numbers):
    def __init__(self):
        School.__init__(self)
        Subject.__init__(self)
        Average.__init__(self)
        Numbers.__init__(self)
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


















