import worldometer
import numpy
#Ranges
deathincrement = numpy.array([0,0,0,0,0,0,0,0])
tempstat = numpy.array ([0,0,0,0,0,0,0,0])

def checki_deathstoday () :
    if ( tempstat [0] == 0 ) :
        tempstat [0] = worldometer.deaths_today
    deathincrement [0] = worldometer.deaths_today - tempstat [0]
    if ( deathincrement [0] >= 5000 ) :
        deathincrement [0] = 0
        tempstat [0] = 0
        return True
    else :
        return False
    
def checki_deaththisyear () :
    if ( tempstat [1] == 0 ) :
        tempstat [1] = worldometer.deaths_this_year
    deathincrement [1] = worldometer.deaths_this_year - tempstat [1]
    if ( deathincrement [1] >= 10000 ) :
        deathincrement [1] = 0
        tempstat [1] = 0
        return True
    else :
        return False

def checki_deathbyalcohol () :
    if ( tempstat [2] == 0 ) :
        tempstat [2] = worldometer.deaths_caused_by_alcohol_this_year
    deathincrement [2] = worldometer.deaths_caused_by_alcohol_this_year - tempstat [2]
    if ( deathincrement [2] >= 50  ) :
        deathincrement [2] = 0
        tempstat [2] = 0
        return True
    else :
        return False

def checki_deathsbysmoking () :
    if ( tempstat [3] == 0 ) :
        tempstat [3] = worldometer.deaths_caused_by_smoking_this_year
    deathincrement [3] = worldometer.deaths_caused_by_smoking_this_year - tempstat [3]
    if ( deathincrement [3] > 100 ) :
        deathincrement [3] = 0
        tempstat [3] = 0
        return True
    else :
        return False

def checki_deathsbyhiv () :
    if ( tempstat [4] == 0 ) :
        tempstat [4] = worldometer.deaths_caused_by_hiv_aids_this_year
    deathincrement [4] = worldometer.deaths_caused_by_hiv_aids_this_year - tempstat [4]
    if ( deathincrement [4] > 20 ) :
        deathincrement [4] = 0
        tempstat [4] = 0
        return True
    else :
        return False

def checki_deathsbycancer () :
    if ( tempstat [5] == 0 ) :
        tempstat [5] = worldometer.deaths_caused_by_cancer_this_year
    deathincrement [5] = worldometer.deaths_caused_by_cancer_this_year - tempstat [5]
    if ( deathincrement [5] > 30 ) :
        deathincrement [5] = 0
        tempstat [5] = 0
        return True
    else :
        return False

def checki_deathsofmothers () :
    if ( tempstat [6] == 0 ) :
        tempstat [6] = worldometer.deaths_of_mothers_during_birth_this_year
    deathincrement [6] = worldometer.deaths_of_mothers_during_birth_this_year- tempstat [6]
    if ( deathincrement [6] > 20 ) :
        deathincrement [6] = 0
        tempstat[6] = 0
        return True
    else :
        return False

def checki_deathsofchildren () :
    if ( tempstat [7] == 0 ) :
        tempstat [7] = worldometer.deaths_of_children_under_5_this_year
    deathincrement [7] = worldometer.deaths_of_children_under_5_this_year - tempstat [7]
    if ( deathincrement [7] > 10 ) :
        deathincrement [7] = 0
        tempstat [7] = 0
        return True
    else :
        return False














