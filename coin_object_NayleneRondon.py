#Naylene Rondon
#4/3/17
#Lab 8
import coin

def main():
    my_coin = coin.coin() #Create Object

    #Display

    print("This side is up: ", my_coin.get_side())

    #Toss the coin
    print("I'm going to toss the coin ten times!")
    for count in range(1,10):
        my_coin.toss()

        print(my_coin.get_side())

main()
    


