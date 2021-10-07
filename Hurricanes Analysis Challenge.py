# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def updated_damages(lst):
  updated = []
  for damage in lst:
    if damage == "Damages not recorded":
      updated.append(damage)
    elif damage[-1] =='B':
      updated.append(float(damage[:-1])*conversion["B"])
    elif damage[-1] =='M':
      updated.append(float(damage[:-1])*conversion["M"])  
  return updated
# test function by updating damages
upd_damage =updated_damages(damages)

# 2 
# Create a Table
def create_dic(name, month, year,max_sustained_wind, areas_affected,upd_damage, death):
  hurricane = dict()
  for i in range(len(name)):
    hurricane[name[i]] ={"Name": name[i], "Month": month[i], "Year": year[i],"Max Sustained Wind" : max_sustained_wind[i], "Areas Affected": areas_affected[i] , "Damage":upd_damage[i], "Death":death[i]}
  return hurricane  

hurricane = create_dic(names, months, years,max_sustained_winds, areas_affected, upd_damage, deaths)

# Create and view the hurricanes dictionary
print(create_dic(names, months, years,max_sustained_winds, areas_affected, damages, deaths))
# 3
# Organizing by Year
def dic_by_year(dic):
  hurricane_year= dict()
  
  for name,detail in dic.items():
    new_key = detail['Year']
    current_year = new_key
    current_detail = detail
    if new_key not in hurricane_year:
      hurricane_year[new_key] = [detail]
    else:
      hurricane_year[new_key].append(detail)     
  return hurricane_year
    
# # create a new dictionary of hurricanes with year and key
hurricanes_by_year = dic_by_year(hurricane)
print("\n",hurricanes_by_year[1932])


# 4
# Counting Damaged Areas
def count_areas(areas_affected):
  dic_area={}
  for area in areas_affected:
    for item in area:
      c=0
      if item in dic_area:
        c= dic_area.get(item)
        dic_area.update({item: c+1})
        continue
      dic_area.update({item: c+1})
  return dic_area  

# create dictionary of areas to store the number of hurricanes involved in
print("dictionary by Area", count_areas(areas_affected))

# 5 
# Calculating Maximum Hurricane Count
def count_max(dic_area):
  max_area= ""
  max_count=0
  for key,value in dic_area.items():
    if max_count < value :
      max_count = value
      max_area = key
  return  max_area, max_count



# find most frequently affected area and the number of hurricanes involved in
dic_area = count_areas(areas_affected)
print(count_max(dic_area))

# 6
# Calculating the Deadliest Hurricane
def deadliest(hurricane):
  max_death=0
  deadly_cane=""
  for key,value in hurricane.items():
    if max_death < value["Death"]:
      max_death = value["Death"]
      deadly_cane = key
  return deadly_cane, max_death   



# find highest mortality hurricane and the number of deaths
deadly_cane, max_death = deadliest(hurricane)
print(deadly_cane, max_death)
# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes):
  """Categorize hurricanes by mortality and return a dictionary."""
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    num_deaths = hurricanes[cane]['Death']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricane)
print(hurricanes_by_mortality[5])

# 8 Calculating Hurricane Maximum Damage

def max_damage(hurricane):
  max_damage=0.0
  deadly_cane=""
  for key,value in hurricane.items():
    if value['Damage'] != "Damages not recorded":
      if max_damage < value["Damage"]:
        max_damage = value["Damage"]
        deadly_cane = key
  return deadly_cane, max_damage   

# find highest damage inducing hurricane and its total cost
deadly_cane, max_damage = max_damage(hurricane)
print(deadly_cane, max_damage)
# 9
# Rating Hurricanes by Damage
def rating_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage = {0:[], 1:[], 2:[] , 3: [], 4:[],5:[] }

  for cane,details in hurricanes.items():
    total_damage = hurricanes[cane]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage
                 
  
# categorize hurricanes in new dictionary with damage severity as key
print("\n Hurricanes rated by severity of damage\n", rating_by_damage(hurricane))
