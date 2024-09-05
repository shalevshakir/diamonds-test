import pandas as pd



def mostexpensive(csv_file):
    # קריאת הקובץ
    df = pd.read_csv(csv_file)
    
    # מציאת המספר הגדול ביותר בעמודה
    max_value = df["price"].max()
    
    return max_value
 #פונקצייה שנותנת לנו ממוצע מחיר של כל היהלומים 
def avgdiamondprice(csv_file ):
  
    df = pd.read_csv(csv_file)
   
    average_value = df['price'].mean()
    
    return average_value

def howmanyideal():
    pass

def colorsandcount():
    pass
def hetsion():
    pass

def avgcarinanycat():
    pass
def avgpriceforcolor():
    pass



