import requests

# key making function
def createCustomKey(item):
    customKey = item.replace(' ', '')
    return customKey.lower()

# state class
class State:
    # state properties
    id = ""
    country  = ""
    name = ""
    abbr = ""
    area = ""
    largestCity = ""
    capital = ""

    # state Instance
    def __init__(self, id, country, name, abbr, area, largest_city, capital):
        self.id = id
        self.country = country
        self.name = createCustomKey(name)
        self.abbr = createCustomKey(abbr)
        self.area = area
        self.largestCity = largest_city
        self.capital = capital

# fetch API Data
def fetchAPIData():

    stateDataDictionary = {}
    stateNameAbbrDictionary = {}

    print "--------------------"
    print "Fetching Data"

    # make a request for data
    requestObject = requests.get("http://services.groupkt.com/state/get/USA/all")
    if requestObject.status_code == 200:
        responseData = requestObject.json()

        # parse JSON response
        restResponse = responseData["RestResponse"]
        messages = restResponse["messages"]
        result = restResponse["result"]

        for item in result:
            state = State(item["id"], item["country"], item["name"], item["abbr"], item["area"], item["largest_city"], item["capital"])
            stateDataDictionary[state.name] = state
            stateNameAbbrDictionary[state.abbr] = state.name

        print "Data successfully fetched."
        print "--------------------"

    return stateDataDictionary, stateNameAbbrDictionary

# prepare user input
def prepareForUserInput():
    # endless loop for user input
    while True:
        userInput = raw_input("Enter state name : ")
        searchableKey = createCustomKey(userInput)

        if userInput == "exit":
            break
        elif len(userInput) >= 2:
            state, errorMessage = getStateInformation(searchableKey)
            if (state is not None):
                print '\n##############\nLargest City : ' + state.largestCity + '.\nCapital : ' + state.capital + '\n##############\n'
            else:
                print errorMessage

# search state info
def getStateInformation(stateNameOrAbbr):
        if len(stateNameOrAbbr) == 2 and (stateNameOrAbbr in stateNameAbbrDictionary):
            stateName = stateNameAbbrDictionary[stateNameOrAbbr]
            return stateDataDictionary[stateName], None
        elif len(stateNameOrAbbr) > 0 and (stateNameOrAbbr in stateDataDictionary):
            return stateDataDictionary[stateNameOrAbbr], None
        else:
            return None, '\n##############\nState not found, please try again.\n##############\n'


#####
# Main Start Here
#####

print '\n##############\nNOTE: \nSearch any state info of USA.\nType "exit" to stop program. \n##############\n'
# 1. fetch API Data
stateDataDictionary, stateNameAbbrDictionary = fetchAPIData()

# 2. preparing for search
if (stateNameAbbrDictionary is not None) and (stateDataDictionary is not None):
    prepareForUserInput()



