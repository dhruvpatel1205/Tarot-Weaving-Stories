import json
import random
import os
from webapp import app


def findFortuneTellingByName(name):
    #print('name : ', name)
    filename = os.path.join(app.static_folder, 'tarot.json')

    f = open(filename)
    data = json.load(f)

    for iterator in data:
        if (iterator == "tarot_interpretations"):
            itemsOut = data[iterator]

            for i in range(len(itemsOut)):
                if (itemsOut[i]['name'] == name):
                    myArraay = itemsOut[i]['meanings']
                    myFirst = itemsOut[i]['story']['light']['infinitive']
                    # myPasts = itemsOut[i]['story']['shadow']['past']

                    # myKeyword = itemsOut[i]['']

                    #print(myFirst, random.choice(myArraay['light']) + " " + random.choice(myArraay['shadow']))
                    return myFirst + " " + random.choice(myArraay['light']) + " " + random.choice(myArraay['shadow'])
    f.close()


# findFortuneTellingByName("The Fool")

def findFortuneTellingByNameReversed(name):
    #print('name : ', name)
    filename = os.path.join(app.static_folder, 'tarot.json')

    f = open(filename)
    data = json.load(f)

    for iterator in data:
        if (iterator == "tarot_interpretations"):
            itemsOut = data[iterator]

            for i in range(len(itemsOut)):
                if (itemsOut[i]['name'] == name):
                    myArraay = itemsOut[i]['meanings']
                    myFirstl = itemsOut[i]['story']['light']['past']
                    myFirsts = itemsOut[i]['story']['shadow']['past']

                    # myKeyword = itemsOut[i]['']

                    print(myFirstl, myFirsts,
                          random.choice(myArraay['light']) + " " + random.choice(myArraay['shadow']))
                    return myFirstl + " " + myFirsts + " " + random.choice(myArraay['light']) + " " + random.choice(
                        myArraay['shadow'])
    f.close()
