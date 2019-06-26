kmhIn = input("Insert the speed in kmh: ")

def convert(kmh):
    message1 = "Speed converted : "
    message2 = " in km/h is "
    message3 = " in Miles/h."
    mph = (kmh/1.609)
    return message1 + str(kmh) + message2 + str(mph) + message3
print(convert(float(kmhIn)))
if float(kmhIn)> 120:
    print("Attention at the Policeman")

##autre syntaxe
def convert2(kmh):
    return "Speed converted : " + str(kmh) + " in km/h is " + str(kmh/1.609) + " in Miles/h."
if float(kmhIn)> 120:
    print("Attention at the Policeman")
print(convert2(float(kmhIn)))



