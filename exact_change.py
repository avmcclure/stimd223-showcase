def exact_change(amount):
    cents = round(amount * 100) #Dollars to cents

    #Defines currency both int and str
    currency = [1000, 500, 100, 25, 10, 5, 1]  #Currency in cents
    currency_string = ["$10 bill", "$5 bill", "$1 bill", "quarter", "dime", "nickel", "penny"]

    for i in range(len(currency)):
        if cents >= currency[i]: 
            count = cents // currency[i]  
            cents %= currency[i]  
            print(f"{count} - {currency_string[i]}") #prints

def main():
    #User inputs
    amount = float(input("Enter an amount of money: "))
    cents = round(amount * 100) #Dollars to cents

    #Defines currency both int and str
    currency = [1000, 500, 100, 25, 10, 5, 1]  #Currency in cents
    currency_string = ["$10 bill", "$5 bill", "$1 bill", "quarter", "dime", "nickel", "penny"]

    for i in range(len(currency)):
        if cents >= currency[i]:
            count = cents // currency[i]
            cents %= currency[i]
            print(f"{count} - {currency_string[i]}") #prints

if __name__ == "__main__":
    main()