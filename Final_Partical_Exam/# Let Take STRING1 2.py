# Let Take  STRING1 


string1 = input("Enter a string with letters and numbers: ")

# Initialize an empty string to store letters
letters_only = ""



# Use indexing to loop through the string
for i in range(len(string1)):
    
    if string1[i].isalpha():
        letters_only += string1[i]  




print("Letters extracted from the string:", letters_only)