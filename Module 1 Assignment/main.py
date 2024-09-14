import pandas

filename = "MDOT_MVA_Electric_and_Plug-in_Hybrid_Vehicle_Registrations_by_County_as_of_each_month_end_from_July_2020_to_August_2024_20240911.csv"

with open(filename, "r") as file:
    
    file = file.readlines()

    countyList = ["ALLEGANY","ANNE ARUNDEL","BALTIMORE CITY","BALTIMORE","CALVERT","CAROLINE","CARROLL","CECIL","CHARLES","DORCHESTER","FREDERICK","GARRETT","HARFORD","HOWARD","KENT","MONTGOMERY","PRINCE GEORGES","QUEEN ANNES","SAINT MARYS","SOMERSET","TALBOT","WASHINGTON","WICOMICO","WORCESTER"]

    cityData = dict()
    for entry in file[1:]:
        lineContents = entry.split(",")
        if lineContents[2] not in cityData and lineContents[2] != "(blank)" and lineContents[2] in countyList:
            cityData[lineContents[2]] = {
                "electric": 0,
                "plug-in hybrid": 0
            }
        elif lineContents[2] in countyList and lineContents[2] != "(blank)":
            cityData[lineContents[2]][lineContents[1].lower()] += int(lineContents[3].strip())

    evData = dict()
    phevData = dict()
    for city in cityData:
        evData[city] = cityData[city]["electric"]
        phevData[city] = cityData[city]["plug-in hybrid"]
    
    evData = sorted(evData, key = evData.get, reverse=True)
    phevData = sorted(phevData, key = phevData.get, reverse=True)

    print("Highest to Lowest Electric Vehicle (EV) Registration by County in MD")
    print("County | Electric")
    for city in evData:
        print(city, cityData[city]["electric"])

    print()
    print("Highest to Lowest Plug-in Hybrid Vehicle (PHEV) Registration by County in MD")
    print("County | Plug-in Hybrid")
    for city in phevData:
        print(city, cityData[city]["plug-in hybrid"])