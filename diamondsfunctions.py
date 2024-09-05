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


def howmanyideal(csv_file):
     df = pd.read_csv(csv_file)
    
    #בודק כמה פעמים יש איידיאל בתוך השורה קאט
     count = df[df['cut'] == 'Ideal'].shape[0]
    
     return count


   

def diamondcolor():
    df = pd.read_csv("diamonds.csv")
    
    # מכניס לתוך מערך את רשימת הצבעים שקיבלנו
    unique_colors = df['color'].unique()
    
    return unique_colors

def median_of_carat():
    # קריאת הקובץ לתוך DataFrame
    df = pd.read_csv("diamonds.csv")
    
    # חישוב החציון של ערכי העמודה 'carat'
    median_carat = df['carat'].median()
    return median_carat

#TODO

def avgcarinanycat():
    pass
def avgpriceforcolor():
    pass



