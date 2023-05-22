import worldometer;
#Ranges
def checki_deaththisyear () :
    deathincrement = 0
    tempstat = worldometer.deaths_this_year
    deathincrement = worldometer.deaths_this_year - tempstat

def checki_deathstoday () :
    deathincrement = 0
    tempstat = worldometer.deaths_today
    deathincrement = worldometer.deaths_today - tempstat
    
def checki_deathbyalcohol () :
    deathincrement = 0
    tempstat = worldometer.deaths_caused_by_alcohol_this_year
    deathincrement = worldometer.deaths_caused_by_alcohol_this_year - tempstat

def checki_deathsbysmoking () :
    deathincrement = 0
    tempstat = worldometer.deaths_caused_by_smoking_this_year
    deathincrement = worldometer.deaths_caused_by_smoking_this_year - tempstat
    












