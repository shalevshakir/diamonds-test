from enum import Enum
from diamondsfunctions import  mostexpensive,avgdiamondprice,howmanyideal,diamondcolor,median_of_carat

class options (Enum):
    show_highest_diamond_price=1 
    show_avrage_diamond_price=2
    show_ideal_diamonds_count=3
    show_diamond_colors=4
    median_of_carat=5
    avg_carat_in_any_cat=6
    avg_price_for_color=7
    exit=8


def menu():
    for item in options: print(f"{item.value}-{item.name}")
    return options(int(input("your selection")))


if __name__=="__main__":

    while True:
        userselection=menu()

        if userselection==options.avg_carat_in_any_cat:pass
        elif userselection== options.avg_price_for_color:pass
        elif userselection== options.show_diamond_colors:
            colors = diamondcolor()
            print(colors)
        elif userselection== options.show_avrage_diamond_price:
            csv_file="diamonds.csv"
            avg_price= avgdiamondprice(csv_file)
            print(avg_price)
        elif userselection==options.show_highest_diamond_price:
            csv_file="diamonds.csv"
            highestprice=mostexpensive(csv_file)
            print(highestprice)
        elif userselection==options.show_ideal_diamonds_count:
            csv_file = 'diamonds.csv'
            ideal_count = howmanyideal(csv_file)
            print(ideal_count)   
         
            
        elif userselection==options.median_of_carat:
            medcarat =  median_of_carat()
            print(medcarat)
        elif userselection==options.exit:exit()

   