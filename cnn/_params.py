def test_animals():
    return {
        2: 'Cheval',
        3: 'Ecureuil',
        4: 'Kangourou',
        5: "Souris",
        6: "Chouette"
    }


def test_races():
    return {
        0: "Inconnu",
        1: "Rottweiler",
        2: "Saint-Bernard",
        3: "Terre-Neuve",
        4: "Epagneul Breton",
        5: "Angora Turc",
        6: "Bleu russe",
        7: "Donskoy",
        8: "Himalayen",
        9: "Sacré de Birmanie"
    }



class params:

    def dataset_folder_name(self):
        return 'dataset'

    def TRAIN_TEST_SPLIT(self):
        return 0.01

    def IM_WIDTH(self):
        return 50

    def dataset_dict(self):
        return {
            'espece_id': {
                0: 'Chien',
                1: 'Chat',
                2: 'Cheval',
                3: 'Ecureuil',
                4: 'Kangourou',
                5: "Souris",
                6: "Chouette"
            },
            'race_id': {
                0: "Inconnu",
                1: "Rottweiler",
                2: "Saint-Bernard",
                3: "Terre-Neuve",
                4: "Epagneul Breton",
                5: "Angora Turc",
                6: "Bleu russe",
                7: "Donskoy",
                8: "Himalayen",
                9: "Sacré de Birmanie"
            },
            'color_id': {
                0: 'default',
                1: 'blanc',
                2: 'noir',
                3: 'gris',
                4: 'marron'
            },
        }


"""
{
    'espece_id': {
        0: 'chien',
        1: 'chat',
    },
    'race_id': {
        0: 'male',
        1: 'female'
    },
    'color_id': {
        0: 'default',
        1: 'blanc',
        2: 'noir',
        3: 'gris',
        4: 'marron'
    },
}
"""




"""

def test_animals():
    return {
        2: 'Cheval',
        3: 'Ecureuil',
        4: 'Kangourou',
        5: "Souris",
        6: "Chouette"
    }


def test_races():
    return {
        0: "Inconnu",
        1: "Affenpinscher",
        2: "Labrador",
        3: "Labrador Retriever",
        4: "Rottweiler",
        5: "Saint-Bernard",
        6: "Terre-Neuve",
        7: "Epagneul Breton",
        8: "Whippet",
        9: "Yorkshire Terrier",
        11: "American Bully",
        12: "Beagle",
        14: "Boston Terrier",
        15: "Abyssin",
        16: "American Bobtail",
        17: "American Curl",
        18: "American Shorthair",
        19: "American Wirehair",
        20: "Angora Turc",
        21: "Asiatique",
        22: "Australian Mist",
        23: "Balinais",
        24: "Bengal",
        25: "Birman",
        26: "Bombay",
        27: "Bleu russe",
        28: "Donskoy",
        29: "German Rex",
        30: "Himalayen",
        31: "Havana Brown",
        32: "Sacré de Birmanie"
    }



class params:

    def dataset_folder_name(self):
        return 'dataset'

    def TRAIN_TEST_SPLIT(self):
        return 0.01

    def IM_WIDTH(self):
        return 250

    def dataset_dict(self):
        return {
            'espece_id': {
                0: 'Chien',
                1: 'Chat',
                2: 'Cheval',
                3: 'Ecureuil',
                4: 'Kangourou',
                5: "Souris",
                6: "Chouette"
            },
            'race_id': {
                0: "Inconnu",
                1: "Affenpinscher",
                2: "Labrador",
                3: "Retriever de la Nouvelle-Écosse",
                4: "Rottweiler",
                5: "Saint-Bernard",
                6: "Terre-Neuve",
                7: "Epagneul Breton",
                8: "Whippet",
                9: "Yorkshire Terrier",
                10: "Bobbycrouz",
                11: "American Bully",
                12: "Beagle Elisabeth",
                13: "Cursinu",
                14: "Boston Terrier",
                15: "Abyssin",
                16: "American Bobtail",
                17: "American Curl",
                18: "American Shorthair",
                19: "American Wirehair",
                20: "Angora Turc",
                21: "Asiatique",
                22: "Australian Mist",
                23: "Balinais",
                24: "Bengal",
                25: "Birman",
                26: "Bombay",
                27: "Bleu russe",
                28: "Donskoy",
                29: "German Rex",
                30: "Himalayen",
                31: "Havana Brown",
                32: "Sacré de Birmanie"
            },
            'color_id': {
                0: 'default',
                1: 'blanc',
                2: 'noir',
                3: 'gris',
                4: 'marron'
            },
        }




"""