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
