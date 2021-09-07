open_file = open("CupcakeInvoices.csv")

print open_file

for line in open_file:
  line = line.rstrip('\n').split(',')
  print(line[2])
    
open_file.seek(0)


for line in open_file:
  line = line.rstrip('\n').split(',')
  total_invoice = float(line[3]) * float(line[4])
  print (total_invoice)

open_file.seek(0)


total_combined = 0.0

for line in open_file:
  line = line.rstrip('\n').split(',')
  total_invoice = float(line[3]) * float(line[4])
  total_combined += total_invoice

print total_combined

open_file.seek(0)

chocolate_sales = 0.0
vanilla_sales = 0.0 
strawberry_sales = 0.0

for line in open_file:
  line = line.rstrip('\n').split(',')
  if line[2] == "Chocolate":
    chocolate_sales += float(line[3]) * float(line[4])
  if line[2] == "Strawberry":
    strawberry_sales += float(line[3]) * float(line[4])
  if line[2] == "Vanilla":
    vanilla_sales += float(line[3]) * float(line[4])

print(chocolate_sales)
print(vanilla_sales)
print(strawberry_sales)

import matplotlib.pyplot as plt 

plt.plot([chocolate_sales, strawberry_sales, vanilla_sales])
plt.ylabel('Total Sales $$$')
plt.xlabel('Type of cupcake')
plt.show()
  
     
  
  
