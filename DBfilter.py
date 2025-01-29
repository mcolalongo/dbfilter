# Checks on pandas library
try:
    import pandas as pd # pd mlmlmlml
except ModuleNotFoundError:
    print("module 'pandas' is not installed")
    print("run the command 'pip3 install pandas'")
    exit()

# Load File Manually
file = input("insert .csv file name: ")
print("inserted {} file".format(file))
print("")

# Import csv using pandas
dataf = pd.read_csv(file, sep=",")
print(dataf)

col = input(f'I have individuated {dataf.columns.to_list()} columns name.\nSelect the column to check for duplicates\n(NB: for multiple parameters write i.e. "login_url,password" separated by a comma and no whitespaces. Don\'t include quotes)\n').split(",")

datafc = dataf.drop_duplicates(subset=col, keep='first')

print("The initial file had {} records. The cleaned csv has {} records. Removed {} records".format(len(dataf.index),len(datafc.index),len(dataf.index)-len(datafc.index)))
fileout = "pass_no_dupli.csv"
print(f"{fileout} generated")
datafc.to_csv(fileout, index=False)
