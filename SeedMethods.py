from random import randint


def generateSeed():
    alpha = 'abcdefghijklmnpqrstuvwkyz'
    seed = alpha[randint(0, len(alpha) - 1)] + alpha[randint(0, len(alpha) - 1)] + \
        alpha[randint(0, len(alpha) - 1)] + alpha[randint(0, len(alpha) - 1)] + alpha[randint(0, len(alpha) - 1)]
    return seed


def intSeed(seed):
    Apos = {'a': [[571, 568], [197, 230], [485, 415], [91, 7]], 'c': [[112, 635], [630, 13], [56, 424], [569, 398]],
            'b': [[298, 562], [591, 306], [368, 574], [39, 559]], 'e': [[546, 124], [434, 565], [157, 510], [482, 295]],
            'd': [[6, 156], [426, 151], [342, 572], [401, 462]], 'g': [[497, 212], [568, 118], [285, 604], [573, 24]],
            'f': [[587, 348], [487, 297], [37, 439], [595, 409]], 'i': [[464, 216], [360, 369], [292, 70], [175, 141]],
            'h': [[494, 474], [388, 385], [482, 38], [88, 459]], 'k': [[80, 7], [505, 180], [344, 312], [157, 52]],
            'j': [[194, 87], [616, 130], [575, 46], [99, 53]], 'm': [[8, 587], [347, 351], [403, 581], [306, 340]],
            'l': [[288, 564], [330, 499], [465, 127], [420, 210]], 'o': [[191, 57], [175, 366], [516, 417], [74, 169]],
            'n': [[605, 616], [189, 401], [479, 36], [414, 561]], 'q': [[214, 625], [93, 370], [621, 350], [46, 401]],
            'p': [[0, 200], [132, 495], [118, 178], [617, 388]], 's': [[4, 590], [474, 445], [305, 19], [59, 517]],
            'r': [[415, 354], [560, 554], [365, 354], [536, 141]], 'u': [[231, 322], [567, 608], [635, 128], [5, 182]],
            't': [[386, 550], [234, 416], [622, 577], [134, 288]], 'w': [[231, 276], [593, 581], [356, 451], [488, 24]],
            'v': [[624, 168], [150, 70], [441, 217], [462, 430]], 'y': [[453, 118], [446, 116], [129, 51], [218, 359]],
            'x': [[175, 388], [58, 259], [22, 208], [24, 538]], 'z': [[352, 312], [418, 502], [113, 223], [473, 592]]}

    AA = {'a': [154, 165, 110, 268], 'c': [207, 69, 288, 54], 'b': [268, 346, 47, 30], 'e': [143, 299, 325, 173],
          'd': [89, 325, 358, 22], 'g': [79, 23, 287, 115], 'f': [263, 259, 146, 89], 'i': [68, 61, 265, 231],
          'h': [47, 2, 220, 142], 'k': [4, 146, 114, 80], 'j': [208, 334, 9, 136], 'm': [360, 28, 77, 293],
          'l': [52, 316, 346, 100], 'o': [328, 351, 128, 205], 'n': [342, 335, 254, 263], 'q': [161, 238, 258, 173],
          'p': [350, 211, 350, 135], 's': [73, 334, 290, 40], 'r': [29, 126, 6, 218], 'u': [288, 279, 45, 132],
          't': [202, 297, 318, 170], 'w': [206, 304, 117, 93], 'v': [231, 49, 298, 33], 'y': [0, 252, 92, 67],
          'x': [19, 283, 186, 62], 'z': [96, 218, 136, 291]}

    BI = {'a': [False, False, False, True, True, None, True, False, False, None, False],
          'c': [False, None, True, False, False, False, False, True, None, None, False],
          'b': [True, False, None, False, False, False, False, False, False, False, True],
          'e': [None, None, False, None, True, None, False, None, True, None, True],
          'd': [None, False, None, False, False, None, None, True, False, True, False],
          'g': [False, False, False, None, None, None, True, False, True, None, False],
          'f': [True, None, False, False, True, True, None, None, None, False, None],
          'i': [True, None, False, None, False, None, None, True, True, False, None],
          'h': [False, False, False, True, None, None, False, False, True, False, False],
          'k': [None, None, None, True, None, False, False, None, False, False, True],
          'j': [None, True, False, None, None, False, False, True, False, False, False],
          'm': [False, None, None, None, None, None, True, None, None, None, False],
          'l': [False, None, None, None, False, None, False, False, False, True, True],
          'o': [None, None, False, None, True, None, False, None, None, None, None],
          'n': [False, False, False, False, None, None, False, True, True, False, None],
          'q': [True, True, False, False, False, False, False, None, False, False, None],
          'p': [None, None, None, None, None, None, False, True, False, None, True],
          's': [False, True, False, True, False, None, False, False, True, False, True],
          'r': [None, True, False, True, False, False, False, False, None, False, None],
          'u': [True, False, False, None, False, False, False, True, None, None, False],
          't': [None, None, False, False, None, True, False, False, None, False, False],
          'w': [None, None, None, True, None, True, False, None, None, False, None],
          'v': [None, True, False, False, True, True, None, None, True, False, False],
          'y': [None, None, None, None, None, None, False, None, None, None, False],
          'x': [None, None, None, None, False, False, None, False, True, None, True],
          'z': [None, None, False, False, False, None, True, False, False, None, True]}

    BP = {
        'a': [[182, 544], [42, 321], [247, 506], [249, 194], [503, 636], [302, 490], [545, 269], [153, 569], [147, 594],
              [17, 292], [245, 402]],
        'c': [[271, 207], [626, 501], [349, 165], [451, 308], [459, 153], [299, 54], [67, 287], [278, 618], [615, 378],
              [479, 167], [124, 491]],
        'b': [[393, 591], [185, 132], [410, 32], [62, 243], [427, 72], [333, 602], [343, 503], [127, 471], [598, 169],
              [336, 265], [301, 330]],
        'e': [[261, 614], [173, 274], [61, 581], [300, 169], [84, 602], [192, 89], [6, 580], [489, 488], [393, 467],
              [112, 571], [57, 49]],
        'd': [[430, 606], [116, 473], [335, 630], [570, 617], [198, 617], [265, 530], [331, 58], [570, 457], [450, 127],
              [371, 365], [217, 17]],
        'g': [[185, 449], [502, 276], [37, 186], [489, 240], [578, 78], [14, 416], [332, 134], [610, 16], [280, 235],
              [14, 61], [560, 573]],
        'f': [[520, 72], [432, 455], [532, 15], [208, 97], [121, 614], [195, 436], [5, 379], [496, 406], [149, 126],
              [217, 144], [84, 84]],
        'i': [[47, 278], [209, 0], [441, 302], [564, 477], [597, 92], [21, 242], [588, 258], [182, 33], [193, 8],
              [597, 602], [539, 593]],
        'h': [[18, 512], [388, 462], [253, 141], [184, 131], [357, 242], [577, 321], [436, 121], [571, 435], [146, 443],
              [584, 572], [159, 530]],
        'k': [[163, 105], [596, 77], [498, 332], [638, 295], [263, 580], [516, 548], [208, 629], [262, 58], [568, 639],
              [379, 45], [536, 371]],
        'j': [[278, 200], [464, 278], [200, 264], [413, 53], [509, 247], [205, 61], [365, 399], [195, 580], [137, 634],
              [61, 456], [213, 168]],
        'm': [[488, 456], [316, 288], [556, 57], [486, 345], [624, 500], [434, 533], [40, 127], [589, 409], [239, 161],
              [76, 340], [514, 39]],
        'l': [[486, 167], [110, 599], [552, 77], [569, 97], [96, 105], [511, 188], [449, 195], [269, 467], [41, 622],
              [38, 196], [422, 557]],
        'o': [[314, 103], [116, 13], [189, 623], [407, 283], [247, 383], [234, 345], [121, 338], [608, 616], [41, 549],
              [452, 150], [632, 100]],
        'n': [[638, 210], [60, 108], [460, 456], [463, 242], [570, 605], [635, 96], [115, 254], [170, 329], [412, 61],
              [380, 272], [171, 149]],
        'q': [[610, 640], [371, 135], [38, 432], [469, 287], [100, 428], [164, 21], [623, 389], [241, 45], [229, 368],
              [349, 108], [369, 149]],
        'p': [[290, 30], [135, 474], [599, 21], [311, 630], [572, 534], [161, 525], [158, 120], [470, 604], [308, 432],
              [618, 397], [362, 363]],
        's': [[408, 156], [313, 392], [455, 465], [281, 127], [601, 319], [498, 246], [95, 218], [25, 568], [584, 608],
              [68, 476], [425, 154]],
        'r': [[118, 514], [465, 506], [183, 408], [52, 109], [188, 515], [96, 198], [89, 80], [128, 34], [321, 634],
              [542, 276], [206, 326]],
        'u': [[482, 325], [508, 326], [184, 418], [161, 372], [383, 522], [390, 153], [388, 528], [516, 355], [69, 337],
              [123, 393], [82, 496]],
        't': [[640, 146], [309, 496], [616, 207], [318, 408], [134, 0], [111, 525], [88, 577], [169, 482], [295, 197],
              [640, 572], [159, 172]],
        'w': [[507, 480], [181, 218], [287, 431], [374, 160], [467, 138], [351, 248], [83, 497], [109, 225], [440, 170],
              [523, 479], [483, 311]],
        'v': [[559, 520], [601, 170], [247, 84], [258, 46], [494, 223], [10, 389], [602, 157], [429, 323], [191, 468],
              [36, 276], [476, 155]],
        'y': [[259, 310], [592, 342], [313, 166], [490, 513], [355, 233], [425, 20], [342, 555], [486, 135], [250, 329],
              [235, 226], [425, 308]],
        'x': [[296, 566], [115, 557], [199, 198], [453, 341], [370, 73], [487, 377], [248, 120], [103, 381], [0, 82],
              [404, 20], [461, 529]],
        'z': [[366, 90], [489, 630], [101, 606], [78, 626], [522, 594], [150, 492], [274, 627], [425, 340], [334, 604],
              [154, 452], [118, 30]]}

    who = {'a': ['bad', 'aster', 'bad', 'bad', 'bad', 'bad', 'bad', 'none', 'none', 'bad', 'aster'],
           'c': ['none', 'bad', 'bad', 'bad', 'bad', 'none', 'aster', 'bad', 'none', 'aster', 'none'],
           'b': ['aster', 'bad', 'aster', 'aster', 'none', 'none', 'bad', 'aster', 'bad', 'bad', 'bad'],
           'e': ['bad', 'bad', 'aster', 'bad', 'bad', 'none', 'none', 'aster', 'bad', 'aster', 'bad'],
           'd': ['bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'aster', 'aster', 'none', 'bad', 'aster'],
           'g': ['bad', 'bad', 'bad', 'bad', 'none', 'bad', 'none', 'none', 'aster', 'bad', 'bad'],
           'f': ['none', 'bad', 'aster', 'none', 'aster', 'aster', 'bad', 'none', 'aster', 'bad', 'bad'],
           'i': ['none', 'aster', 'bad', 'bad', 'aster', 'bad', 'bad', 'bad', 'none', 'bad', 'bad'],
           'h': ['aster', 'bad', 'bad', 'aster', 'aster', 'none', 'none', 'bad', 'bad', 'bad', 'bad'],
           'k': ['bad', 'none', 'none', 'none', 'bad', 'bad', 'bad', 'aster', 'bad', 'bad', 'none'],
           'j': ['none', 'bad', 'aster', 'bad', 'none', 'bad', 'aster', 'aster', 'bad', 'bad', 'bad'],
           'm': ['bad', 'none', 'bad', 'bad', 'bad', 'none', 'aster', 'bad', 'none', 'bad', 'none'],
           'l': ['none', 'bad', 'aster', 'aster', 'bad', 'aster', 'none', 'none', 'bad', 'bad', 'bad'],
           'o': ['none', 'bad', 'bad', 'aster', 'bad', 'bad', 'bad', 'bad', 'bad', 'none', 'none'],
           'n': ['aster', 'aster', 'aster', 'bad', 'bad', 'aster', 'bad', 'bad', 'bad', 'bad', 'bad'],
           'q': ['none', 'bad', 'aster', 'aster', 'bad', 'bad', 'bad', 'bad', 'bad', 'none', 'bad'],
           'p': ['aster', 'none', 'aster', 'bad', 'bad', 'none', 'aster', 'aster', 'bad', 'bad', 'bad'],
           's': ['aster', 'aster', 'none', 'none', 'none', 'bad', 'aster', 'bad', 'bad', 'none', 'none'],
           'r': ['none', 'bad', 'bad', 'none', 'bad', 'none', 'aster', 'bad', 'none', 'none', 'bad'],
           'u': ['none', 'none', 'aster', 'none', 'aster', 'aster', 'bad', 'aster', 'bad', 'bad', 'bad'],
           't': ['bad', 'bad', 'bad', 'aster', 'bad', 'bad', 'aster', 'none', 'none', 'none', 'bad'],
           'w': ['bad', 'bad', 'bad', 'bad', 'none', 'bad', 'bad', 'none', 'bad', 'bad', 'bad'],
           'v': ['bad', 'none', 'none', 'aster', 'none', 'aster', 'none', 'bad', 'bad', 'aster', 'bad'],
           'y': ['none', 'bad', 'none', 'bad', 'bad', 'none', 'bad', 'bad', 'bad', 'bad', 'none'],
           'x': ['bad', 'aster', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'none'],
           'z': ['aster', 'bad', 'bad', 'none', 'bad', 'aster', 'bad', 'bad', 'bad', 'bad', 'none']}
    info = [Apos[seed[0:1]],AA[seed[1:2]],BI[seed[2:3]],BP[seed[3:4]]]
    index = seed[4:]
    index = who[str(index)]
    asteroids = []
    enemies = []
    pos = 0
    for potentialEnemy in index:
        if potentialEnemy == 'bad':
            enemies.append(pos)
        elif potentialEnemy != 'none':
            asteroids.append('a')
        pos += 1
    listOfEntitiesToCreate = []
    for enemy in enemies:
        newd = ['bad']
        newd.append(info[2][enemy])
        newd.append(info[3][enemy])
        listOfEntitiesToCreate.append(newd)
    position = 0
    for asteroid in asteroids:
        newd = ['asteroid']
        newd.append(info[1][position])
        newd.append(info[0][position])
        position += 1
        listOfEntitiesToCreate.append(newd)
    return listOfEntitiesToCreate  # final thing *whew*
