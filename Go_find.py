# Import required libraries
import csv
import pandas as pd
import random
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization

class Person:
  def __init__(self,name,min,max):
    self.name = name
    self.min = min
    self.max = max
# Obteining input from user
print("Please enter your name\n")
name = input()
print("Hi", name)
print("\nPlease enter minimum price you want to search")
min = input()
print("\nPlease enter maximum price you want to search")
max = input()

p1 = Person(name,min,max)

#Constatns set for the purpose of searching
daft = Daft()
daft.set_location(Location.COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN)
daft.set_sort_type(SortType.PRICE_ASC)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)
#user input
daft.set_min_price(min)
daft.set_max_price(max)

listings = daft.search(max_pages=1)

# Assigning location  to be our CCT 
cct = [53.346203924833866, -6.258907486506016]
listings.sort(key=lambda x: x.distance_to(cct))


# Loop to show list of advertisings in range 1km from colege
for listing in listings:
    print(f'{listing.title}')
    print(f'{listing.daft_link}')
    print(f'{listing.price}')
    print(f'{listing.distance_to(cct):.1}km')
    print('')

listings = daft.search()


# saving listings in the local csv file
with open("best_acomodation.csv", "w") as fp:
    fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

# read from the local csv file
with open("best_acomodation.csv") as fp:
  lines = fp.readlines()

print ("\n Results")

# Creating visualisation on the map using dataframe
properties = []
for line in lines:
  properties.append(eval(line))

df = pd.DataFrame(properties)
print(df)

dublin_map = MapVisualization(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("dublin_student_map.html")
print("\nDone, list it's just above. Csv file with all student acommodation\n",
        "available aroud CCT college in your price range is downloaded. Map is ready too!")


print("\n Do you want to use our random suggestion? [y/n]\n")

decision = input()

# funcion to find random row in dataset 
if decision == 'y':
      with open("best_acomodation.csv") as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        print(chosen_row)
      rd = pd.DataFrame(chosen_row)
      print(rd) 
      print("\n Our bet for you, enjoy your live in Dublin",name,"Bye, bye")
else:
      print("\nEnjoy your live in Dublin",name," Bye, bye")




