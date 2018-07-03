#CTI - 110
#P5T1 Kilometer Converter
#Robert Charity
#070318

def main():
    program='true'
    while program== 'true':
        choice=str(input("Would you like to convert kilometers into miles? "))
        while choice=='y':
            show_miles()
            break
        while choice!='y':
            program= 'false'
            break

def show_miles():
    km=float(input("Input your the amount of Kilometers to be converted into miles: "))
    print(km * .6214)
    


main()    
