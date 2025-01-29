# checks on pandas library
try:
    import pandas as pd # import module
except ModuleNotFoundError: # if not present, suggest user to install it
    print("module 'pandas' is not installed")
    print("run the command 'pip3 install pandas'")
    exit()

# load File Manually
file = input("insert .csv file name: ")
print("inserted {} file".format(file))
print("")

# import csv using pandas
dataf = pd.read_csv(file, sep=",")
# print(dataf) # optional, better not to print out the database on terminal. Sensitive data!

# accept one column name or multiple. Use split to dtype list.
col = input(f'I have individuated {dataf.columns.to_list()} columns name.\nSelect the column to check for duplicates\n(NB: for multiple parameters write i.e. "login_url,password" separated by a comma and no whitespaces. Don\'t include quotes)\n').split(",")

datafc = dataf.drop_duplicates(subset=col, keep='first') # use builtin pandas function to search for duplicates within the db

# informative print
print("The initial file had {} records. The cleaned csv has {} records. Removed {} records".format(len(dataf.index),len(datafc.index),len(dataf.index)-len(datafc.index)))
fileout = "pass_no_dupli.csv" # so here should be much better to implement os.getcwd() and os.path.join(pwd, 'pass_no_dupli.csv') to ensure path out to be in same folder as script
print(f"{fileout} generated")
datafc.to_csv(fileout, index=False) # actual extraction
