#Student Name: Benjamin Brumm (W0305413)  
#Program Title: IT Database Administration
#Description: TechCheck1 

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    print("*************************************")
    print("*                                   *")
    print("*  Welcome to Jane's Resturant!     *")
    print("*                                   *")
    print("*************************************")
    # Here I wrote the title/introduction for the console.

    
    billAmount = float(input("Please, enter your original bill amount: $"))
    # Here I created a program that requests the amount for the original bill. 
    tipPercentage = float(input("Please, enter the percent you would like to tip (e.g., 15 for 15%): %"))
    # Here I created a prompt for the input of the percentage that the customer is looking to tip for the meal
    taxAmount = (15/100)*billAmount
    # Here is a calculation for the tax amount based on the first entry of the bill total.
    tipAmount = (tipPercentage/100)*billAmount
    # Here is a calculation for the tip amount based on the first entry of the bill total
    totalAmount = billAmount+tipAmount+taxAmount
    # This calculation shows the sum of all amounts, into the final cost


    print("=====================================================")
    print(f"| Cost before tax: ${billAmount:.2f}                          |")
    # Here is the output of the bill amount before tax. I used a format to describe to the computer that I will be entering a float/integer value, along with a .2 for cents.
    print(f"| Tax amount: ${taxAmount:.2f}                                |")
    # I repeated the same process for the bill amount here, but entered the tax amount instead.
    print(f"| Tip amount: ${tipAmount:.2f}                                |")
    # Same as the top two, but with tip amount.
    print(f"| The total amount after tip and tax is: ${totalAmount:.2f}    |")
    # Here is the final amount which is being printed as a float with two decimals for cents. It was previously configured with the sum of all amounts listed (tip, tax, and bill).
    print("=====================================================")


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()