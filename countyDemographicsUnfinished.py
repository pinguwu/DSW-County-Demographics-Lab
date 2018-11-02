import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(county_with_highest_income(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first_county = counties[0]["County"]
    for x in counties:
        if x["County"] < first_county:
            first_county = x["County"]
    return first_county


def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    most_under = counties[0]["County"]
    state = counties[0]["State"]
    percent = counties[0]["Age"]["Percent Under 18 Years"]
    for x in counties:
        if x["Age"]["Percent Under 18 Years"] > percent:
            most_under = x["County"]
            state = x["State"]
            percent = x["Age"]["Percent Under 18 Years"]
    return most_under + ", " + state

    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    most_under = counties[0]["County"]
    percent = counties[0]["Age"]["Percent Under 18 Years"]
    for x in counties:
        if x["Age"]["Percent Under 18 Years"] > percent:
            most_under = x["County"]
            percent = x["Age"]["Percent Under 18 Years"]
    return str(percent)
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    return county_most_under_18(counties) + ": " + percent_most_under_18(counties) + " are under 18 years old."
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #Find the state in the dictionary with the most counties
    
    #Return the state with the most counties

    los = {}

    for x in counties:
        state = x["State"]
        tf = state in los
        if (tf == False):
            los[state] = 0

        else:
            los[state] = los[state] + 1

    most = los["CA"]
    state = ""
    for x in los:
        if (los[x] > most):
            most = los[x]
            state = x

    return state + ": " + str(most) + " counties."
    
def county_with_highest_income(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    most_under = counties[0]["County"]
    state_most_under = counties[0]["State"]
    percent = counties[0]["Income"]["Median Household Income"]
    for x in counties:
        if (x["Income"]["Median Household Income"] > percent):
            most_under = x["County"]
            state_most_under = x["State"]
            percent = x["Income"]["Median Household Income"]
    return state_most_under + ", " + most_under + ": " + str(percent)

if __name__ == '__main__':
    main()
