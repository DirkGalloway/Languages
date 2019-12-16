import random
import time


def base_code():
    # -----------------------------------------------------------------------------------------------------------------
    # This code has been laid out as follows:

    # Defining all known words and sentences
    # Choosing random words and a sentence
    # Inputting chosen words into the sentence
    # Adjusting sentences with language caveats
    # Returning chosen sentence and translation

    # -----------------------------------------------------------------------------------------------------------------
    # Defining all known words and sentences

    # Sentences
    classify_sentences_array = [  # cqwd
        ["single_pronoun am/are/is a people_adjective people_noun", "he people_noun people_adjective single_pronoun"],
        ["plural_pronoun are people_adjective people_nouns", "he people_noun people_adjective plural_pronoun"],
        ["single_pos_def is a general_adjective general_noun", "he general_noun general_adjective single_pos_def"],
        ["plural_pos_def are general_adjective general_nouns", "he general_noun general_adjective plural_pos_def"],

        ["single_pronoun am/are/is lone_people_adjective", "he lone_people_adjective single_pronoun"],
        ["plural_pronoun are lone_people_adjective", "he lone_people_adjective plural_pronoun"],

        ["The general_noun is lone_general_adjective", "he lone_general_adjective te general_noun"],
        ["The general_nouns are lone_general_adjective", "he lone_general_adjective ngā general_noun"],
        ["The people_noun is lone_people_adjective", "he lone_people_adjective te people_noun"],
        ["The people_nouns are lone_people_adjective", "he lone_people_adjective ngā people_noun"],

        ["single_pos_def is lone_general_adjective", "he lone_general_adjective single_pos_def"],
        ["plural_pos_def are lone_general_adjective", "he lone_general_adjective plural_pos_def"]
    ]

    # Nouns
    people_noun_array = [["son", "tama"],
                         ["man", "tāne"],
                         ["dad", "pāpā"],
                         ["grandfather", "koroua"],
                         ["mother", "whaea"],
                         ["person", "tangata"],
                         ["boy", "tamaiti tāne"],
                         ["father", "matua"],
                         ["older sibling", "tuakana"],
                         ["younger sibling", "teina"],
                         ["mum", "māmā"],
                         ["girl", "hine"],
                         ["friend", "hoa"],
                         ["grandmother", "kui"],
                         ["grandchild", "mokopuna"],
                         ["child", "tamaiti"],
                         ["woman", "wahine"],
                         ["dog", "kurī"],
                         ["bird", "manu"],
                         ["cat", "ngeru"],
                         ["fish", "ika"],
                         ]
    general_noun_array = [["subtribe", "hapu"],
                          ["meeting", "hui"],
                          ["mountain", "maunga"],
                          ["river", "awa"],
                          ["lake", "roto"],
                          ["tree", "rākau"],
                          ["forest", "wao"],
                          ["island", "moutere"],
                          ["vehicle", "waka"],
                          ["house", "whare"],
                          ["harbour", "whanga"],
                          ["discussion", "kōrero"],
                          ["time", "wa"],
                          ["day", "rā"],
                          ["sea", "moana"],
                          ["food", "kai"],
                          ["table", "papa-kai"],
                          ["chair", "nohoanga"],
                          ["oven", "oumu"],
                          ["bus", "pahi"],
                          ["bread", "taro"],
                          ["key", "kī"],
                          ["door", "tatau"],
                          ["paper", "pepa"],
                          ["computer", "rorohiko"],
                          ["brain", "wairoro"],
                          ["table", "tepu"],
                          ["fire", "ahi"],
                          ["cushion", "aupuru"],
                          ["light", "marama"],
                          ["couch", "hōneanea"],
                          ["screen", "whakaruru"],
                          ["pillow", "pera"],
                          ["paper", "pepa"],
                          ["bicycle", "paihikara"],
                          ["window", "matapihi"],
                          ["car", "motoka"],
                          ["apple", "aporo"],
                          ["home", "kāinga"],
                          ["cup", "kapu"],
                          ["plate", "pereti"],
                          ["clothes", "kākahu"],
                          ["shoes", "hu"],
                          ["drink", "inu"],
                          ["fruit", "hua rākau"],
                          ["aeroplane", "waka rerangi"],
                          ["outside", "waho"],
                          ["toilet", "wharepaku"],
                          ["flower", "putiputi"],
                          ["surf", "auheke"],
                          ["sand", "kirikiri"],
                          ["grass", "pātītī"],
                          ["seagull", "karoro"],
                          ["ice cream", "aihikirīmi"],
                          ["barbecue", "kaihōhunu"],
                          ["idea", "whakaaro"],
                          ["funeral", "tangihanga"]]
    all_noun_array = general_noun_array + people_noun_array

    # Verbs
    verb_array = [["doing", "aha"],
                  ["coming", "haere"],
                  ["buying", "hoko"],
                  ["sleeping", "moe"],
                  ["swimming", "kaukau"],
                  ["running", "oma"],
                  ["washing", "horoi"],
                  ["writing", "tuhituhi"],
                  ["removing", "tango"],
                  ["acquiring", "tango"],
                  ["talking", "korero"],
                  ["cooking", "tunu"],
                  ["sitting", "noho"],
                  ["staying", "noho"],
                  ["flying", "rere"],
                  ["eating", "kai"],
                  ["waking up", "whakaara"],
                  ["making", "hanga"],
                  ["knows", "mōhio"],
                  ["seeing", "kite"],
                  ["looking", "titiro"],
                  ["wanting", "hiahia"],
                  ["asking", "pātai"],
                  ["hearing", "oko"],
                  ["understanding", "mārama"],
                  ["calling", "karanga"],
                  ["moving", "neke"],
                  ["playing", "tākaro"],
                  ["showing", "whakaata"],
                  ["listening", "whakarongo"],
                  ["rolling about", "takahurihuri"],
                  ["feeling", "whāwhā"],
                  ["screeching", "kirea"],
                  ["squabbling", "kohetehete"],
                  ["tasting", "reka"],
                  ["feeling", "whāwhā"],
                  ["smelling", "kakara"],
                  ["squealing", "pūkoto"],
                  ["becoming", "huri"],
                  ["grew up", "tipu ake"]]

    # Adjectives
    people_adjective_array = [["good", "pai"],
                              ["bad", "kino"],
                              ["strong", "kaha"],
                              ["beautiful", "ātaahua"],
                              ["small", "iti"],
                              ["fun", "whakangahau"],
                              ["well", "ora"],
                              ["sick", "māuiui"],
                              ["sleepy", "hiamoe"],
                              ["happy", "koa"],
                              ["sad", "pōuri"],
                              ["angry", "riri"],
                              ["hot", "wera"],
                              ["cold", "makariri"],
                              ["hungry", "hiakai"],
                              ["thirsty", "hianinu"],
                              ["frustrated", "hōhā"]]
    general_adjective_array = [["big", "nui"],
                               ["good", "pai"],
                               ["bad", "kino"],
                               ["strong", "kaha"],
                               ["long", "roa"],
                               ["beautiful", "ātaahua"],
                               ["fast", "tere"],
                               ["sweet", "reka"],
                               ["small", "iti"],
                               ["wide", "whānui"],
                               ["windy", "hauhau"],
                               ["cold", "mātao"],
                               ["gritty", "māngūngungu"],
                               ["grainy", "tōpata"],
                               ["fresh", "mata"],
                               ["fragrant", "ōngi"],
                               ["soft and sweet", "kuteretere"],
                               ["scarlet", "ngangana"],
                               ["sturdy", "mārōrō"],
                               ["fizzy", "koropupū"],
                               ["fun", "whakangahau"],
                               ["smokey", "mina-auahi"],
                               ["spicy", "namunamuā"],
                               ["ripe", "rōpere"],
                               ["gluggy", "paihukahuka"]]

    # Definitives
    single_pos_def_array = [["this", "tēnei"],
                            ["that", "tēnā"],
                            ["that", "tērā"]]
    plural_pos_def_array = [["these", "ēnei"],
                            ["those", "ēnā"],
                            ["those", "ērā"]]
    single_pronoun_array = [["I", "ahau", "am"],  # This one is special for now.
                            ["you", "koe", "are"],
                            ["she", "ia", "is"]]
    plural_pronoun_array = [["we (incl)", "tāua"],
                            ["we (excl)", "māua"],
                            ["you two", "kōrua"],
                            ["those two", "rāua"],
                            ["we three (incl)", "tātou"],
                            ["we three (excl)", "mātou"],
                            ["you three", "koutou"],
                            ["those three", "rātou"]]

    # Miscellaneous
    time_array = [["today", "nōnāianei"],
                  ["tomorrow", "ākengokengo"],
                  ["yesterday", "inanahi"]]
    direction_array = [["south", "tonga"]]
    name_array = ["Paul", "John", "George",
                  "Ringo", "Liverpool", "Aotearoa"]

    # -----------------------------------------------------------------------------------------------------------------
    # Choosing a random word/sentence from each array

    # Choosing a sentence
    sentence = random.choice(classify_sentences_array)

    # double_subject_flag = random.randint(0, 1)
    # if double_subject_flag == 0:
    #    pass

    # double_info_flag = random.randint(0, 1)
    # if double_info_flag == 0:
    #    pass

    # Choosing nouns
    general_noun = random.choice(general_noun_array)
    people_noun = random.choice(people_noun_array)
    all_noun = random.choice(all_noun_array)

    double_adjective_flag = random.randint(0, 1)
    if double_adjective_flag == 1:
        # Choosing required adjectives
        adj1 = random.choice(people_adjective_array)
        adj2 = random.choice(people_adjective_array)
        lone_people_adjective = [adj1[0] + " and " + adj2[0], adj1[1] + " " + adj2[1]]
        lone_people_adjective = random.choice(people_adjective_array)  # stuupid
        lone_general_adjective = random.choice(general_adjective_array)
        # Choosing optional adjectives
        people_adjective = ["", ""]
        general_adjective = ["", ""]
        adjective_flag = random.randint(0, 1)
        if adjective_flag == True:
            people_adjective = random.choice(people_adjective_array)
            general_adjective = random.choice(general_adjective_array)
    else:
        # Choosing required adjectives
        lone_people_adjective = random.choice(people_adjective_array)
        lone_general_adjective = random.choice(general_adjective_array)

        # Choosing optional adjectives
        people_adjective = ["", ""]
        general_adjective = ["", ""]
        adjective_flag = random.randint(0, 1)
        if adjective_flag == True:
            people_adjective = random.choice(people_adjective_array)
            general_adjective = random.choice(general_adjective_array)

    # Choosing positional definitives
    single_pos_def = random.choice(single_pos_def_array)
    plural_pos_def = random.choice(plural_pos_def_array)

    # Choosing pronouns
    single_pronoun = random.choice(single_pronoun_array)
    plural_pronoun = random.choice(plural_pronoun_array)

    # verb = random.choice(verb_array)
    # time = random.choice(time_array)
    # direction = random.choice(direction_array)
    # name = random.choice(name_array)

    # -----------------------------------------------------------------------------------------------------------------
    # Inputting chosen words into the sentence

    # Inputting all nouns. Note that some nouns are only used in conjunction with people.
    sentence[0] = sentence[0].replace("general_noun", general_noun[0])
    sentence[0] = sentence[0].replace("people_noun", people_noun[0])
    sentence[0] = sentence[0].replace("all_noun", all_noun[0])
    sentence[1] = sentence[1].replace("general_noun", general_noun[1])
    sentence[1] = sentence[1].replace("people_noun", people_noun[1])
    sentence[1] = sentence[1].replace("all_noun", all_noun[1])

    # Inputting all adjectives. Note that lone adjectives are not optional, but adjectives in adj-noun combos are.
    sentence[0] = sentence[0].replace("lone_people_adjective", lone_people_adjective[0])
    sentence[0] = sentence[0].replace("lone_general_adjective", lone_general_adjective[0])
    sentence[0] = sentence[0].replace("general_adjective", general_adjective[0])
    sentence[0] = sentence[0].replace("people_adjective", people_adjective[0])
    sentence[1] = sentence[1].replace("lone_people_adjective", lone_people_adjective[1])
    sentence[1] = sentence[1].replace("lone_general_adjective", lone_general_adjective[1])
    sentence[1] = sentence[1].replace("general_adjective", general_adjective[1])
    sentence[1] = sentence[1].replace("people_adjective", people_adjective[1])

    # Inputting positional definitives "This, that"
    sentence[0] = sentence[0].replace("single_pos_def", single_pos_def[0])
    sentence[0] = sentence[0].replace("plural_pos_def", plural_pos_def[0])
    sentence[1] = sentence[1].replace("single_pos_def", single_pos_def[1])
    sentence[1] = sentence[1].replace("plural_pos_def", plural_pos_def[1])

    # Inputting all pronouns.
    sentence[0] = sentence[0].replace("single_pronoun", single_pronoun[0])
    sentence[0] = sentence[0].replace("am/are/is", single_pronoun[2])  # Refer to single pronoun array
    sentence[0] = sentence[0].replace("plural_pronoun", plural_pronoun[0])
    sentence[1] = sentence[1].replace("single_pronoun", single_pronoun[1])
    sentence[1] = sentence[1].replace("plural_pronoun", plural_pronoun[1])

    # -----------------------------------------------------------------------------------------------------------------
    # Adjusting sentences with language caveats

    # Fixing a / an issue
    sentence[0] = sentence[0].replace(" a a", " an a")
    sentence[0] = sentence[0].replace(" a e", " an e")
    sentence[0] = sentence[0].replace(" a i", " an i")
    sentence[0] = sentence[0].replace(" a o", " an o")
    sentence[0] = sentence[0].replace(" a u", " an u")

    # Fixing double space adjective issue
    sentence[0] = sentence[0].replace("  ", " ")
    sentence[1] = sentence[1].replace("  ", " ")

    # Capitalising
    sentence[0] = sentence[0].capitalize()
    sentence[1] = sentence[1].capitalize()

    # -----------------------------------------------------------------------------------------------------------------

    return sentence


def main():
    a, b = base_code()
    print(a)
    time.sleep(5)
    print(b)
    print("")
    time.sleep(2)


for i in range(5):
    main()
