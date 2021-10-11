import  math
def convertDegrees(radians):
    return math.degrees(radians)

def convertRadians(degrees):
    return math.radians(degrees)


radians = 3.14159
degrees = 90.0
print(degrees," this degress is ",convertRadians(degrees),"radians")
print(degrees," this radians is ",convertRadians(degrees),"degress")