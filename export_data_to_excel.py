import pandas
import openpyxl

customers =[
    {'name':'krishna','city':'bangalore','area':'vijayanagar','car':'i10'},
    {'name':'arjun','city':'bangalore','area':'whitefield','car':'duster'},
    {'name':'arjun','city':'bangalore','area':'whitefield','car':'duster'},
    {'name':'ajay','city':'ramanagara','area':'bidadi','car':'santro'},
    {'name':'pramod','city':'mysore','area':'jp nagar','car':'swift'},
    {'name':'shenoy','city':'bangalore','area':'kengeri','car':'polo'}
]

df=pandas.DataFrame(customers)
excel_file_path = "customers_sheet.xlsx"
try:
    df.to_excel(excel_file_path, index=False)

except PermissionError:
    print('Warning...!: File is in use, Please close the file and try again')

print(df)