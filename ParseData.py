#Author   :Debjit Ghosh
#Created  :10/26/2012

#global variables
episodes = []

#Create dictionary for variable ids
variableID = {}
variableID["1"] = "Blood pressure (diastolic)"
variableID["2"] = "Blood pressure (systolic)"
variableID["3"] = "Capillary refill rate (peripheral)"
variableID["4"] = "End-tidal CO2"
variableID["5"] = "Fraction inspired O2"
variableID["6"] = "Total Glascow coma score"
variableID["7"] = "Glucose"
variableID["8"] = "Heart Rate"
variableID["9"] = "pH"
variableID["10"] = "Respiratory Rate"
variableID["11"] = "Blood Oxygen Saturation (SaO2)"
variableID["12"] = "Temperature"
variableID["13"] = "Urine output"
variableID["14"] = "pH areterial"
variableID["15"] = "pH venous"

#Class Episode holds the episode info
class Episode:

    def __init__(self, datarow):
        
        self.epid = datarow[0]
        self.minutes = datarow[1]
        self.bucket = datarow[2]
        self.varid = datarow[3]
        self.value = datarow[4]
        self.valuescale = datarow[5]
        self.valueshift = datarow[6]
        self.valid = datarow[7]

    def write(self):
        
        print ('Episode info:', self.epid, self.minutes, self.bucket, self.varid,
        self.value, self.valuescale, self.valueshift, self.valid)

#Read the lines of the data file

def ReadDataFile():
    #Open data file physiologic-deid.csv
    datafile = open("physiologic-deid.csv")
    lines = datafile.readlines()
    return lines


#Create list of episodes
def CreateListOfEpisodes():
    global episodes
    datarows = ReadDataFile()
    counter = 0
    for row in datarows:
        episodes.append(Episode(row.rstrip().split(',')))
        counter += 1
        print(counter)

#Create class where for each episode id, we have a dictionary of all the episodes

#Return the list of episodes based on the variable id
def GetInfoByVarID(varID):
    ep_by_varid = []
    for episode in episodes:
        if episode.varid == varID:
            ep_by_varid.append(episode)

    return ep_by_varid


        
    



	

    
