from enum import Enum
from diamondsfunctions import  mostexpensive,avgdiamondprice,avgcarinanycat,avgpriceforcolor

class options (Enum):
    show_highest_diamond_price=1 
    show_avrage_diamond_price=2
    show_ideal_diamonds_count=3
    show_which_color_and_count_of_every_color=4
    something=5
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
        if userselection== options.avg_price_for_color:pass
        if userselection== options.show_avrage_diamond_price:
            csv_file="diamonds.csv"
            avg_price= avgdiamondprice(csv_file)
            print(avg_price)
        if userselection==options.show_highest_diamond_price:
            csv_file="diamonds.csv"
            highestprice=mostexpensive(csv_file)
            print(highestprice)
        if userselection==options.show_ideal_diamonds_count:pass
        if userselection==options.show_which_color_and_count_of_every_color:pass
        if userselection==options.something:pass
        if userselection==options.exit:exit()

   