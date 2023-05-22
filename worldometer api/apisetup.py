import worldometer
import numpy
#Ranges
deathincrement = numpy.array([0,0,0,0,0,0,0,0])

def checki_deathstoday () :
    tempstat = worldometer.deaths_today
    deathincrement [0] = worldometer.deaths_today - tempstat
    if ( deathincrement [0] >= 5000 ) :
        deathincrement [0] = 0
        return True
    else :
        return False
    
def checki_deaththisyear () :
    tempstat = worldometer.deaths_this_year
    deathincrement [1] = worldometer.deaths_this_year - tempstat
    if ( deathincrement [1] >= 10000 ) :
        deathincrement [1] = 0
        return True
    else :
        return False

def checki_deathbyalcohol () :
    tempstat = worldometer.deaths_caused_by_alcohol_this_year
    deathincrement [2] = worldometer.deaths_caused_by_alcohol_this_year - tempstat
    if ( deathincrement [2] >= 50  ) :
        deathincrement [2] = 0
        return True
    else :
        return False

def checki_deathsbysmoking () :
    tempstat = worldometer.deaths_caused_by_smoking_this_year
    deathincrement [3] = worldometer.deaths_caused_by_smoking_this_year - tempstat
    if ( deathincrement [3] > 100 ) :
        deathincrement [3] = 0
        return True
    else :
        return False

def checki_deathsbyhiv () :
    tempstat = worldometer.deaths_caused_by_hiv_aids_this_year
    deathincrement [4] = worldometer.deaths_caused_by_hiv_aids_this_year - tempstat
    if ( deathincrement [4] > 20 ) :
        deathincrement [4] = 0
        return True
    else :
        return False

def checki_deathsbycancer () :
    tempstat = worldometer.deaths_caused_by_cancer_this_year
    deathincrement [5] = worldometer.deaths_caused_by_cancer_this_year - tempstat
    if ( deathincrement [5] > 30 ) :
        deathincrement [5] = 0
        return True
    else :
        return False

def checki_deathsofmothers () :
    tempstat = worldometer.deaths_of_mothers_during_birth_this_year
    deathincrement [6] = worldometer.deaths_of_mothers_during_birth_this_year - tempstat
    if ( deathincrement [6] > 20 ) :
        deathincrement [6] = 0
        return True
    else :
        return False

def checki_deathsofchildren () :
    tempstat = worldometer.deaths_of_children_under_5_this_year
    deathincrement [7] = worldometer.deaths_of_children_under_5_this_year - tempstat
    if ( deathincrement [7] > 10 ) :
        deathincrement [7] = 0
        return True
    else :
        return False














