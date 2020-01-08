import extraction as ex
import write


def testExtraction():
    result = ex.extractFromFile("05gfp.txt", 6)
    print(result[3])


def testWriteToCSV():
    rating = ['0g', 'Bestplacestovisitin2019', '3', '1', '0g', 'MostpopularfoodsinAmerica', '2', '1', '0g', 'Daylightsavingstime', '1', '0', '0g', 'GlobalWarming', '5', '0', '0g', 'Bestrestaurantsinsanfrancisco', '4', '0', '0g', 'HowisAlmondmilkmade', '3', '0', '0g', 'Whatisagoodcreditscore', '2', '1', '0g', 'Top10easiestrecipes', '1', '0', '0g', 'Lastminutehalloweencostumeideas', '5', '0', '0g', 'Bestsmartphone2019', '4', '0', '01gfp', 'HowcanIsendmoneytosomeone', '3', '0', '01gfp', 'Bestplacestovisitin2019', '2', '0', '01gfp',
              'MostpopularfoodsinAmerica', '1', '0', '01gfp', 'Daylightsavingstime', '5', '0', '01gfp', 'GlobalWarming', '4', '0', '01gfp', 'Bestrestaurantsinsanfrancisco', '3', '0', '01gfp', 'HowisAlmondmilkmade', '2', '0', '01gfp', 'Whatisagoodcreditscore', '1', '1', '01gfp', 'Top10easiestrecipes', '5', '0', '01gfp', 'Lastminutehalloweencostumeideas', '4', '0', '05gfp', 'Bestsmartphone2019', '3', '0', '05gfp', 'RecipeforMacandCheese', '2', '1', '05gfp', 'Topnews', '1', '1', '05gfp', 'Universityrankings2019', '5', '5', '05gfp',
              'Upcomingmarvelmovies', '4', '1', '05gfp', 'Amazonprime', '3', '0', '05gfp', 'Worldhealthorganization', '2', '0', '05gfp', 'Billboardtop100', '1', '0', '05gfp', 'Worldseries2019', '1', '11', '05gfp', 'Mustseemovies', '5', '0', '09gfp', 'Mustseemovies', '4', '0', '09gfp', 'RecipeforMacandChese', '3', '1', '09gfp', 'Topnews', '2', '1', '09gfp', 'Universityrankings2019', '1', '1', '09gfp', 'Upcomingmarvelmovies', '5', '0', '09gfp', 'Amazonprime', '4', '0', '09gfp', 'Worldhealthorganization', '3', '0', '09gfp',
              'Billboardtop100', '2', '0', '09gfp', 'Worldseries2019', '1', '0', '09gfp', 'Mustseemovies', '5', '0']
    respondent = ['18-21', 'male', 'highSchool', '127.0.0.1', 'test']
    #print(str(len(rating)))
    write.writeToCSVFiles(respondent,rating,respondent[4])


if __name__ == '__main__':
    testExtraction()

