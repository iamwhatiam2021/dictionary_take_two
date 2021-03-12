import dictionary

#def transalte(engspn):
 #   """
#
 #   :param engspn: english: spanish
  #  :return: translated words
  #  """
#words = (english(spanish))

#for words in engspn.lower().split():

print(dictionary.engspn)

#reference = "english number"
#translate = ""
#numbers = reference.split()
#for n in numbers:
    #translate = translate + "" + dictionary.engspn[n]

#print(translate)

engspn = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro","five": "cinco", "six": "seis", "seven": "siete", "eight": "ocho", "nine": "nueve", "ten": "diez"}
#data = engspn.lower().split()
#data = engspn[('\n').split(' ')]
data = splitString=engspn.split('\n')

def define(number):
    number = number.lower()
    if number in data:
        return data[number]
    elif number.title() in data:
        return data[number.title()]
    elif number.upper() in data:
        return data[number.upper()]
    elif  len(number,data.keys()) > 0 :
        yn = input("Did you mean %s instead? Enter Y if yes and N if no: " % (number, data.keys())[0].upper())
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The number is not found"
        else:
            return "The input is outside the database"

    else :
        return ("You entered a wrong number, please check it.")


word=input("Enter any word to know its meaning : ")
output = (define(word))

if type(output) == list :
    for item in output:
        print(item)
else :
    print (output)