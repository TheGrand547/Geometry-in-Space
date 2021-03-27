import pygame
from pygame.locals import *
from sys import exit
from random import randint,  shuffle, choice
from math import sin, cos, radians,  sqrt, degrees, atan2, acos
from datetime import datetime

def ScreenUpdate(screen):
    global oldFrame, frameNumber,location
    if location == 4:
        screen = reformat(screen, oldFrame, frameNumber)
        if frameNumber == 1:
            frameNumber = 0
        else:
            frameNumber = 1
        oldFrame = screen.copy()
    pygame.display.flip()

def reformat(new, old, frame):
    reformed = pygame.PixelArray(new)
    r2 = pygame.PixelArray(old)
    reformed[:,::(frame+2)] = r2[:,::(frame+2)]
    return reformed.surface

def encript(to_encript):
    #this function has no purpose...
    atlas = "abcdefghijklmnopqrstuvwxyz"
    atlas += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #in_cripts = [25,14,18,8,1,12,5,6,19,24,23,9,11,3,2,16,14]
    #in_cripts = [16, 8, 19, 11, 14, 23, 24, 5, 12, 9, 13, 21, 20, 7, 15, 3, 1, 2, 0, 18, 4, 10, 17, 22, 6]
    in_cripts = [20, 22, 29, 30, 15, 26, 35, 16, 4, 12, 18, 28, 43, 38, 33, 44, 37, 9, 25, 31, 34, 42, 47,
                 23, 17, 11, 51, 10, 46, 39, 24, 19, 50, 41, 27, 3, 40, 21, 32, 8, 13, 1, 7, 2, 14, 0, 45,
                 6, 49, 5, 48, 36]
    encoded = ""
    place = 0
    to_encript.lower()
    not_allowed = '1234567890-=`~!@#$%^&*()_+[]{}\|;:"/?.>, <' + "'"
    for letter in to_encript:
        #if not letter == " ":
        if letter not in not_allowed:
           lets = atlas.find(letter)
           if place >= len(in_cripts):
               place = 0
           new_pos = in_cripts[place] - lets
           #print new_pos
           if new_pos >= 26:
               new_pos -= 26
           elif new_pos < 0 :
                new_pos += 26
           new_letter = atlas[new_pos]
           place += 1
           encoded += new_letter
           if place > len(in_cripts) -1:
               place = 0
        else:
            #encoded += " "
            encoded += letter
            place += 1
    return encoded


def range2(start,stop=None,step=1.0):
    if stop is None:
        stop = start
        start = 0
    x = []
    while start <= stop:
        x.append(start)
        start += step
    return x


def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return sqrt(dotproduct(v, v))

def angle(v1, v2):
  return acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def intSeed(stage,info,seed):
    # Apos = {'a':[[10,10],[25,25]],'b':[]} #asteroids pos's
    # AA = {'a':[29,53,174,342]} #asteroid angles
    dashP = []
    crs = 0
    while True: #finds all the dashes
        k = seed.find('-',crs+1)
        if k != -1:
            dashP.append(k)
            crs = int(k)
        else:
            break
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
            'x': [[175, 388], [58, 259], [22, 208], [24, 538]], 'z':[[352,312],[418,502],[113,223],[473,592]]}
    
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

    BP = {'a': [[182, 544], [42, 321], [247, 506], [249, 194], [503, 636], [302, 490], [545, 269], [153, 569], [147, 594], [17, 292], [245, 402]],
          'c': [[271, 207], [626, 501], [349, 165], [451, 308], [459, 153], [299, 54], [67, 287], [278, 618], [615, 378], [479, 167], [124, 491]],
          'b': [[393, 591], [185, 132], [410, 32], [62, 243], [427, 72], [333, 602], [343, 503], [127, 471], [598, 169], [336, 265], [301, 330]],
          'e': [[261, 614], [173, 274], [61, 581], [300, 169], [84, 602], [192, 89], [6, 580], [489, 488], [393, 467], [112, 571], [57, 49]],
          'd': [[430, 606], [116, 473], [335, 630], [570, 617], [198, 617], [265, 530], [331, 58], [570, 457], [450, 127], [371, 365], [217, 17]],
          'g': [[185, 449], [502, 276], [37, 186], [489, 240], [578, 78], [14, 416], [332, 134], [610, 16], [280, 235], [14, 61], [560, 573]],
          'f': [[520, 72], [432, 455], [532, 15], [208, 97], [121, 614], [195, 436], [5, 379], [496, 406], [149, 126], [217, 144], [84, 84]],
          'i': [[47, 278], [209, 0], [441, 302], [564, 477], [597, 92], [21, 242], [588, 258], [182, 33], [193, 8], [597, 602], [539, 593]],
          'h': [[18, 512], [388, 462], [253, 141], [184, 131], [357, 242], [577, 321], [436, 121], [571, 435], [146, 443], [584, 572], [159, 530]],
          'k': [[163, 105], [596, 77], [498, 332], [638, 295], [263, 580], [516, 548], [208, 629], [262, 58], [568, 639], [379, 45], [536, 371]],
          'j': [[278, 200], [464, 278], [200, 264], [413, 53], [509, 247], [205, 61], [365, 399], [195, 580], [137, 634], [61, 456], [213, 168]],
          'm': [[488, 456], [316, 288], [556, 57], [486, 345], [624, 500], [434, 533], [40, 127], [589, 409], [239, 161], [76, 340], [514, 39]],
          'l': [[486, 167], [110, 599], [552, 77], [569, 97], [96, 105], [511, 188], [449, 195], [269, 467], [41, 622], [38, 196], [422, 557]],
          'o': [[314, 103], [116, 13], [189, 623], [407, 283], [247, 383], [234, 345], [121, 338], [608, 616], [41, 549], [452, 150], [632, 100]],
          'n': [[638, 210], [60, 108], [460, 456], [463, 242], [570, 605], [635, 96], [115, 254], [170, 329], [412, 61], [380, 272], [171, 149]],
          'q': [[610, 640], [371, 135], [38, 432], [469, 287], [100, 428], [164, 21], [623, 389], [241, 45], [229, 368], [349, 108], [369, 149]],
          'p': [[290, 30], [135, 474], [599, 21], [311, 630], [572, 534], [161, 525], [158, 120], [470, 604], [308, 432], [618, 397], [362, 363]],
          's': [[408, 156], [313, 392], [455, 465], [281, 127], [601, 319], [498, 246], [95, 218], [25, 568], [584, 608], [68, 476], [425, 154]],
          'r': [[118, 514], [465, 506], [183, 408], [52, 109], [188, 515], [96, 198], [89, 80], [128, 34], [321, 634], [542, 276], [206, 326]],
          'u': [[482, 325], [508, 326], [184, 418], [161, 372], [383, 522], [390, 153], [388, 528], [516, 355], [69, 337], [123, 393], [82, 496]],
          't': [[640, 146], [309, 496], [616, 207], [318, 408], [134, 0], [111, 525], [88, 577], [169, 482], [295, 197], [640, 572], [159, 172]],
          'w': [[507, 480], [181, 218], [287, 431], [374, 160], [467, 138], [351, 248], [83, 497], [109, 225], [440, 170], [523, 479], [483, 311]],
          'v': [[559, 520], [601, 170], [247, 84], [258, 46], [494, 223], [10, 389], [602, 157], [429, 323], [191, 468], [36, 276], [476, 155]],
          'y': [[259, 310], [592, 342], [313, 166], [490, 513], [355, 233], [425, 20], [342, 555], [486, 135], [250, 329], [235, 226], [425, 308]],
          'x': [[296, 566], [115, 557], [199, 198], [453, 341], [370, 73], [487, 377], [248, 120], [103, 381], [0, 82], [404, 20], [461, 529]],
          'z': [[366, 90], [489, 630], [101, 606], [78, 626], [522, 594], [150, 492], [274, 627], [425, 340], [334, 604], [154, 452], [118, 30]]}

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
    """
    if stage == 0:
        us = seed[:dashP[0]]
        info.append(Apos[str(us[1:2])])
    elif stage == 1:
        us = seed[dashP[0]+1:dashP[1]]
        info.append(AA[str(us[1:2])])
    elif stage == 2:
        us = seed[dashP[1]+1:dashP[2]]
        info.append(BI[str(us[1:2])])
    elif stage == 3:
        us = seed[dashP[2]+1:dashP[3]]
        info.append(BP[str(us[1:2])])
    elif stage == 4:
        us = seed[dashP[3]+2:]
        #info.append(who[str(us[1:2])])
        us = who[str(us)]
        blue = list(info)
        asts = []
        bads = []
        pos = 0
        for i in us:
            if i == 'bad':
                bads.append(pos)
            elif i != 'none':
                asts.append('a')
            pos += 1
        toot = []
        for bat in bads:
            newd = ['bad']
            newd.append(info[2][bat])
            newd.append(info[3][bat])
            toot.append(newd)
        nuts = 0
        for nBat in asts:
            newd = ['aster']
            newd.append(info[0][nuts])
            newd.append(info[1][nuts])
            nuts += 1
            toot.append(newd)
        return toot #final thing *whew*
    return info
    """
    #simpler
    if stage == 0:
        us = seed[0:1]
        info.append(Apos[str(us)])
    elif stage == 1:
        us = seed[1:2]
        info.append(AA[str(us)])
    elif stage == 2:
        us = seed[2:3]
        info.append(BI[str(us)])
    elif stage == 3:
        us = seed[3:4]
        info.append(BP[str(us)])
    else:
        us = seed[4:]
        us = who[str(us)]
        blue = list(info)
        asts = []
        bads = []
        pos = 0
        for i in us:
            if i == 'bad':
                bads.append(pos)
            elif i != 'none':
                asts.append('a')
            pos += 1
        toot = []
        #print bads, '/', info[2]
        for bat in bads:
            newd = ['bad']
            newd.append(info[2][bat])
            newd.append(info[3][bat])
            toot.append(newd)
        nuts = 0
        for nBat in asts:
            newd = ['aster']
            newd.append(info[1][nuts])
            newd.append(info[0][nuts])
            nuts += 1
            toot.append(newd)
        return toot #final thing *whew*
    return info
        
        

        
def makeSeed():
    #creates a random seed for the map to be made of
    #3 components
    #number of bads
    #angles of everything and poses
    #example
    #the positions, angles and types are stored in preset arrrays
    #the arrays are actually dictionaries with lists as the definitions
    #example seed
    #Ac-Ad-Bg-Be-Si
    #first part (Ac5) means: Asteroid, 'c'th index 
    #second same, but with angles
    #third is bad guys index then subindex for types
    #fourth is their positions, but this time the 4th(Starting) index of the 2,3,34 and 87 numbers are thier positions
    #the starting index is where it starts, and it increases by 1 every time
    #5th tells how many of each type(bads and asteroids) there are
    alpha = 'abcdefghijklmnpqrstuvwkyz'
    """nums = '1230'
    Apos = {'a':[[10,10],[25,25]],} #asteroids pos's
    AA = {'a':[29,53,174,342]} #asteroid angles
    #asteroids number and pos
    seed = 'A' + alpha[randint(0,len(alpha)-1)]
    #asteroids angles
    seed += '-A' + alpha[randint(0,4)]
    #bads num and types
    seed += '-B' + alpha[randint(0,len(alpha)-1)]
    #bads positions
    seed += '-B' + alpha[randint(0,len(alpha)-1)]#step and start
    
    #nitty gritty actually stuff
    for i in [0,1,2,3]:
        seed += nums[randint(0,len(nums)-1)] + '|'
    """
    #seed += '-S' + alpha[randint(0,len(alpha)-1)]
    #new simplier version
    seed = alpha[randint(0,len(alpha)-1)] + alpha[randint(0,len(alpha)-1)] + \
           alpha[randint(0,len(alpha)-1)] + alpha[randint(0,len(alpha)-1)] + alpha[randint(0,len(alpha)-1)]
    return seed


def moves(t0,t1,psx,psy,speed,bot=False):


    speed = speed
    distance = [t0 - psx, t1 - psy]
    norm = sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / norm, distance[1] / norm]

    bullet_vector = [direction[0] * speed, direction[1] * speed]
    if bot:
        pass
        #bullet_vector[0] += randint(-1,1)*1.1742*random()
        #bullet_vector[1] += randint(-1,1)*1.1742*random()
    elif bot is None:
        ofs = range(-5,5,.25)
        bullet_vector[0] += choice(ofs)*2.34
        bullet_vector[1] += choice(ofs)*2.23
        #bullet_vector[0] += randint(-5,5)*4.5742*random()
        #bullet_vector[1] += randint(-5,5)*4.5742*random()
    #print uniform(-1,1)
    return bullet_vector

class Bullet2():
    def __init__(self,angle,pos,t,x=False,image=None):
        if image is None:
            self.i = pygame.image.load("bullet.png").convert()
            self.et = pygame.image.load("bullet.png").convert()
        else:
            self.i = image
            self.et = image
        self.et.set_colorkey((255,255,255))
        self.i.set_colorkey((255,255,255))
        self.a = angle
        self.r = self.i.get_rect(center=pos)
        self.hb = pygame.mask.from_surface(self.i)
        self.ig = False
        self.t = t
        self.g = 0
        self.jjj = True
        self.s = 12
        #self.ch = [self.s * ((cos(radians(int(self.a))))),self.s * ((sin(radians(int(self.a)))))]
        if not t:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],8,True)
        elif x:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],9,None)
        else:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],8,False)
        self.bt = 0
        self.btm = 90
        #self.s = 6

    def update(self):
        #damage = 5
        global htbl,player,fnum
        #'''
        #'''
        '''
        if not self.ig:
            if self.t and not self.t is None:
                #player bullet
                k = [self.r.topleft[0], self.r.topleft[1]]
                for i in range(0,8):
                    k[0] += float(self.ch[0]/8)
                    k[1] += float(self.ch[1]/8)
                    for th in htbl:
                        ccc = [th.r.topleft[0],th.r.topleft[1]]
                        dx = int(ccc[0]-k[0])
                        dy = int(ccc[1]-k[1])
                        if th.hb.overlap(self.hb,[dx,dy]) != None:
                            self.ig = True
                            break
            else:
                #not
                k = [self.r.topleft[0], self.r.topleft[1]]
                for i in range(0,8):
                    k[0] += float(self.ch[0]/8)
                    k[1] += float(self.ch[1]/8)
                    ccc = [player.r.topleft[0],player.r.topleft[1]]
                    dx = int(ccc[0]-k[0])
                    dy = int(ccc[1]-k[1])
                    if player.hb.overlap(self.hb,[dx,dy]) != None:
                        self.ig = True
       
        #self.c = [self.r.center[0],self.r.center[1]]
        #self.c[0] += float(self.ch[0])
        #self.c[1] += float(self.ch[1])
            self.c = k
            if self.c[0] > 640:
                self.c[0] -= 640
            if self.c[0] < 0:
                self.c[0] += 640
            if self.c[1] < 0:
                self.c[1] += 640
            if self.c[1] > 640:
                self.c[1] -= 640
           
            self.r = self.i.get_rect(topleft=self.c)
            screen.blit(self.i,self.r)
            self.bt += 1
            if self.bt >= self.btm:
                self.ig = True
        '''
        '''
        if True:
            #k = [self.r.center[0], self.r.center[1]]
            k = [self.r.topleft[0], self.r.topleft[1]]
            k[0] += float(self.ch[0])
            k[1] += float(self.ch[1])
            self.r = self.i.get_rect(center=k)
            #if self.t:
            if True:
                for th in htbl:
                    k = [self.r.center[0], self.r.center[1]]
                    k[0] -= float(self.ch[0])
                    k[1] -= float(self.ch[1])
                    for i in range(0,8):
                        k[0] += float(float(self.ch[0])/8)
                        k[1] += float(float(self.ch[1])/8)
                        ccc = [th.r.topleft[0],th.r.topleft[1]]
                        #dx = int(th.c[0]-k[0])
                        #dy = int(th.c[1]-k[1])
                        dx = int(ccc[0]-k[0])
                        dy = int(ccc[1]-k[1])
                        #print dx, "/", dy
                        #print self.hb.overlap(th.hb,[dx,dy])
                        if self.hb.overlap(th.hb,[dx,dy]) != None and self.t:
                            th.h -= 12
                            #print 'duh'
                            self.r = self.i.get_rect(center=k)
                            self.ig = True
                            break
                        if self.t:
                            for i in astrds:
                                ccc = [th.r.topleft[0],th.r.topleft[1]]
                                dx = int(ccc[0]-k[0])
                                dy = int(ccc[1]-k[1])
                                if self.hb.overlap(th.hb,[dx,dy]) != None:
                                    i.a += 15
                                    self.ig = True
                                    self.r = self.i.get_rect(center=k)
                                    break
                        if not self.t:
                            ccc = [th.r.topleft[0],th.r.topleft[1]]
                            dx = int(ccc[0]-k[0])
                            dy = int(ccc[1]-k[1])
                            if self.hb.overlap(player.hb,[dx,dy]) != None:
                                player.h -= 4
                                self.ig = True
                                self.r = self.i.get_rect(center=k)
                                break
                        #if self.ig:
                            #break
                    #if self.ig:
                        #break
                
        '''
        if True:
            if self.t:
                for th in htbl:
                    k = [self.r.center[0], self.r.center[1]]
                    #k[0] -= float(self.ch[0])
                    #k[1] -= float(self.ch[1])
                    #print "dorty"
                    if th.h <= 0:
                        htbl.remove(th)
                        global exps
                        exps.play(exps2)
                        continue
                    for i in range(0,8):
                        k[0] += float(float(self.ch[0])/8)
                        k[1] += float(float(self.ch[1])/8)
                        ccc = [th.r.topleft[0],th.r.topleft[1]]
                        #dx = int(th.c[0]-k[0])
                        #dy = int(th.c[1]-k[1])
                        dx = int(ccc[0]-k[0])
                        dy = int(ccc[1]-k[1])
                        #print dx, "/", dy
                        #print self.hb.overlap(th.hb,[dx,dy])
                        if self.hb.overlap(th.hb,[dx,dy]) != None:
                            th.h -= 12
                            #print 'duh'
                            self.r = self.i.get_rect(center=k)
                            self.ig = True
                            break
                        dx = int(ccc[0]-k[0])
                        dy = int(ccc[1]-k[1])
                        #print dx, "/", dy
                        #print self.hb.overlap(th.hb,[dx,dy])
                        '''
                        if self.hb.overlap(irk.hb,[dx,dy]) != None:
                            #print 'duh'
                            irk.a += choice(range(-180,180,20))
                            self.r = self.i.get_rect(center=k)
                            self.ig = True
                            break
                        '''
        
        
                #if True:
                '''
                for irk in astrds:
                     k = [self.r.center[0], self.r.center[1]]
                     k[0] -= float(self.ch[0])
                     k[1] -= float(self.ch[1])
                     for i in range(0,8):
                        k[0] += float(float(self.ch[0])/8)
                        k[1] += float(float(self.ch[1])/8)
                        ccc = [irk.r.topleft[0],irk.r.topleft[1]]
                        #dx = int(th.c[0]-k[0])
                        #dy = int(th.c[1]-k[1])
                        dx = int(ccc[0]-k[0])
                        dy = int(ccc[1]-k[1])
                        #print dx, "/", dy
                        #print self.hb.overlap(th.hb,[dx,dy])
                        if self.hb.overlap(irk.hb,[dx,dy]) != None:
                            #print 'duh'
                            irk.a += choice(range(-180,180,20))
                            self.r = self.i.get_rect(center=k)
                            self.ig = True
                            break
                '''
        
            else:
                if self.jjj:
                    k = [self.r.center[0], self.r.center[1]]
                    k[0] -= float(self.ch[0])
                    k[1] -= float(self.ch[1])
                    for i in range(0,10):
                        k[0] += float(float(self.ch[0])/10)
                        k[1] += float(float(self.ch[1])/10)
                        #g = [self.r.topleft[0],self.r.topleft[1]]
                        dx = int(player.c[0]-k[0])
                        dy = int(player.c[1]-k[1])
                        if self.hb.overlap(player.hb,[dx,dy]):
                                player.health -= 3
                                self.ig = True
                                self.jjj = False
                                self.r = self.i.get_rect(center=k)
                                
        #'''
        #'''
            
            self.c = [self.r.center[0],self.r.center[1]]
            #"""
            self.c = k
            if self.c[0] > 640:
                self.c[0] -= 640
            if self.c[0] < 0:
                self.c[0] += 640
            if self.c[1] < 0:
                self.c[1] += 640
            if self.c[1] > 640:
                self.c[1] -= 640
           
            self.r = self.i.get_rect(center=self.c)
            screen.blit(self.i,self.r)
            self.bt += 1
            if self.bt >= self.btm:
                self.ig = True
            #'''

    def update2(self):
        #new draw function because the other was too cluttered
        #hit detection
        global demo
        if not self.ig:
            k = [self.r.topleft[0],self.r.topleft[1]]
            if self.t is None or not self.t:
                #non-player
                for i in range(0,5):
                    k[0] += float(self.ch[0]/5.0)
                    k[1] += float(self.ch[1]/5.0)
                    if True:
                        dx = int(demo.r.topleft[0]-k[0])
                        dy = int(demo.r.topleft[1]-k[1])
                        if self.hb.overlap(demo.hb,[dx,dy]):
                            self.ig = True
                            demo.health -= 2
                            break
                    if self.ig:
                        break
            else:
                k = [self.r.topleft[0],self.r.topleft[1]]
                #player
                #print "i'm a player"
                for i in range(0,5):
                    k[0] += float(self.ch[0]/5.0)
                    k[1] += float(self.ch[1]/5.0)
                    for th in htbl: 
                        dx = int(th.r.topleft[0]-k[0])
                        dy = int(th.r.topleft[1]-k[1])
                        if self.hb.overlap(th.hb,[dx,dy]):
                            th.h -= 12
                            self.ig = True
                            break
                        
                    for th in astrds:
                        dx = int(th.r.topleft[0]-k[0])
                        dy = int(th.r.topleft[1]-k[1])
                        if self.hb.overlap(th.hb,[dx,dy]):
                            self.ig = True
                            #th.a += 45
                            sfe = atan2(self.ch[1],self.ch[0])
                            th.a = angle([th.a,-th.s],[sfe,8.5])
                            break
                    if self.ig:
                        break
                    #if self.ig:
                        #break
                        #'''
                
        #drawing and stuff
        try:
            self.c = k
        except:
            self.c = [self.r.topleft[0],self.r.topleft[1]]
        if self.c[0] > 640:
            self.c[0] -= 640
        if self.c[0] < 0:
            self.c[0] += 640
        if self.c[1] < 0:
            self.c[1] += 640
        if self.c[1] > 640:
            self.c[1] -= 640
       
        self.r = self.i.get_rect(topleft=self.c)
        screen.blit(self.i,self.r)
        self.bt += 1
        if self.bt >= self.btm:
            self.ig = True


class Bullet():
    def __init__(self,angle,pos,t,x=False,image=None):
        if image is None:
            self.i = pygame.image.load("bullet.png").convert()
            self.et = pygame.image.load("bullet.png").convert()
        else:
            self.i = image
            self.et = image
        self.et.set_colorkey((255,255,255))
        self.i.set_colorkey((255,255,255))
        self.a = angle
        self.r = self.i.get_rect(center=pos)
        self.hb = pygame.mask.from_surface(self.i)
        self.ig = False
        self.t = t
        self.g = 0
        self.jjj = True
        self.s = 12
        #self.ch = [self.s * ((cos(radians(int(self.a))))),self.s * ((sin(radians(int(self.a)))))]
        if not t:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],8.5,True)
        elif x:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],9,None)
        else:
            self.ch = moves(self.a[0],self.a[1],self.a[2],self.a[3],8.5,False)
        self.bt = 0
        self.btm = 90
        #self.s = 6
        
    def update2(self):
        #new draw function because the other was too cluttered
        #hit detection
        global stats, bH2, bHt
        if not self.ig:
            k = [self.r.topleft[0],self.r.topleft[1]]
            if self.t is None or not self.t:
                #non-player
                for i in range(0,5):
                    k[0] += float(self.ch[0]/5.0)
                    k[1] += float(self.ch[1]/5.0)
                    if True:
                        dx = int(player.r.topleft[0]-k[0])
                        dy = int(player.r.topleft[1]-k[1])
                        if self.hb.overlap(player.hb,[dx,dy]):
                            self.ig = True
                            bH2.play(bHt)
                            player.health -= 2
                            break
                    if self.ig:
                        break
            else:
                k = [self.r.topleft[0],self.r.topleft[1]]
                #player
                #print "i'm a player"
                #shots fired, baddies hit, asteroids hit, baddies killed, deaths
                #wins, time spent playing (in levels)
                for i in range(0,5):
                    k[0] += float(self.ch[0]/5.0)
                    k[1] += float(self.ch[1]/5.0)
                    for th in htbl:
                        if not th.dead:
                            dx = int(th.r.topleft[0]-k[0])
                            dy = int(th.r.topleft[1]-k[1])
                            if self.hb.overlap(th.hb,[dx,dy]):
                                th.h -= 12
                                bH2.play(bHt)
                                stats[1] += 1
                                self.ig = True
                                break
                    for th in astrds:
                        dx = int(th.r.topleft[0]-k[0])
                        dy = int(th.r.topleft[1]-k[1])
                        if self.hb.overlap(th.hb,[dx,dy]):
                            self.ig = True
                            stats[2] += 1
                            sfe = atan2(self.ch[1],self.ch[0])
                            #th.a = angle([th.a,-th.s],[sfe,8.5])
                            k = [th.s*cos(radians(th.a)),th.s*sin(radians(th.a))]
                            th.a = angle(k,[self.ch[0],self.ch[1]])+90
                            break
                    if self.ig:
                        break
                    #if self.ig:
                        #break
                
        #drawing and stuff
        try:
            self.c = k
        except:
            self.c = [self.r.topleft[0],self.r.topleft[1]]
        if self.c[0] > 640:
            self.c[0] -= 640
        if self.c[0] < 0:
            self.c[0] += 640
        if self.c[1] < 0:
            self.c[1] += 640
        if self.c[1] > 640:
            self.c[1] -= 640
       
        self.r = self.i.get_rect(topleft=self.c)
        screen.blit(self.i,self.r)
        self.bt += 1
        if self.bt >= self.btm:
            self.ig = True

class HpBar():
    def __init__(self, number):
        self.number = number
        self.oldpercent = 0

    def paint(self):
        global player
        self.width = player.r.width
        a = (self.width,3)
        self.image = pygame.Surface(a)
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, (0,255,0), (0,0,a[0], a[1]),1)
        self.rect = self.image.get_rect()
        
    def update(self):
        a = [10,10]
        global player
        a = [player.health, player.max]
        b = [player.r.topleft[0], player.r.topleft[1]]
        c = player.r.height
        self.percent = float(a[0] / (a[1]*1.0))
    
        if self.percent != self.oldpercent:
            self.paint() # important ! boss.rect.width may have changed (because rotating)
            pygame.draw.rect(self.image, (0,0,0), (0,0,self.width,3)) # fill black
            pygame.draw.rect(self.image, (0,255,0), (0,0,self.width,3),1)
            pygame.draw.rect(self.image, (0,255,0), (0,0,
                             int(self.width * self.percent),3),0) # fill green
            
        self.oldpercent = self.percent
        self.rect[0] = b[0]
        self.rect[1] = b[1] - c /2 + 7
        screen.blit(self.image, self.rect)
        if not a[0] < 1:   #check if boss is still alive
            screen.blit(self.image, self.rect)

class Player():
    def __init__(self,image=None):
        if image is None:
            self.i = pygame.image.load("hero.png").convert()
            self.p = pygame.image.load('hero.png').convert()
        else:
            self.i = image
            self.p = image
        self.mFsO = [pygame.image.load('heroF1.png').convert(),
                     pygame.image.load('heroF2.png').convert(),
                     pygame.image.load('heroF3.png').convert(),
                     pygame.image.load('heroF4.png').convert(),
                    pygame.image.load('heroF5.png').convert()]
        self.mFs = [pygame.image.load('heroF1.png').convert(),
                     pygame.image.load('heroF2.png').convert(),
                     pygame.image.load('heroF3.png').convert(),
                    pygame.image.load('heroF4.png').convert(),
                    pygame.image.load('heroF5.png').convert()]
        for i in self.mFsO:
            i.set_colorkey((255,255,255))
        for i in self.mFs:
            i.set_colorkey((255,255,255))
        self.i.set_colorkey((255,255,255))
        self.p.set_colorkey((255,255,255))
        self.hb = pygame.mask.from_surface(self.i)
        #self.r = self.i.get_rect(center=(274,311))
        self.r = self.i.get_rect(center=[320,320])
        angls = 320
        self.s = 0
        self.h = 20
        #self.a = 90
        self.a = 0
        self.ad = 90
        #self.c = [300,620]
        #self.c = [213,298]
        self.c = self.r.center
        self.k = [5,25]
        #health
        self.health = 150
        self.max = 150
        self.hpBar = HpBar(-1)
        #firing control
        self.pl = False
        self.frm = 0
        self.total = [self.s * float((cos(radians(self.ad)))),self.s * float((sin(radians(self.ad))))]
        

    def draw(self):
        global screen
        if self.s >= 25:
            self.s = 25
        self.move()
        if self.c[0] > 640:
            self.c[0] -= 640
        if self.c[0] < 0:
            self.c[0] += 640
        if self.c[1] < 0:
            self.c[1] += 640
        if self.c[1] > 640:
            self.c[1] -= 640
        self.r = self.i.get_rect()
        self.r.center = self.c
        self.c = self.r.center
        if self.s <= 0:
            screen.blit(self.i, self.r)
        else:
            a = int(round(self.frm))
            screen.blit(self.mFs[a],self.r)
            if self.frm >= 4:
                self.frm = 0
            self.frm += .2
        self.hpBar.update()
        if self.health < 10:
            pass
            #print self.health
       #if self.health > self.max:
            #self.health = int(self.max)

    def move(self):
        if self.a >= 360:
            self.a -= 360
        #x = [(self.r.center[0]+self.s * float((cos(radians(self.ad))))),(self.r.center[1]-self.s * float((sin(radians(self.ad)))))]
        #self.total = [self.s * float((cos(radians(self.ad)))),self.s * float((sin(radians(self.ad))))]
        x = [self.r.center[0]+self.total[0],self.r.center[1]-self.total[1]]
        #div = 9.0
        #global astrds
        #xs = float((cos(radians((self.ad)))))
       # ys = float((sin(radians((self.ad)))))
        '''
        for i in range(0,int(div)):
            #asteroid hit detection
            self.r[0] += (self.s/div) * xs#float((cos(radians((self.ad)))))
            self.r[1] -= (self.s/div) * ys#float((sin(radians((self.ad)))))
            """
            for i in astrds:
                self.r[0] += (self.s/div) * xs#float((cos(radians((self.ad)))))
                self.r[1] -= (self.s/div) * ys#float((sin(radians((self.ad)))))
                dx = int(self.r[0]-i.r[0])
                dy = int(self.r[1]-i.r[1])
                if self.hb.overlap(i.hb, (dx,dy)):
                    #i.s *= -1
                    #i.a += randint(-5,5)
                    i.a *= -1
                    self.health -= 3
                    self.r[0] -= 8 * (self.s/div) * xs
                    self.r[1] += 8 * (self.s/div) * ys
                    i.r[0] += 3 * (i.s/-2.0) * cos(radians(i.a))
                    i.r[1] -= 3 * (i.s/-2.0) * sin(radians(i.a))
                    self.s /= 2
                    i.cnm = True
                    break
            #"""
        '''
        self.c = x
        self.s -= .0025
        if self.s < 0:
            self.s = 0


    def rotate(self,deg):
        global roundEnd
        if not roundEnd:
            if self.a <= 0:
                self.a = 360
            self.a += deg
            self.ad += deg
            self.i = pygame.transform.rotate(self.p, self.a)
            r = self.r
            #self.r = self.i.get_rect()
            self.r = self.i.get_rect(topleft=[r[0],r[1]])
            sdf = []
            for i in self.mFsO:
                newt = pygame.transform.rotate(i, self.a)
                sdf.append(newt)
            self.mFs = sdf
            self.total = [self.s * float((cos(radians(self.ad)))),self.s * float((sin(radians(self.ad))))]
                

    def fire(self):
        #shots fired, baddies hit, asteroids hit, baddies killed, deaths
        #wins, time spent playing (in levels)
        global st,lazer, cfr,stats
        self.pl = True
        if cfr:
            stats[0] += 1
            cfr = False
            ad = float(self.ad)
            unp[0] = True
            #k = randint(-4,4)
            #print ad
            #ad += kd
            #print adf
            #print randint(-2,2)
            #sas = [randint(-10,10), randint(-10,10)]
            sas = [0,0]
            #print sas
            k = [self.r.center[0],self.r.center[1]]
           # for i in range(0,):
            k[0] += 40 * float(cos(radians(self.ad)))
            k[1] -= 40 * float(sin(radians(self.ad)))
            g = [k[0]+sas[0],k[1]+sas[1],self.r.center[0],self.r.center[1]]
            st.append(Bullet(g, self.r.center,True))
            lazer.play(lazer1)

class HpBar2():
    def __init__(self, number):
        self.number = number
        self.oldpercent = 0

    def paint(self):
        global player
        self.width = demo.r.width
        a = (self.width,2)
        self.image = pygame.Surface(a)
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, (0,255,0), (0,0,a[0], a[1]),1)
        self.rect = self.image.get_rect()
        
    def update(self):
        a = [10,10]
        global player
        a = [demo.health, demo.max]
        b = [demo.r.topleft[0], demo.r.topleft[1]]
        c = demo.r.height
        self.percent = float(a[0] / (a[1]*1.0))
    
        if self.percent != self.oldpercent:
            self.paint() # important ! boss.rect.width may have changed (because rotating)
            pygame.draw.rect(self.image, (0,0,0), (0,0,self.width,5)) # fill black
            pygame.draw.rect(self.image, (0,255,0), (0,0,
                             int(self.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect[0] = b[0]
        self.rect[1] = b[1] - c /2 + 7
        screen.blit(self.image, self.rect)
        if not a[0] < 1:   #check if boss is still alive
            screen.blit(self.image, self.rect)

class Player2():
    def __init__(self,image=None):
        if image is None:
            self.i = pygame.image.load("hero.png").convert()
            self.p = pygame.image.load('hero.png').convert()
        else:
            self.i = image
            self.p = image
        self.i.set_colorkey((255,255,255))
        self.p.set_colorkey((255,255,255))
        self.hb = pygame.mask.from_surface(self.i)
        #self.r = self.i.get_rect(center=(274,311))
        self.r = self.i.get_rect(center=[320,320])
        angls = 320
        self.s = 0
        self.h = 20
        #self.a = 90
        self.a = 0
        self.ad = 90
        #self.c = [300,620]
        #self.c = [213,298]
        self.c = self.r.center
        self.k = [5,25]
        #health
        self.health = 150
        self.max = 150
        self.hpBar = HpBar2(-1)
        #firing control
        self.pl = False
        

    def draw(self):
        global screen
        if self.s >= 25:
            self.s = 25
        self.move()
        '''
        mps = pygame.mouse.get_pos()
        dux = mps[0]-self.r.topleft[0]#-mps[0]
        duy = mps[1]-self.r.topleft[1]#-mps[1]
        angs = degrees(atan2(duy,dux))
        self.rotate(angs)
        self.a = angs
        self.ad = angs
        self.move()
        '''
        if self.c[0] > 640:
            self.c[0] -= 640
        if self.c[0] < 0:
            self.c[0] += 640
        if self.c[1] < 0:
            self.c[1] += 640
        if self.c[1] > 640:
            self.c[1] -= 640
        self.r = self.i.get_rect()
        self.r.center = self.c
        self.c = self.r.center
        screen.blit(self.i, self.r)
        self.hpBar.update()
        if self.health < 10:
            pass
            #print self.health
       #if self.health > self.max:
            #self.health = int(self.max)

    def move(self):
        if self.a >= 360:
            self.a -= 360
        x = [(self.r.center[0]+self.s * float((cos(radians(self.ad))))),(self.r.center[1]-self.s * float((sin(radians(self.ad)))))]
        div = 9.0
        global astrds
        xs = float((cos(radians(self.ad))))
        ys = float((sin(radians(self.ad))))
        self.r[0] += self.s*xs
        self.r[1] -= self.s*ys
        #'''
        hitLs = False
        for i in range(0,int(div)):
            #pass
            #asteroid hit detection
            self.r[0] += (self.s/div) * xs#float((cos(radians((self.ad)))))
            self.r[1] -= (self.s/div) * ys#float((sin(radians((self.ad)))))
            if not hitLs:
                for i in astrds:
                    dx = int(self.r[0]-i.r[0])
                    dy = int(self.r[1]-i.r[1])
                    if self.hb.overlap(i.hb, (dx,dy)):
                        #i.s *= -1
                        #i.a += randint(-5,5)
                        i.s *= -1
                        self.health -= .5
                        self.r[0] -= 8 * (self.s/div) * xs
                        self.r[1] += 8 * (self.s/div) * ys
                        i.r[0] += 3 * (i.s/2.0) * cos(radians(i.a))
                        i.r[1] -= 3 * (i.s/2.0) * sin(radians(i.a))
                        self.s /= 2
                        i.cnm = True
                        hitLs = True
                        break
            #'''
            '''
            for i in astrds:
                self.r[0] += (self.s/div) * xs#float((cos(radians((self.ad)))))
                self.r[1] -= (self.s/div) * ys#float((sin(radians((self.ad)))))
                dx = int(self.r[0]-i.r[0])
                dy = int(self.r[1]-i.r[1])
                if self.hb.overlap(i.hb, (dx,dy)):
                    #i.s *= -1
                    #i.a += randint(-5,5)
                    i.a *= -1
                    self.health -= .5
                    self.r[0] -= 8 * (self.s/div) * xs
                    self.r[1] += 8 * (self.s/div) * ys
                    i.r[0] += 3 * (i.s/-2.0) * cos(radians(i.a))
                    i.r[1] -= 3 * (i.s/-2.0) * sin(radians(i.a))
                    self.s /= 2
                    i.cnm = True
                    break
            '''
        self.c = x
        self.s -= .025
        if self.s < 0:
            self.s = 0
            

    def rotate(self,deg):
        global roundEnd
        if not roundEnd:
            if self.a <= 0:
                self.a = 360
            self.a += deg
            #self.a = deg
            self.ad += deg
            #self.ad = deg
            self.i = pygame.transform.rotate(self.p, self.a)
            r = self.r
            #self.r = self.i.get_rect()
            self.r = self.i.get_rect(topleft=[r[0],r[1]])

    def fire(self):
        global st,lazer, cfr,shF
        self.pl = True
        if cfr:
            shF += 1
            cfr = False
            ad = float(self.ad)
            unp[0] = True
            #k = randint(-4,4)
            #print ad
            #ad += kd
            #print adf
            #print randint(-2,2)
            #sas = [randint(-10,10), randint(-10,10)]
            sas = [0,0]
            #print sas
            k = [self.r.center[0],self.r.center[1]]
           # for i in range(0,):
            k[0] += 40 * float(cos(radians(self.ad)))
            k[1] -= 40 * float(sin(radians(self.ad)))
            g = [k[0]+sas[0],k[1]+sas[1],self.r.center[0],self.r.center[1]]
            st.append(Bullet(g, self.r.center,True))
            lazer.play(lazer1)

class Bad2():
    def __init__(self,ai=None,pos=[320,320],off=None,image=None):
        if image is None:
            self.i = pygame.image.load("bad.png").convert()
        else:
            self.i = image
        #self.i.set_colorkey((255,255,255))
        self.i.set_colorkey((0,0,0))
        self.hb = pygame.mask.from_surface(self.i)
        #print self.hb
        #self.hb = pygame.mask.Mask((400,400))
        self.c = pos
        self.h = 50
        self.r = self.i.get_rect(topleft=self.c)
        if ai is None:
            self.afs = [15,45]
        else:
            self.afs = range(0,60,12)
        self.sn = False
        self.ai = ai
        if off is None:
            off = randint(1,15)
        self.sd = 0
        self.off = off
        self.dst = 1000
        self.s = 3
        self.dead = False
        self.dAni = False
        self.nm = None
        #randomness in movement so they wont stack as much
        self.Moff = randint(-30,30)
        #LAZER M8 vars
        self.lsC = [[0,0,255],[0,255,0],[255,255,0],[255,0,0]] #the list of lazer colors before damage happens
        self.lsCc = self.lsC[0] #the current lazer color
        self.lsTmax = 20 #the maximum time between changing colors of the lazer
        self.lsTcur = 0 #current time of the current of the color
        self.lsDo = False #makes the things run
        self.lsRc = 0 #lazer recharge
        self.lsRcmax = 15 #lazer recharge time
        self.lsCd = False
        

    def draw(self):
        global fnum
        #ai
        #ai must run less than 50 lines a frame so it will run at 60fps
        #only calculates AI every 8th frame, so it spreads out the intensity
        #3 AI's
        #None = Shooter Guy
        #True = LAZAR M8
        #False = Rapid Fire Sprayer
        if self.ai:
            global demo
            x = demo.c[0] - self.c[0]
            y = demo.c[1] - self.c[1]
            self.dst = int(sqrt(x**2 + y**2))
            if self.dst < 150:
                self.lsDo = True
            else:
                self.lsDo = False
                self.lsCc = self.lsC[0]
                self.lsTcur = 0
        if fnum + self.off in self.afs:
            #then do the AI
            #checks for it being dead
            if not self.dead:
                if self.ai is None:
                    self.nm = None
                    x = demo.c[0] - self.c[0]
                    y = demo.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst <= 300 + self.Moff:
                        self.sn = True
                    else:
                        self.sn = True
                        self.nm = self.angle()
                elif not self.ai:
                    self.sn = True
                    self.nm = None
                    x = demo.c[0] - self.c[0]
                    y = demo.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst >= 250 + self.Moff:
                        self.sn = True
                        self.nm = self.angle()
                else:
                    self.nm = None
                    x = demo.c[0] - self.c[0]
                    y = demo.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst >= 150 + self.Moff:
                        self.nm = self.angle()
        else:
            if not self.dead:
                if self.sn and self.ai is None:
                    self.fire()
                elif self.sn and not self.ai:
                    self.xfire()
                elif self.nm != None:
                    #pass
                    self.sn = False
                    self.r[0] += self.s * float((cos(radians(float(self.nm)))))
                    self.r[1] -= self.s * float((sin(radians(float(self.nm)))))
                if self.lsDo:
                    if self.lsTcur >= self.lsTmax:
                        self.lsTcur = 0
                        final = False
                        if self.lsCc != self.lsC[-1]:
                            for i in self.lsC:
                                if i == self.lsCc:
                                    final = True
                                elif final:
                                    self.lsCc = i
                                    break
                        else:
                            demo.health -= 10
                            self.lsCd = True
                            self.lsCc = self.lsC[0]
                            self.lsRc = 0
                    if not self.lsCd:
                        pygame.draw.line(screen, self.lsCc, [self.r.center[0],self.r.center[1]],[demo.r.center[0],demo.r.center[1]],2)
                        self.lsTcur += 1
                    else:
                        if self.lsRc >= self.lsRcmax:
                            self.lsCd = False
                        self.lsRc += 1
                    self.lsDo = False
                
        #drawing
        if not self.dead:
            if self.h <= 0:
                self.dead = True
                global exps
                exps.play(exps2)
            self.c = [self.r.center[0],self.r.center[1]]
            screen.blit(self.i, self.r)
        else:
            #do dead animation
            #explosion type sound
            pass
        #pygame.draw.line(screen, (255,0,0), player.c, self.c)

    def xfire(self):
        #print 'dfs'
        self.sn = False
        global player, st
        x = demo.r.center[0] - self.r.center[0]
        y = demo.r.center[1] - self.r.center[1]
        gg = [demo.r.center[0],demo.r.center[1],self.r.center[0],self.r.center[1]]
        st.append(Bullet2(gg,[self.r.center[0],self.r.center[1]],False,True))
        lazer22.play(lazer2)
    
    def fire(self):
        #print 'sd'
        self.sn = False
        global player,st, lazer2
        #x = player.c[0]- self.c[0]
        #y = player.c[1] - self.c[1]
        x = demo.r.center[0] - self.r.center[0]
        y = demo.r.center[1] - self.r.center[1]
        #dst = int(sqrt(x**2 + y**2))
        ad = 360-degrees(atan2(float(radians(float(y))),float(radians(float(x)))))
        #ad = degrees(ad)
        #print ad
        if ad >= 360:
            pass
            #ad -= 360
        self.sd = float(ad)
        #ad += randint(-5,5)
        g = [self.r.center[0],self.r.center[1]]
        #print 3 * cos(radians(ad))
        #print 3 * sin(radians(ad))
        for i in range(0,50):
            g[0] += 3 * float(cos(radians(ad)))
            g[1] -= 3 * float(sin(radians(ad)))
        #pygame.draw.line(screen, (0,0,255), [self.r.center[0],self.r.center[1]], g, 5)
        #st.append(Bullet(ad,[self.r.center[0],self.r.center[1]],False))

        gg = [demo.r.center[0],demo.r.center[1],self.r.center[0],self.r.center[1]]
        #gg[0] /= dst/3
        #gg[1] /= dst/3
        st.append(Bullet2(gg,[self.r.center[0],self.r.center[1]],False))
        #if pygame.mixer.find_channel() != None:
        lazer22.play(lazer2)

    def angle(self):
        global player
        x = demo.c[0]- self.c[0]
        y = demo.c[1] - self.c[1]
        ad = 360-degrees(atan2(float(radians(y)),float(radians(x))))
        return ad

class BadHPBar():
    def __init__(self,tId):
        self.id = tId

    def update(self):
        global htbl
        for pts in htbl:
            if pts.id == self.id:
                newR = pts.r.copy()
                perc = float((float(pts.h) / 50.0))
                pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-5,newR[2]+1,2),1)
                pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-5,newR[2]*perc,2),0)
        
class Bad():
    def __init__(self,ai=None,pos=[320,320],off=None,image=None,demo=False):
        if image is None:
            self.i = pygame.image.load("bad.png").convert()
            self.i2 = pygame.image.load("bad.png").convert()
        else:
            self.i = image
            self.i2 = image
        #self.i.set_colorkey((255,255,255))
        self.i.set_colorkey((0,0,0))
        self.i2.set_colorkey((0,0,0))
        self.hb = pygame.mask.from_surface(self.i)
        #print self.hb
        #self.hb = pygame.mask.Mask((400,400))
        self.c = pos
        self.h = 50
        self.r = self.i.get_rect(topleft=self.c)
        if ai is None:
            self.afs = [15,45]
        else:
            self.afs = range(0,60,12)
        self.sn = False
        self.ai = ai
        if off is None:
            off = randint(1,15)
        self.sd = 0
        self.off = off
        self.dst = 1000
        self.s = 3
        self.dead = False
        self.dAni = False
        self.nm = None
        #randomness in movement so they wont stack as much
        self.Moff = randint(-30,30)
        #LAZER M8 vars
        self.lsC = [[0,0,255],[0,255,0],[255,255,0],[255,0,0]] #the list of lazer colors before damage happens
        self.lsCc = self.lsC[0] #the current lazer color
        self.lsTmax = 20 #the maximum time between changing colors of the lazer
        self.lsTcur = 0 #current time of the current of the color
        self.lsDo = False #makes the things run
        self.lsRc = 0 #lazer recharge
        self.lsRcmax = 15 #lazer recharge time
        self.lsCd = False
        self.demo = demo
        '''health bars'''
        self.id = str(pos[0])+str(pos[1])
        self.tdm = BadHPBar(str(pos[0])+str(pos[1]))
        #self.tdm = BadHPBar()
        

    def draw(self):
        global fnum
        #ai
        #ai must run less than 50 lines a frame so it will run at 60fps
        #only calculates AI every 8th frame, so it spreads out the intensity
        #3 AI's
        #None = Shooter Guy
        #True = LAZAR M8
        #False = Rapid Fire Sprayer
        if self.ai:
            global player
            x = player.c[0] - self.c[0]
            y = player.c[1] - self.c[1]
            self.dst = int(sqrt(x**2 + y**2))
            if self.dst < 150:
                self.lsDo = True
            else:
                self.lsDo = False
                self.lsCc = self.lsC[0]
                self.lsTcur = 0
        if fnum + self.off in self.afs:
            #then do the AI
            #checks for it being dead
            if not self.dead:
                if self.ai is None:
                    self.nm = None
                    x = player.c[0] - self.c[0]
                    y = player.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst <= 300 + self.Moff:
                        self.sn = True
                    else:
                        self.sn = True
                        self.nm = self.angle()
                elif not self.ai:
                    self.sn = True
                    self.nm = None
                    x = player.c[0] - self.c[0]
                    y = player.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst >= 250 + self.Moff:
                        self.sn = True
                        self.nm = self.angle()
                else:
                    self.nm = None
                    x = player.c[0] - self.c[0]
                    y = player.c[1] - self.c[1]
                    self.dst = int(sqrt(x**2 + y**2))
                    if self.dst >= 150 + self.Moff:
                        self.nm = self.angle()
        else:
            if not self.dead:
                self.c = [self.r.center[0],self.r.center[1]]
                x = player.c[0]- self.c[0]
                y = player.c[1] - self.c[1]
                ad = 360-degrees(atan2(float(radians(y)),float(radians(x))))
                self.i = pygame.transform.rotate(self.i2, ad)
                if self.sn and self.ai is None:
                    self.fire()
                elif self.sn and not self.ai:
                    self.xfire()
                elif self.nm != None:
                    #pass
                    self.sn = False
                    self.r[0] += self.s * float((cos(radians(float(self.nm)))))
                    self.r[1] -= self.s * float((sin(radians(float(self.nm)))))
                if self.lsDo:
                    if self.lsTcur >= self.lsTmax:
                        self.lsTcur = 0
                        final = False
                        if self.lsCc != self.lsC[-1]:
                            for i in self.lsC:
                                if i == self.lsCc:
                                    final = True
                                elif final:
                                    self.lsCc = i
                                    break
                        else:
                            player.health -= 10
                            self.lsCd = True
                            self.lsCc = self.lsC[0]
                            self.lsRc = 0
                    if not self.lsCd:
                        pygame.draw.line(screen, self.lsCc, [self.r.center[0],self.r.center[1]],[player.r.center[0],player.r.center[1]],2)
                        self.lsTcur += 1
                    else:
                        if self.lsRc >= self.lsRcmax:
                            self.lsCd = False
                        self.lsRc += 1
                    self.lsDo = False
                
        #drawing
        if not self.dead:
            if self.h <= 0:
                self.dead = True
                global exps
                exps.play(exps2)
            '''
            self.c = [self.r.center[0],self.r.center[1]]
            x = player.c[0]- self.c[0]
            y = player.c[1] - self.c[1]
            ad = 360-degrees(atan2(float(radians(y)),float(radians(x))))
            self.i = pygame.transform.rotate(self.i2, ad)
            '''
            #self.tdm.update()
            perc = float(self.h/50.0)
            newR = self.r.copy()
            #pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-6,newR[2]+1,3),1)
            #pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-5,newR[2]*perc,2),0)
            pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-6,newR[2]+1,3),1)
            pygame.draw.rect(screen, (0,255,0), (newR[0]-1,newR[1]-5,newR[2]*perc+1,2),0)
            screen.blit(self.i, self.r)
        else:
            #do dead animation
            #explosion type sound
            pass
        #pygame.draw.line(screen, (255,0,0), player.c, self.c)

    def xfire(self):
        self.sn = False
        global player, st
        x = player.r.center[0] - self.r.center[0]
        y = player.r.center[1] - self.r.center[1]
        gg = [player.r.center[0],player.r.center[1],self.r.center[0],self.r.center[1]]
        st.append(Bullet(gg,[self.r.center[0],self.r.center[1]],False,True))
        lazer22.play(lazer2)
    
    def fire(self):
        self.sn = False
        global player, st, lazer2
        #x = player.c[0]- self.c[0]
        #y = player.c[1] - self.c[1]
        x = player.r.center[0] - self.r.center[0]
        y = player.r.center[1] - self.r.center[1]
        #dst = int(sqrt(x**2 + y**2))
        ad = 360-degrees(atan2(float(radians(float(y))),float(radians(float(x)))))
        #ad = degrees(ad)
        #print ad
        self.sd = float(ad)
        #ad += randint(-5,5)
        g = [self.r.center[0],self.r.center[1]]
        #print 3 * cos(radians(ad))
        #print 3 * sin(radians(ad))
        for i in range(0,50):
            g[0] += 3 * float(cos(radians(ad)))
            g[1] -= 3 * float(sin(radians(ad)))
        #pygame.draw.line(screen, (0,0,255), [self.r.center[0],self.r.center[1]], g, 5)
        #st.append(Bullet(ad,[self.r.center[0],self.r.center[1]],False))
        gg = [player.r.center[0],player.r.center[1],self.r.center[0],self.r.center[1]]
        #gg[0] /= dst/3
        #gg[1] /= dst/3
        st.append(Bullet(gg,[self.r.center[0],self.r.center[1]],False))
        #if pygame.mixer.find_channel() != None:
        lazer22.play(lazer2)

    def angle(self):
        global player
        x = player.c[0]- self.c[0]
        y = player.c[1] - self.c[1]
        ad = 360-degrees(atan2(float(radians(y)),float(radians(x))))
        return ad

class Asteroid():
    #Evil random floating things
    def __init__(self,pos,angle,ids):
        self.pos = pos
        self.ids = ids
        self.image = pygame.image.load('asteriod2.png').convert()
        self.image.set_colorkey((255,255,255))
        self.r = self.image.get_rect(topleft=pos)
        self.hb = pygame.mask.from_surface(self.image)
        self.s = 3.34
        self.hpl = False
        self.a = angle
        self.cnm = False

    def update2(self):
        #maybe better optimized
        tps = [self.r.center[0],self.r.center[1]]
        global demo
        for i in [1,2,3]:
            tps[0] += float((self.s/3.0)*(cos(radians(self.a))))
            tps[1] -= float((self.s/3.0)*(sin(radians(self.a))))
            dx = int(demo.c[0]-tps[0])
            dy = int(demo.c[1]-tps[1])
            if self.hb.overlap(demo.hb, [dx,dy]) and not self.hpl:
                    demo.health -= 2
                    demo.s /= 2
                    tps[0] -= 4*(self.s/3)*(cos(radians(self.a)))
                    tps[1] += 4*(self.s/3)*(sin(radians(self.a)))
                    self.s *= -1
                    self.hpl = True
                    self.cnm = True
                    break
        self.r = self.image.get_rect(center=tps)
        if self.r[0] > 640:
            self.r[0] -= 640
        if self.r[0] < 0:
            self.r[0] += 640
        if self.r[1] > 640:
            self.r[1] -= 640
        if self.r[1] < 0:
            self.r[1] += 640
        screen.blit(self.image,self.r)
    
    def update(self):
        tps = [self.r.center[0],self.r.center[1]]
        lst = [1,2,3]
        try:
            global asT2, asT
        except:
            pass
        hitLs = False
        if not self.cnm:
            '''
            dx = int(player.c[0]-tps[0])
            dy = int(player.c[1]-tps[1])
            if self.hb.overlap(player.hb, [dx,dy]) and not self.hpl:
                player.health -= 7
                player.s /= 2
                tps[0] -= 4*(self.s/3)*(cos(radians(self.a)))
                tps[1] += 4*(self.s/3)*(sin(radians(self.a)))
                self.s *= -1
                asT2.play(asT)
                self.hpl = True
                self.cnm = True
            '''
            for ik in lst:
                tps[0] += float((self.s/3.0)*(cos(radians(self.a))))
                tps[1] -= float((self.s/3.0)*(sin(radians(self.a))))
                dx = int(player.c[0]-tps[0])
                dy = int(player.c[1]-tps[1])
                if not hitLs:
                    if self.hb.overlap(player.hb, [dx,dy]) and not self.hpl:
                        player.health -= 3
                        pC = [player.r.center[0],player.r.center[1]]
                        pC[0] -= player.total[0]
                        pC[1] += player.total[1]
                        if pC[0] > 640:
                            pC[0] -= 640
                        if pC[0] < 0:
                            pC[0] += 640
                        if pC[1] > 640:
                            pC[1] -= 640
                        if pC[1] < 0:
                            pC[1] += 640
                        player.r = player.i.get_rect(center=pC)
                        player.s /= 16.0
                        player.s = round(player.s,3)
                        player.total = [player.s * float((cos(radians(player.ad)))),player.s * float((sin(radians(player.ad))))]
                        tps[0] -= 4*(self.s/3.0)*(cos(radians(self.a)))
                        tps[1] += 4*(self.s/3.0)*(sin(radians(self.a)))
                        self.s *= -1
                        asT2.play(asT)
                        self.hpl = True
                        self.cnm = True
                        hitLs = True
                        break
                    for th in htbl:
                        dx = int(th.r.center[0]-tps[0])
                        dy = int(th.r.center[1]-tps[1])
                        if self.hb.overlap(th.hb, [dx,dy]) and not self.hpl:
                                tps[0] -= 4*(self.s/3.0)*(cos(radians(self.a)))
                                tps[1] += 4*(self.s/3.0)*(sin(radians(self.a)))
                                self.s *= -1
                                self.a += randint(-5,5)
                                th.h -= 4
                                asT2.play(asT)
                                self.hpl = True
                                hitLs = True
                                break
                        else:
                            self.hpl = False
                for i in astrds:
                        if i.ids != self.ids:
                            dx = int(i.r.center[0]-tps[0])
                            dy = int(i.r.center[1]-tps[1])
                            if self.hb.overlap(i.hb, [dx,dy]) and not self.hpl:
                                tps[0] -= 4*(self.s/3.0)*(cos(radians(self.a)))
                                tps[1] += 4*(self.s/3.0)*(sin(radians(self.a)))
                                self.s *= -1
                                self.a += randint(-5,5)
                                kks = [i.r.center[0],i.r.center[1]]
                                kks[0] -= 2*(i.s/3.0)*cos(radians(i.a))
                                kks[1] += 2*(i.s/3.0)*sin(radians(i.a))
                                i.r = i.image.get_rect(center=kks)
                                self.hpl = True
                                asT2.play(asT)
                                break
                            else:
                                self.hpl = False
            '''
            for i in lst:
                #if not True:
                    #print 'the way'
                #"""
                tps[0] += float((self.s/3.0)*(cos(radians(self.a))))
                tps[1] -= float((self.s/3.0)*(sin(radians(self.a))))
                dx = int(player.c[0]-tps[0])
                dy = int(player.c[1]-tps[1])
                if self.hb.overlap(player.hb, [dx,dy]) and not self.hpl:
                    player.health -= 2
                    player.s /= 2
                    tps[0] -= 4*(self.s/3)*(cos(radians(self.a)))
                    tps[1] += 4*(self.s/3)*(sin(radians(self.a)))
                    self.s *= -1
                    self.hpl = True
                    self.cnm = True
                    break
                #"""
                #tps[0] += float((self.s/3.0)*(cos(radians(self.a))))
                #tps[1] -= float((self.s/3.0)*(sin(radians(self.a))))
                else:
                #if 'f' == 'f':
                    for i in astrds:
                        if i.ids != self.ids:
                            dx = int(i.r.center[0]-tps[0])
                            dy = int(i.r.center[1]-tps[1])
                            if self.hb.overlap(i.hb, [dx,dy]) and not self.hpl:
                                tps[0] -= 4*(self.s/3.0)*(cos(radians(self.a)))
                                tps[1] += 4*(self.s/3.0)*(sin(radians(self.a)))
                                self.s *= -1
                                self.a += randint(-5,5)
                                kks = [i.r.center[0],i.r.center[1]]
                                kks[0] -= 2*(i.s/3.0)*cos(radians(i.a))
                                kks[1] += 2*(i.s/3.0)*sin(radians(i.a))
                                i.r = i.image.get_rect(center=kks)
                                self.hpl = True
                                break
                            else:
                                self.hpl = False
                    for i in htbl:
                        dx = int(i.r.center[0]-tps[0])
                        dy = int(i.r.center[1]-tps[1])
                        if self.hb.overlap(i.hb, [dx,dy]) and not self.hpl:
                            tps[0] -= 4*(self.s/3.0)*(cos(radians(self.a)))
                            tps[1] += 4*(self.s/3.0)*(sin(radians(self.a)))
                            self.s *= -1
                            self.a += randint(-5,5)
                            i.h -= 7
                            self.hpl = True
                            break
                        else:
                            self.hpl = False
            '''
        else:
            self.cnm = False
            tps[0] += 4*(self.s)*(cos(radians(self.a)))
            tps[1] -= 4*(self.s)*(sin(radians(self.a)))
        self.r = self.image.get_rect(center=tps)
        if self.r[0] > 640:
            self.r[0] -= 640
        if self.r[0] < 0:
            self.r[0] += 640
        if self.r[1] > 640:
            self.r[1] -= 640
        if self.r[1] < 0:
            self.r[1] += 640
        screen.blit(self.image,self.r)
        #self.r[0] += self.s*(cos(radians(self.a)))
        #self.r[1] -= self.s*(sin(radians(self.a)))
        
def setup():
    global lazer1,lazer,lazer2,lazer22,exps2,exps,eng2,eng,mainT,maint,curSound
    #images 
    global player1,bulletI,badI,asteroidI,stars,men,menT,butI,butI2,click,t1,t2
    global bHt, asT, bH2, asT2
    #sounds
    if curSound == 0:
        #pygame.mixer.init()
        #player sound, louder, AI sound, quieter
        lazer1 = pygame.mixer.Sound('Laser_Shoot.wav')
        lazer1.set_volume(.35)
        lazer = pygame.mixer.Channel(0)
        bHt = pygame.mixer.Sound('bdHt.wav')
        bHt.set_volume(.35)
        bH2 = pygame.mixer.Channel(2)
        curSound = 1
    elif curSound == 1:
        lazer2 = pygame.mixer.Sound('Laser_Shoot.wav')
        lazer2.set_volume(.05)
        lazer22 = pygame.mixer.Channel(1)
        curSound = 2
    elif curSound == 2:
        #explosion sound
        exps2 = pygame.mixer.Sound('xps.wav')
        exps2.set_volume(.45)
        exps = pygame.mixer.Channel(2)
        curSound = 3
    elif curSound == 3:
        #engine sound
        eng2 = pygame.mixer.Sound('engine.wav')
        eng2.set_volume(.5)
        eng = pygame.mixer.Channel(3)
        curSound = 4
        asT = pygame.mixer.Sound('asCr.wav')
        asT.set_volume(.35)
        asT2 = pygame.mixer.Channel(5)
    elif curSound == 4:
        #main theme
        mainT = pygame.mixer.Sound('theme.wav')
        mainT.set_volume(.33)
        maint = pygame.mixer.Channel(4)
        curSound = 5
    #images
    elif curSound == 5:
        player1 = pygame.image.load('hero.png').convert()
        curSound = 6
    elif curSound == 6:
        bulletI = pygame.image.load('bullet.png').convert()
        curSound = 7
    elif curSound == 7:
        badI = pygame.image.load('bad.png').convert()
        curSound = 8
    elif curSound == 8:
        stars = []
        for i in range(0,110):
            x = randint(0,640)
            y = randint(0,640)
            stars.append([x,y])
        curSound = 9
    elif curSound == 9:
        men = pygame.mixer.Sound('button.wav')
        men.set_volume(.45)
        menT = pygame.mixer.Channel(5)
        curSound += 1
    elif curSound == 10:
        butI = pygame.image.load('buton.png').convert()
        curSound += 1
    elif curSound == 11:
        butI2 = pygame.image.load('buton2.png').convert()
        curSound += 1
    elif curSound == 12:
        click = pygame.mixer.Sound('click.wav')
        curSound += 1
    elif curSound == 13:
        t2 = pygame.image.load('tablet.png').convert()
        t1 = pygame.image.load('tablet2.png').convert()
        curSound += 1
    else:
        asteroidI = pygame.image.load('asteriod2.png').convert()
        global curP
        curP = 'Done'

class Button():
    #class for buttons in the main menu
    def __init__(self,coords,place,text):
        self.place = place
        global butI,butI2,butT
        self.imageUn = butI.copy()
        self.imageP = butI2.copy()
        self.r = self.imageUn.get_rect(topleft=coords)
        tx = butT.render(text,1,(255,0,0))
        txS = butT.size(text)
        txS2 = [txS[0]/2.0,txS[1]/2.0]
        rS = [self.r[2]/2.0,self.r[3]/2.0]
        rrr = [rS[0]-txS2[0],rS[1]-txS2[1],txS[0],txS[1]]
        self.imageUn.blit(tx,rrr)
        self.imageP.blit(tx,rrr)
        self.imageUn.set_colorkey((255,255,255))
        self.imageP.set_colorkey((255,255,255))
        self.pressed = False

    def draw(self):
        global men,menT
        msP = pygame.mouse.get_pos()
        if self.r.collidepoint(msP[0],msP[1]):
            screen.blit(self.imageP,self.r)
            if not self.pressed:
                self.pressed = True
                menT.play(men)
        else:
            screen.blit(self.imageUn,self.r)
            self.pressed = False

class Thingy():
    def __init__(self,coords,info,override=False,let='a'):
        global t2,t1,tF,tF2
        self.info = info
        self.i1 = t1.copy()
        self.i1.set_colorkey((255,255,255))
        self.i2 = t2.copy()
        self.i2.set_colorkey((255,255,255))
        self.r = self.i1.get_rect(topleft=coords)
        self.pd = False
        #draw the 3 things
        #plus the label
        labs = ['Seed','Difficulty','Score']
        y = 20
        g = 0
        if not override:
            for i in info:
                t21 = tF2.render(str(labs[g]),0,(255,15,15))#(196,6,6))
                ts2 = tF2.size(str(labs[g]))
                t212 = tF2.render(str(labs[g]),0,(158,28,25))
                self.i1.blit(t21,[self.r[2]/2-ts2[0]/2,y,100,100])
                self.i2.blit(t212,[self.r[2]/2-ts2[0]/2,y,100,100])
                t21 = tF.render(str(i),0,(255,0,0))
                ts2 = tF.size(str(i))
                t212 = tF.render(str(i),0,(140,0,0))
                self.i1.blit(t21,[self.r[2]/2-ts2[0]/2,y+30,100,100])
                self.i2.blit(t212,[self.r[2]/2-ts2[0]/2,y+30,100,100])
                y += 60
                g += 1
        else:
            labs = ['Option %s'%let]
            fsfs = 180
            self.i1 = pygame.transform.scale(self.i1, (115,fsfs))
            self.i2 = pygame.transform.scale(self.i2, (115,fsfs))
            self.r = self.i1.get_rect(topleft=coords)
            t21 = tF2.render(str(labs[0]),0,(255,15,15))#(196,6,6))
            ts2 = tF2.size(str(labs[0]))
            t212 = tF2.render(str(labs[0]),0,(158,28,25))
            self.i1.blit(t21,[self.r[2]/2-ts2[0]/2,y,100,100])
            self.i2.blit(t212,[self.r[2]/2-ts2[0]/2,y,100,100])
            t21 = tF.render(str(info),0,(255,0,0))
            ts2 = tF.size(str(info))
            t212 = tF.render(str(info),0,(140,0,0))
            self.i1.blit(t21,[self.r[2]/2-ts2[0]/2,y+30,100,100])
            self.i2.blit(t212,[self.r[2]/2-ts2[0]/2,y+30,100,100])

    def draw(self):
        global men, menT
        mp = pygame.mouse.get_pos()
        if self.r.collidepoint(mp[0],mp[1]):
            screen.blit(self.i2,self.r)
            if not self.pd:
                menT.play(men)
                self.pd = True
        else:
            self.pd = False
            screen.blit(self.i1,self.r)

    def click(self):
        global click,seed
        click.play()
        seed = self.info[0]   
      
screen = pygame.display.set_mode((640,640))
icons = pygame.image.load('icon.png')
pygame.display.set_icon(icons)
pygame.display.set_caption("Space Enclave","Space Enclave")
pygame.font.init()
lazer1,lazer,lazer2,lazer22,exps2,exps,eng2,eng,mainT,maint,t1 = range(0,11)
player1,bulletI,badI,asteroidI,men,menT,butI,butI2,click,t2 = range(0,10)
bHt, asT, bH2, asT2 = 0,1,2,3
'''
#sounds
pygame.mixer.init()
#player sound, louder, AI sound, quieter
lazer1 = pygame.mixer.Sound('Laser_Shoot.wav')
lazer1.set_volume(.35)
lazer = pygame.mixer.Channel(0)
lazer2 = pygame.mixer.Sound('Laser_Shoot.wav')
lazer2.set_volume(.05)
lazer22 = pygame.mixer.Channel(1)
#explosion sound
exps2 = pygame.mixer.Sound('xps.wav')
exps2.set_volume(.45)
exps = pygame.mixer.Channel(2)
#engine sound
eng2 = pygame.mixer.Sound('engine.wav')
eng2.set_volume(.5)
eng = pygame.mixer.Channel(3)
#main theme
mainT = pygame.mixer.Sound('theme.wav')
mainT.set_volume(.33)
maint = pygame.mixer.Channel(4)
;'''
#key stuff
pygame.key.set_repeat(10,10)
pygame.key.set_repeat(5,5)
#a list of keys to make sure they can't be spammed
unp = [False]
#space bar, and whatever others
#lists of stuff and things
st = []
#htbl = [Bad(ai=None),Bad(ai=False,pos=[230,230]),Bad(ai=False,pos=[450,450]), Bad(ai=None,pos=[50,50])]#,Bad(ai=True,pos[0,0]),Bad(ai=True,pos=[560,560])]#,Bad(pos=[150,10]),Bad(pos=[450,450])]
'''
htbl = [Bad(ai=None),Bad(ai=True,pos=[230,230]),Bad(ai=False,pos=[450,450])
        , Bad(ai=None,pos=[50,50]),Bad(ai=False,pos=[620,62]), Bad(ai=True,pos=[60,500])]
'''
#htbl = [Bad(ai=True)]
'''
astrds = [Asteroid([350,350],63,'s'),Asteroid([125,125], 24,'d'),
          Asteroid([420,400],127,'sf'), Asteroid([500,200],265,'t')]
'''
stars = []
#locations are 0 = credits, 1 = menu, 2 = Enter Seed, 3 = loading screen, 4 = main_game, 5 = high scores(EXPERIMENTAL), 6 = Tutorial, 7 = dev
# more locations (too many ahhh *runs* lol) 8 = Recent scores room thingy, 9 = random seeds room
#potential locations are ; Recent seed room with scores, highscore room with the scores for each dif, a room with a couple of random seeds to chose from 
location = 0
loaded = False
fnum = 1

#random cool dev stuff
pygame.mixer.init()
clock = pygame.time.Clock()
fpsf = pygame.font.Font(None, 15)
ldF = pygame.font.Font(None, 23) #loading screen font
tsF = pygame.font.SysFont('krungthep',45)
tsF2 = pygame.font.SysFont('krungthep',27)
butT = pygame.font.SysFont('krungthep',25)
splsF = pygame.font.SysFont('krungthep',12)
tF = pygame.font.SysFont('krungthep',18)
tF2 = pygame.font.SysFont('krungthep',20)
#game loop
lowest = 60
oldFrame = pygame.surface.Surface((640,640))
oldFrame.fill([0,0,0])
frameNumber = 0
#print cos(radians(63)), '/', sin(radians(63))  
#makeSeed()
#credits vars
phases = ['Grand', 'Loading']
curP = phases[0]
curPf = 0
curPm = 30
curSound = 0
letters = ''
#setup()
sumSters = []
for i in range(0,110):
    sumSters.append([randint(0,640),randint(0,640)])
splash = []
new_splash = 'Umm.... there has been an error. Houston, we have a problem.'
fils = open('splash.rsc','r')
while True:
    try:
        newt = fils.readline()
        if newt.strip() == '':
            break
        splash.append(newt)
    except:
       break
fils.close()
#lore component
lores = []
fils = open('lore.rsc','r')
while True:
    try:
        newt = fils.readline()
        if newt.strip() == '':
            break
        lores.append(newt)
    except:
       break
fils.close()

nedSp = ['um',[23,23,23,23]]
#loading stuff
stage = 0 # out of creating, intrepting(5 steps), creating(14 times no matter what) so 20
seed = 's' # the seed of the level
dif = 0 # difficulty of the level, used to make scores more balanced.
infos = []

#intSeed(0,[],'Ac3-Ad-Bg32-B4/2|3|34|87|-S5')
htbl = []
astrds = []
#timer
start = 0 #will be assigned to the clock

#computer based high-score system
highs = open('hs.rsc','r')
#format is dificulty|score
#so .375|2750.3 could be a score
highSc2 = []
while True:
    kes = highs.readline()
    if kes.strip() == '':
        break
    else:
        highSc2.append(str(kes).replace('\n',''))
highs.close()
highSc = []
for i in highSc2:
    po = i.split('|')
    highSc.append(po)
abad = False
#difficulty max thing
maxD = 32.0
maxD = 20.25
#firing delay
fdm = 10
fd = 0
cfr = True

#stores the last 3 games
#format
#seed|dif|score
lG2 = []
fils = open('prvs.rsc','r')
while True:
    try:
        newt = fils.readline()
        if newt.strip() == '':
            break
        lG2.append(newt)
    except:
       break
fils.close()
#print lG2
lG = []
for i in lG2:
    sdf = []
    po = i.split('|')
    for isd in po:
        sdf.append(isd.replace('\n',''))
    lG.append(sdf)
'''for recording stats'''
#shots fired, baddies hit, asteroids hit, baddies killed, deaths
#wins, time spent playing (in levels)
#will calculate the win/loss ratio
stats2 = []
stats = []
fils = open('stats.rsc','r')

while True:
    try:
        newt = fils.readline()
        if str(newt).strip() == '':
            break
        stats2.append(newt)
    except:
       break
fils.close()
for i in stats2:
    stats.append(int(str(i).replace('\n','')))
#print stats
logos = pygame.image.load('grandP2.png').convert()
timesG = 0

'''
Stuff to do
-Make movement not total shit
-Make proper file structure
-Remove redundant code
'''
max_fps = stats[-1]
fps_y = stats[-1] #290-380
fps_x = 460
max_fps = 200

while True:
    if location == 0:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        if curP == phases[0]:
            #my logo and stuff
            #screen.fill((0,251,255))
            screen.fill((125,125,255))
            for i in sumSters:
                pygame.draw.rect(screen, (0,255,255), [i[0],i[1],2,2])
            txtx = tsF.render('The Grand Annihilator', 0, (255,0,0))
            t23 = tsF.size('The Grand Annihilator')
            screen.blit(txtx, (320-t23[0]/2,15,1000,1000))
            screen.blit(logos, (320-256,350-256,1000,1000))
            pygame.draw.rect(screen,(0,255,0), (320-257,350-254,515,513),5)
            #curP = phases[1]
            timesG += 1
            if timesG >= 120:
                curP = phases[1]
            clock.tick(60)
        elif curP == phases[1]:
            #loading screen
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            setup()
            #text
                #loadind
            txt = ldF.render("Loading Resources", 0, (255,0,0))
            screen.blit(txt, (247,275,1000,1000))
                #game title
                #space enclave
            tx = tsF.render('Space Enclave',0,(255,0,0))
            screen.blit(tx, (149,150,1000,1000))
                #dev info
            txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
            screen.blit(txtx, (468,630,1000,1000))
            #loading bar
            pygame.draw.rect(screen, (0,255,0), (245,305,150,25),2)
            pygame.draw.rect(screen, (0,255,0), (245,305,
                             int(150 * (curSound/14.0)),25),0)
            #control how long it takes to load
            #clock.tick(4)
            clock.tick(10)
        else:
            location = 1
            buts = [Button((216,490),2,'Tutorial'),Button((216,170),3,'Play Game'),
                    Button((216,410),5,'Statistics'), Button((216,250),6,'Set Game Seed'),
                    #Button((216,490),5,"Anvil Account"), Button((216,250),6,'Set Game Seed'),
                    Button((216,330),8,'Recent Games')]
        ScreenUpdate(screen)
    if location == 5:
        #stats room
        #has its own loop cause it's 'cool'
        '''
        #shots fired, baddies hit, asteroids hit, baddies killed, deaths
        #wins, time spent playing (in levels)
        #will calculate the win/loss ratio'''
        sents = ['Shots Fired: %s'%str(stats[0]),
                 'Enemies Hit: %s'%str(stats[1]),
                 'Accuracy: %s%%' %str(round(100*(float(stats[1])/(float(stats[0])+float(stats[2]))),2)),
                 'Shots Per Kill: %s' %str(round(float(stats[0])/float(stats[3]),2)), 
                 'Enemies Killed: %s'%str(stats[3]),
                 'Asteroids Hit: %s'%str(stats[2]),
                 'Deaths: %s'%str(stats[4]),
                 'Wins: %s'%str(stats[5]),
                 'Total Points Scored',
                 str(stats[7])]
        from datetime import datetime,timedelta
        inGame = 'Time Spent in Game'
        sec = timedelta(seconds=int(stats[6]))
        d = datetime(1,1,1) + sec
        sents.append(inGame)
        inGame = ""
        '''
        if d.day > 0:
            inGame += '%s Days:'%str(int(d.day)-1)
        '''
        if d.hour > 0 or d.day > 0:
            inGame += '%s Hours:'%str(d.hour+24*(int(d.day)-1))
        if d.minute > 0:
            inGame += '%s Minutes:'%str(d.minute)
        if d.second > 0:
            inGame += '%s Seconds'%str(d.second)
        sents.append(inGame)
        daBk = Button((15,15),1,'Back')
        daBk.imageUn = pygame.transform.scale(daBk.imageUn, (106,34))
        daBk.imageP = pygame.transform.scale(daBk.imageP, (106,34))
        daBk.r = pygame.rect.Rect([0,0],[108,36])
        kts = False
        while True:
            screen.fill((0,0,0))
            y = 120
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    msp = pygame.mouse.get_pos()
                    if daBk.r.collidepoint(msp[0],msp[1]):
                        click.play()
                        kts = True
            if kts:
                break
            odd = 1
            for i in sents:
                if odd%2==0:
                    txt = tF2.render(i, 1, (255,0,0))
                else:
                    txt = tF2.render(i, 1, (0,0,255))
                odd += 1
                txt2 = tF2.size(i)
                screen.blit(txt, [320-txt2[0]/2,y,1000,1000])
                y += 40
            txt = tsF.render('Statistics',1,(255,0,0))
            txt2 = tsF.size('Statistics')
            txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
            screen.blit(txtx, (468,630,1000,1000))
            screen.blit(txt,[320-txt2[0]/2,60,1000,1000])
            daBk.draw()
            ScreenUpdate(screen)
            clock.tick(60)
        location = 1
        
    if location == 1:
        screen.fill((0,0,0))
        for i in sumSters:
            pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
        #menu
        #only 3 options
        #play, option screen and umm... pizza
        #high-score thingy, with sign-in
        #the sign-in will be email based
        #also shows fps thingy
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                for i in buts:
                    if i.r.collidepoint(msP[0],msP[1]):
                        location = i.place
                        if location == 5:
                            pass
                            #location = 1
                        else:
                            while True:
                                new_splash = choice(splash)
                                #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
                                if new_splash == 'Lore':
                                    perc = randint(1,100)
                                    if perc <= 50:
                                        #new_splash = choice(lores)
                                        break
                                    else:
                                        pass
                                else:
                                    break
                            ks = splsF.size(new_splash.replace('\n',''))
                            nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]
                        click.play()
        msP = pygame.mouse.get_pos()
        gg2 = pygame.mouse.get_rel()[1]
        if fps_x+20 < msP[0] < fps_x+90 and 300 < msP[1] < 400 and pygame.mouse.get_pressed()[0]:
            fps_y += gg2
            max_fps -= gg2            
        if 120 < 120-fps_y:
            fps_y = 0
        if 120-fps_y < 30:
            fps_y = 90
        if max_fps < 30:
            max_fps = 30
        if max_fps > 120:
            max_fps = 120
            #draw the text showing the current fps
        txtx = fpsf.render(str(120-fps_y), 0, (255,0,0))
        screen.blit(txtx, (fps_x+125,300+fps_y,1000,1000))
        
        
        #draws buttons
        for i in buts:
            i.draw()
        #text
        tx = tsF.render('Space Enclave',0,(255,0,0))
        screen.blit(tx, (149,70,1000,1000))
        txtx = fpsf.render('The Grand Annihilator, 2015-2017', 0, (255,0,0))
        screen.blit(txtx, (468,630,1000,1000))
        txt = fpsf.render('v0.0.1',0,(255,0,0))
        screen.blit(txt, (2,630,1000,1000))
        #updates and stuff
        
        ScreenUpdate(screen)
        clock.tick(300)
    if location == 2:
        #tutorial
        #explains everything, score, movement, shooting and other things.
        #this is going to take a long time to code so yeah


        objcts = [['Press',1,False],['movement',550,False],['speed',20,False],['firing',10,False],
                  ['bads ded',3, False],['astrH',2,False],['time',30,False]]#list of the objectives required to move on
        #first is the identifier, second is the requirement of that obective,third is if its completed or not
        '''stats that need to be created'''
        dst,damage,speed,badT,asH,time=[0,0,0,0,0,0]
        #demo player and bots and stuff
        demo = Player2()
        astrds = [Asteroid([480,480],45,'df')]
        htbl = [Bad2(pos=[200,200]),Bad2(ai=False,pos=[500,300]),Bad2(ai=True,pos=[50,500])]
        #htbl = [Bad2(ai=False,pos=[200,200])]
        #has its own loop because it needs to :)
        roundEnd = False
        upsD = False
        uspD = False
        shF = 0
        st = []
        firing = False
        fnum = 0
        cloct = 0
        aT = 0
        cT = 0
        astT = 45
        while True:
            screen.fill((0,0,0))
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            if not cfr:
                if fdm+8 > fd and demo.pl:
                    fd += 1
                elif fdm > fd and not demo.pl:
                    fd += 1
                    demo.fl = True
                else:
                    fd = 0
                    cfr = True
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    objcts[0][2] = True
                    if event.key == K_w or event.key == K_UP:
                        #player.s = 1 + float(player.s/10.0)
                        demo.s += .125
                        eng.stop()
                        eng.play(eng2)
                    elif event.key == K_s or event.key == K_DOWN:
                        demo.s -= .125
                        if demo.s < 0:
                            demo.s = 0
                        #player.s = (player.s/10.0) - 1
                    if event.key == K_d or event.key == K_RIGHT:
                        #player.a -= 5
                        #player.rotate(-1.25)
                        demo.rotate(-2.5)
                        #player.fire()
                    if event.key == K_a or event.key == K_LEFT:
                        #player.a += 5
                        #player.rotate(1.25)
                        demo.rotate(2.5)
                        #player.fire()
                    if event.key == K_SPACE:
                        demo.fire()
                        unp[0] = True
                    if event.key == K_f and not upsD:
                        upsD = True
                        if not firing:
                            firing = True
                        else:
                            firing = False
                        '''
                    if event.key == K_COMMA:
                        player.rotate(1.25)
                    if event.key == K_PERIOD:
                        player.rotate(-1.25)
                        '''
                    
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        unp[0] = False
                    if event.key == K_f:
                        upsD = False
            '''goes through the objectives'''
            if objcts[0][2]:
                if objcts[1][2]:
                    if objcts[2][2]:
                        if objcts[3][2]:
                            if objcts[4][2]:
                                if objcts[5][2]:
                                    if objcts[6][2]:
                                        cloct += 1
                                        #done with all expressions
                                        if cloct >= 480:
                                            break
                                        else:
                                            txt = 'You have now completed the tutorial'
                                            txt2 = 'Good Luck and Have Fun'
                                    else:
                                        #will explain the clock
                                        cT += 1
                                        if cT >= 480:
                                            objcts[6][2] = True
                                            cloct = 0
                                        else:
                                            nowt = 60-cloct
                                            d2 = tF.render(str(nowt),0,(255,0,0))
                                            ds2 = tF.size(str(nowt))
                                            screen.blit(d2, (320-ds2[0]/2,80,ds2[0],ds2[1]))
                                            txt = 'The clock is a major component of your score'
                                            txt2 = 'It has been moved lower for reasons'
                                else:
                                    #asteroids
                                    #angle = 45
                                    aT += 1
                                    astrds[0].update2()
                                    if astrds[0].a != astT:
                                        objcts[5][2] = True
                                        cloct = 0
                                    if aT >= 45:
                                        txt = 'Shoot the asteroid'
                                        txt2 = 'It will change directions'
                                    else:
                                        txt = 'This is a asteroid'
                                        txt2 = 'If it hits you, you will take damage'
                                    
                            else:
                                if htbl[0].dead:
                                        #objcts[4][2] = True
                                    if htbl[1].dead:
                                        if htbl[2].dead:
                                            objcts[4][2] = True
                                            astT = astrds[0].a
                                        else:
                                            htbl[2].draw()
                                            txt = "This is a 'Lazer' Baddie"
                                            txt2 = 'It has lazer that needs to charge up'
                                    else:
                                        htbl[1].draw()
                                        txt = "This is a 'Sprayer' Baddie"
                                        txt2 = 'He will fire shots rapidly with low accuracy'
                                else:
                                    htbl[0].draw()
                                    txt = "This is a 'Sharpshooter' Baddie"
                                    txt2 = 'He will fire shots slowly to hurt you'
                        else:
                            txt = 'Press space to fire a laser shot off'
                            txt2 = "Press 'f' to toggle auto-fire on and off"
                            if shF >= objcts[3][1]:
                                objcts[3][2] = True
                    else:
                        #sanic objective
                        txt = 'There is a maximum speed'
                        txt2 = 'Try and reach it'
                        if demo.s >= 17.5:
                            objcts[2][2] = True
                else:
                    #still on movement
                    if dst >= int(objcts[1][1]):
                        objcts[1][2] = True
                    elif dst >= int(objcts[1][1])/2:
                        #halfway there
                        txt = "Use the 'A' key to turn left"
                        txt2 = "Use the 'D' key to turn right"
                    else:
                        #Not halfway there
                        txt = "Use the 'W' key to increase your speed"
                        txt2 = "Use the 'S' key to reduce your speed"
            else:
                txt = 'You are the little triangle thing'
                txt2 = 'In the center of the screen'
            if firing:
                demo.fire()
            htb = tsF2.size(txt)
            htbs = tsF2.render(txt, 0,(0,0,255))
            screen.blit(htbs, [320-htb[0]/2,5,1000,1000])
            htb = tsF2.size(txt2)
            htbs = tsF2.render(txt2, 0,(0,0,255,))
            screen.blit(htbs, [320-htb[0]/2,605,1000,1000])
            demo.draw()
            dst += demo.s
            for i in st:
                    if i.ig:
                        st.remove(i)
                    else:
                        i.update2()
            fnum += 1
            if fnum > 60:
                fnum = 1
                if not roundEnd:
                    cloct += 1 
            ScreenUpdate(screen)
        location = 1
        

        

    if location == 8:
        #from main menu
        #the room with the 3 previous games and stuff
        #has its own loop
        ss = False
        #buttons
        #buns = [Thingy([320,320],['hello',0,0])]
        buns = []
        x = 80
        for i in lG:
            buns.append(Thingy([x,220],i))
            x += 160
        #kewl buttons, ik
        daBk = Button((15,15),1,'Back')
        daBk.imageUn = pygame.transform.scale(daBk.imageUn, (106,34))
        daBk.imageP = pygame.transform.scale(daBk.imageP, (106,34))
        daBk.r = pygame.rect.Rect([0,0],[108, 36])
        endCond = None
        while True:
            screen.fill((0,0,0))
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mp = pygame.mouse.get_pos()
                    #NEEDS TO GET BETTER!!
                    if daBk.r.collidepoint(mp[0],mp[1]):
                        click.play()
                        ss = True
                        endCond = None
                        break
                    for tab in buns:
                        if tab.r.collidepoint(mp[0],mp[1]):
                            tab.click()
                            while True:
                                new_splash = choice(splash)
                                #new_splash = 'Lore'
                                #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
                                if new_splash == 'Lore':
                                    perc = randint(1,100)
                                    if perc <= 50:
                                        new_splash = choice(lores)
                                        break
                                    else:
                                        new_splash = choice(splash)
                                else:
                                    break
                            ks = splsF.size(new_splash.replace('\n',''))
                            nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]
                            endCond = True
                            letters = tab.info[0]
                            abad = True
                            ss = True
                            break
                else:
                    break

            if ss:
                break
            #draw the selectable stuff
            for t in buns:
                t.draw()
            daBk.draw()
            #draw the text stuff
            tx = tsF.render('Space Enclave',0,(255,0,0))
            screen.blit(tx, (149,100,1000,1000))
            tx = tsF2.render('Recently Played',0,(255,0,0))
            sd = tsF2.size('Recently Played')
            screen.blit(tx, (320-sd[0]/2,155,1000,1000))
            txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
            screen.blit(txtx, (468,630,1000,1000))
            ScreenUpdate(screen)
        if endCond is None:
            location = 1
        elif endCond:
            location = 3
    if location == 9:
        #from the seed thing
        #will have its own loops so it fits in with the 'cool' functions 
        #has 4 random seeds and you can press a button to have it
        #make 4 new ones, and you can select any of them
        sTabs = []
        x = 80
        for i in ["'A'","'B'","'C'","'D'"]:
            sTabs.append(Thingy([x,220],makeSeed(),override=True,let=i))
            x += 120
        ss = False
        #buttons that aren't tablets
        daBk = Button((0,0),6,'Back')
        daBk.imageUn = pygame.transform.scale(daBk.imageUn, (106,34))
        daBk.imageP = pygame.transform.scale(daBk.imageP, (106,34))
        daBk.r = pygame.rect.Rect([0,0],[108,36])
        
        daBk2 = Button((400,15),1,'Main Menu')
        daBk2.imageUn = pygame.transform.scale(daBk2.imageUn, (106,34))
        daBk2.imageP = pygame.transform.scale(daBk2.imageP, (106,34))
        daBk2.r = pygame.rect.Rect([533,0],[108,36])

        ranB = Button((220,410),-2,'Randomize')
        
        while True:
            screen.fill((0,0,0))
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    msp = pygame.mouse.get_pos()
                    if daBk.r.collidepoint(msp[0],msp[1]):
                        #goes to menu
                        click.play()
                        location = 6
                        ss = True
                        break
                    elif daBk2.r.collidepoint(msp[0],msp[1]):
                        click.play()
                        location = 1
                        ss = True
                        break
                    elif ranB.r.collidepoint(msp[0],msp[1]):
                        #for the scramble button
                        click.play()
                        sTabs = []
                        x = 80
                        for i in ["'A'","'B'","'C'","'D'"]:
                            sTabs.append(Thingy([x,220],makeSeed(),override=True,let=i))
                            x += 120
                    else:
                        for i in sTabs:
                            if i.r.collidepoint(msp[0],msp[1]):
                                click.play()
                                while True:
                                    new_splash = choice(splash)
                                    #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
                                    if new_splash == 'Lore':
                                        perc = randint(1,100)
                                        if perc <= 50:
                                            new_splash = choice(lores)
                                            break
                                        else:
                                            pass
                                    else:
                                        break
                                ks = splsF.size(new_splash.replace('\n',''))
                                nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]

                                letters = i.info
                                ss = True
                                abad = True
                                location = 3
                                break
            if ss:
                break
            #tablets and buttons
            daBk.draw()
            daBk2.draw()
            ranB.draw()
            for i in sTabs:
                i.draw()
            #text
            tx = tsF.render('Space Enclave',0,(255,0,0))
            screen.blit(tx, (149,100,1000,1000))
            tx = tsF2.render('Random Seeds',0,(255,0,0))
            sd = tsF2.size('Random Seeds')
            screen.blit(tx, (320-sd[0]/2,155,1000,1000))
            #dev info
            txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
            screen.blit(txtx, (468,630,1000,1000))
            
            ScreenUpdate(screen)
            clock.tick(300)
        #location = 1
    
    if location == 6:
        #screen for a set seed
        #own loop because why not
        #letters = 'aaaaa'
        letters = makeSeed()
        current = 0
        pygame.key.set_repeat()
        butI = pygame.image.load('buton.png').convert()
        butI2 = pygame.image.load('buton2.png').convert()
        men = pygame.mixer.Sound('button.wav')
        click = pygame.mixer.Sound('click.wav')
        men.set_volume(.45)
        menT = pygame.mixer.Channel(5)
        daBk = Button((0,0),1,'Back')
        daBk.imageUn = pygame.transform.scale(daBk.imageUn, (106,34))
        daBk.imageP = pygame.transform.scale(daBk.imageP, (106,34))
        daBk.r = pygame.rect.Rect([0,0],[108,36])
        rdy = Button((220,330),3,'Start Game')
        ss = False
        #letters not allowed in the seed
        nots = '-1234567890,<.>/?;:!@#$%^&*()-_=+|\{[]}`~"' + "'"
        
        #'next' button
        daBk2 = Button((400,15),9,'Random Seeds')
        daBk2.imageUn = pygame.transform.scale(daBk2.imageUn, (126,34))
        daBk2.imageP = pygame.transform.scale(daBk2.imageP, (126,34))
        daBk2.r = pygame.rect.Rect([513,0],[108,36])
        while True:
            screen.fill((0,0,0))
            for i in sumSters:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    msp = pygame.mouse.get_pos()
                    if daBk.r.collidepoint(msp[0],msp[1]):
                        #goes to menu
                        click.play()
                        location = 1
                        ss = True
                        break
                    if daBk2.r.collidepoint(msp[0],msp[1]):
                        #goes to random seed thingy
                        click.play()
                        location = 9
                        ss = True
                        break
                    if rdy.r.collidepoint(msp[0],msp[1]):
                        #goes to loading screen
                        location = 3
                        click.play()
                        abad = True
                        while True:
                            new_splash = choice(splash)
                            #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
                            if new_splash == 'Lore':
                                perc = randint(1,100)
                                if perc <= 50:
                                    new_splash = choice(lores)
                                    break
                                else:
                                    pass
                            else:
                                break
                        ks = splsF.size(new_splash.replace('\n',''))
                        nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]
                        loaded = False
                        ss = True
                        break
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        current += 1
                        if current > 4:
                            current = 0
                    elif event.key == K_LEFT:
                        current -= 1
                        if current < 0:
                            current = 4
                    else:
                        prsd = pygame.key.name(event.key)
                        if len(prsd) == 1 and not prsd in nots:
                            letters = list(letters)
                            letters[current] = prsd
                            letters = str(letters).replace(',','').replace(']','').replace('[','').replace("'",'').replace(' ', '').strip()
                            current += 1
                            if current > 4:
                                current = 0
                            elif current < 0:
                                current = 4
                        elif prsd == 'backspace':
                            current -= 1
                            if current > 4:
                                current = 0
                            elif current < 0:
                                current = 4
                        elif prsd == 'space':
                            current += 1
                            if current > 4:
                                current = 0
                            elif current < 0:
                                current = 4
            if ss:
                break
            daBk.draw()
            daBk2.draw()
            rdy.draw()
            #highlight the current letter
            ds2 = tsF.size(letters)
            ste = tsF.size(letters[current:current+1])
            srs = tsF.size(letters[:current])
            '''testing'''
            #pygame.draw.rect(screen, (0,255,0), (319-ds2[0]/2+srs[0],249,ste[0]+1,ste[1]+1),0)
            pygame.draw.rect(screen, (0,255,0), (319-ds2[0]/2+srs[0],249,ste[0]+1,ste[1]+1),0)
            #draw current letter
            ent = tsF.render(letters,0,(255,0,0))
            screen.blit(ent, (320-ds2[0]/2,250,ds2[0],ds2[1]))
            #draw name and me
            tx = tsF.render('Space Enclave',0,(255,0,0))
            screen.blit(tx, (149,100,1000,1000))
            txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
            screen.blit(txtx, (468,630,1000,1000))
            ScreenUpdate(screen)
            clock.tick(300)
    if not loaded and location == 3:
        '''
        while True:
            new_splash = choice(splash)
            #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
            if new_splash == 'Lore':
                perc = randint(1,100)
                if perc <= 50:
                    new_splash = choice(lores)
                    break
                else:
                    pass
            else:
                break
            '''
        new_splash = choice(splash)
        if new_splash == 'Lore':
            new_splash = choice(lores)
        loaded = True
        if not abad:
            seed = makeSeed()
        if letters.lower() == 'lrpls':
            #uh oh, you have discovered the secret of the game
            #do secret magic :)
            #decripts a file that was previously unreadable
            fils = open('9-4-3053.ctl','r')
            cont2 = fils.readlines()
            cont = ''
            for i in cont2:
                cont += i
            #print cont
            fils.close()
            #print cont.find('\n')
            cont = cont.replace('\\n','#$')
            #print cont.find('#$')
            #print cont + '\n\n\n\n'
            cont = encript(cont)
            #print cont
            cont = cont.replace('#$','\n')
            #print '\n\n\n'
            #print cont
            #'''
            fils = open('9-4-3053.ctl','w')
            fils.write(cont)
            fils.close()
            #'''
            new_splash = "Look for a file named '9-4-3053.ctl'"
        ks = splsF.size(new_splash.replace('\n',''))
        nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]
    if loaded and location == 3:
        
        loaded = True
        #loading screen
        #what needs to be loaded
        #splash text
        #seed, and intrept it
        #'the baddies' 
        screen.fill((0,0,0))
        for i in sumSters:
            pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
        screen.blit(nedSp[0],nedSp[1])
        pygame.key.set_repeat(10,10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        #big large clunky thing for parts of the loading process
        if stage == 0:
            fils = open('stats.rsc','w')
            for i in stats:
                fils.write(str(i)+'\n')
            fils.write(str(max_fps))
            fils.close()
            player = Player()
            stage += 1
        elif stage == 1 and not abad:
            #seed = makeSeed()
            stage += 1
            highs = open('hs.rsc','r')
            #resets the scoreboard
            #format is dificulty|score
            #so .375|2750.3 could be a score
            highSc2 = []
            while True:
                kes = highs.readline()
                if kes.strip() == '':
                    break
                else:
                    highSc2.append(str(kes).replace('\n',''))
            highs.close()
            highSc = []
            for i in highSc2:
                po = i.split('|')
                highSc.append(po)
        elif stage == 1 and abad:
            seed = letters
            stage += 1
        elif 2 <= stage < 9:
            if not stage >= 7:
                infos = intSeed(stage-2,infos,seed[:])
            stage += 1
        else:
            try:
                tPs = infos[stage-9]
                if tPs[0] == 'bad':
                    if tPs[1] is None:
                        dif += 1.5
                    elif tPs[1] == False:
                        dif += 2
                    else:
                        dif += 4
                    htbl.append(Bad(pos=tPs[2],ai=tPs[1]))
                else:
                    astrds.append(Asteroid(tPs[2],tPs[1],stage))
                    #make it more random
                    ops = tPs[2]
                    cnt = [320,320]
                    dx = ops[0] - cnt[0]
                    dy = ops[1] - cnt[1]
                    tos = sqrt(dx**2+dy**2)
                    if tos >= 400:
                        dif += 1.5
                    #elif tos >= 300:
                        #dif += 1.825
                    elif tos >= 250:
                        dif += 2
                    elif tos >= 75:
                        dif += 2.25
                    else:
                        dif += 2.75
                    #dif += 2
            except IndexError:
                loaded = True
                location = 4
                dif -= 9
            stage += 1
        if stage >= 20:
            stage = 20
        #text
        txtx = fpsf.render('The Grand Annihilator, 2015-2016', 0, (255,0,0))
        screen.blit(txtx, (468,630,1000,1000))
        tx = tsF.render('Space Enclave',0,(255,0,0))
        screen.blit(tx, (149,100,1000,1000))
        #progress bar
        pygame.draw.rect(screen, (0,255,0), (145,305,350,25),2)
        pygame.draw.rect(screen, (0,255,0), (145,305,
                             int(350 * (stage/20.0)),25),0)

        #loaded = True
        #location = 4
        
        ScreenUpdate(screen)
        clock.tick(20)
        #will have load loading screen, random splash text and progress bar
        
    if loaded and location == 4:
        #main game, with the bad guys positions along with any other stuff already loaded
        '''disabled so i can listen to music'''
        #maint.play(mainT, loops=-1)
        firing = False
        start = datetime.now()
        start = [start.minute,start.second,start.microsecond]
        #print new_splash
        #create the 'stars'
        roundEnd = False
        endT = 'You Win!'
        endF = 0
        endFm = 180
        cloct = 0
        hsT = ''
        abad = False
        upsD = False
        #htbl = [Bad()]
        #astrds = [Asteroid((60,500),90,'dfdfd')]
        'new splash text thingy'''
        while True:
            new_splash = choice(splash)
            #if new_splash == 'The pilot of your ship is named Greg, please respect him.':
            if new_splash == 'Lore':
                perc = randint(1,100)
                if perc <= 50:
                    new_splash = choice(lores)
                    break
                else:
                    pass
            else:
                break
        if new_splash == 'Lore':
            new_splash = choice(lores)
        ks = splsF.size(new_splash.replace('\n',''))
        nedSp = [splsF.render(new_splash.replace('\n',''),0,(0,0,255)),[320-ks[0]/2,250,ks[0],ks[1]]]
        paused = False
        stop = False
        paPr = False

        while True:
            screen.fill((0,0,0))
            for i in stars:
                pygame.draw.rect(screen, (255,255,255), [i[0],i[1],2,2])
            if not cfr:
                #if fdm+8 > fd and player.pl:
                    #fd += 1
                if fdm > fd and player.pl:
                    fd += 1
                elif fdm > fd and not player.pl:
                    fd += 1
                    player.fl = True
                else:
                    fd = 0
                    cfr = True
                
            #for event in pygame.event.get():
            g = pygame.event.get()
            if fnum == 60:
                pass
                #print g
            for event in g:
                if event.type == QUIT:
                    pygame.quit()
                    #print lowest
                    exit()
                if event.type == KEYDOWN:
                    '''
                    #experimental!!!
                    if event.key == K_w:
                        player.s += .125
                        eng.stop()
                        eng.play(eng2)
                        for i in g:
                            if i.key == K_SPACE:
            
                                player.fire()
                                break
                    if event.key == K_d or event.key == K_RIGHT:
                        player.rotate(-2.5)
                        for i in g:
                            if i.type == KEYDOWN:
                                if i.key == K_SPACE:
                                    print 'my victory is at hand'
                                    player.fire()
                                    break
                    ''''''
                    if event.key == K_n:
                        player.s += .125
                        eng.stop()
                        eng.play(eng2)
                        player.fire()
                    if event.key == K_m:
                        player.s -= .08
                        eng.stop()
                        eng.play(eng2)
                        player.fire()
                    '''
                    if event.key == K_ESCAPE and not paPr or event.key == K_p and not paPr:
                        paPr = True
                        if paused:
                            paused = False
                        else:
                            paused = True
                    if not paused:# or paused:
                        if event.key == K_f and not upsD:
                            upsD = True
                            if not firing:
                                firing = True
                            else:
                                firing = False
                        if event.key == K_w or event.key == K_UP:
                            #player.s = 1 + float(player.s/10.0)
                            player.s += .125
                            eng.stop()
                            eng.play(eng2)
                            player.total = [player.s * float((cos(radians(player.ad)))),player.s * float((sin(radians(player.ad))))]
                        elif event.key == K_s or event.key == K_DOWN:
                            player.s -= .08
                            if player.s < 0:
                                player.s = 0
                            player.total = [player.s * float((cos(radians(player.ad)))),player.s * float((sin(radians(player.ad))))]
                            #player.s = (player.s/10.0) - 1
                        if event.key == K_d or event.key == K_RIGHT:
                            #player.a -= 5
                            #player.rotate(-1.25)
                            player.rotate(-2.5)
                            #player.fire()
                        if event.key == K_a or event.key == K_LEFT:
                            #player.a += 5
                            #player.rotate(1.25)
                            player.rotate(2.5)
                            #player.fire()
                        if event.key == K_SPACE:
                            player.fire()
                        if event.key == K_COMMA:
                            player.rotate(1.25)
                        if event.key == K_PERIOD:
                            player.rotate(-1.25)

                    if event.key == K_k:
                        pass
                        #print player.frm
                        #print (htbl[0].h/50.0)
                        #player.health = 0
                        #print htbl[0].sd
                        #print player.ad
                        #print htbl[0].bps
                        #print astrds[0].pos
                        #print event
                        #for ik in g:
                            #print pygame.event.event_name(ik.type)
                        #print player.health, '/', player.max
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        unp[0] = False
                    if event.key == K_f:
                        upsD = False
                    if event.key == K_ESCAPE or event.key == K_p:
                        paPr = False
                    #"""
                if event.type == MOUSEBUTTONDOWN and paused:
                    re2 = tsF2.size('Resume Game')
                    pt2 = pygame.mouse.get_pos()
                    hitPt = pygame.rect.Rect(320-re2[0]/2,270-re2[1]/2,re2[0],re2[1]).collidepoint(pt2[0],pt2[1])
                    if hitPt:
                        click.play()
                        paused = False
                    re2 = tsF2.size('Quit Game')
                    hitPt = pygame.rect.Rect(320-re2[0]/2,370-re2[1]/2,re2[0],re2[1]).collidepoint(pt2[0],pt2[1])
                    if hitPt:
                        click.play()
                        stop = True
                        loaded = False
                        stage = 0
                        infos = []
                        htbl = []
                        astrds = []
                        dif = 0
            if stop:
                location = 1
                break
            if not roundEnd and not paused:
                player.draw()
                for i in st:
                    if i.ig:
                        st.remove(i)
                    else:
                        i.update2()
                    #htbl[0].draw()
                for i in htbl:
                    #pass
                    if i.h <= 0:
                        #shots fired, baddies hit, asteroids hit, baddies killed, deaths
                        #wins, time spent playing (in levels)
                        stats[3] += 1
                        htbl.remove(i)
                    else:
                        #pass
                        i.draw()
                for i in astrds:
                    i.update()
            else:
                screen.blit(player.i,player.r)
                player.hpBar.update()
                for i in astrds:
                    screen.blit(i.image,i.r)
                for i in htbl:
                    screen.blit(i.i,i.r)
            if firing and not roundEnd:
                player.fire()
            #make the clock
            #nowt = str(60-int(dud[1]-start[1]))
            nowt = 60-cloct
            d2 = tF.render(str(nowt),0,(255,0,0))
            ds2 = tF.size(str(nowt))

            #for debugging *laughs*
            #player.health += 5

            '''#passive regen
            player.health += .05
            if player.health > player.max:
                player.health = player.max
            '''
            
            fp = fpsf.render('FPS:'+str(int(clock.get_fps())),0,(255,0,0))
            ifi = fpsf.render('DIF:'+str(round(float(dif)/maxD,3)),0,(255,0,0))
            t2d = fpsf.render('SEED:'+str(seed.lower()),0,(255,0,0))
            if  20 < int(clock.get_fps()) <= lowest:
                lowest = int(clock.get_fps())
            screen.blit(fp, [575,10,1000,1000])
            screen.blit(ifi, [575,20,1000,1000])
            screen.blit(t2d, [575,30,1000,1000])
            screen.blit(d2, (320-ds2[0]/2,10,ds2[0],ds2[1]))
            #ScreenUpdate(screen)
            #clock.tick(60)
            if not paused:
                #passive regen
                player.health += .05
                if player.health > player.max:
                    player.health = player.max
                fnum += 1
                if fnum > 60:
                    fnum = 1
                    if not roundEnd:
                        cloct += 1 
                    shuffle(astrds)
                '''
                tst = 0
                for i in st:
                    if not i.t and not i.t is None:
                        tst += 1
                print tst
                '''
            else:
                #draw the options :)
                re2 = tsF2.size('Resume Game')
                pt2 = pygame.mouse.get_pos()
                hitPt = pygame.rect.Rect(320-re2[0]/2,270-re2[1]/2,re2[0],re2[1]).collidepoint(pt2[0],pt2[1])
                if hitPt:
                    resM = tsF2.render('Resume Game',0,(255,125,0))
                else:
                    resM = tsF2.render('Resume Game',0,(255,125,50))
                screen.blit(resM,(320-re2[0]/2,270-re2[1]/2,1000,1000))
                re2 = tsF2.size('Quit Game')
                hitPt = pygame.rect.Rect(320-re2[0]/2,370-re2[1]/2,re2[0],re2[1]).collidepoint(pt2[0],pt2[1])
                if hitPt:
                    resM = tsF2.render('Quit Game',0,(255,125,0))
                else:
                    resM = tsF2.render('Quit Game',0,(255,125,50))
                screen.blit(resM,(320-re2[0]/2,370-re2[1]/2,1000,1000))
            #ending the round conditions
            if player.health <= 0 or cloct >= 60:
                if endF >= endFm:
                    stats[4] += 1
                    stats[6] += cloct
                    #player is 'd-e-d' or went over their time
                    location = 1
                    maint.stop()
                    loaded = False
                    stage = 0
                    infos = []
                    htbl = []
                    astrds = []
                    dif = 0
                    #print (dif/maxD)*(60-cloct)*player.health
                    fils = open('stats.rsc','w')
                    for i in stats:
                        fils.write(str(i)+'\n')
                    fils.write(str(max_fps))
                    fils.close()
                    break
                elif not roundEnd:
                    roundEnd = True
                    endT = 'You Lost'
                    hst2 = ''
                    
            if htbl == [] and cloct < 60 and not roundEnd:
                #player won
                stats[5] += 1
                stats[7] += int((((dif+.01)/maxD))*(60-cloct)*player.health)
                roundEnd = True
                endT = 'You Won with a Score of %s' % str(int((((dif+.01)/maxD))*(60-cloct)*player.health))
                score = [str(int((((dif+.01)/maxD))*(60-cloct)*player.health)),float(dif/maxD)]
                dis = round(score[1],1)
                #print 'new', score[0]
                btsdis = highSc[int(dis*10.0)][1]
                #print 'old', btsdis
                #print score[0] +'>='+btsdis
                #print score[0] >= btsdis
                if int(score[0]) >= int(btsdis):
                    #print score[0], '/', btsdis
                    #print 'u beat the high corp'
                    highSc[int(dis*10.0)][1] = score[0]
                    hsT = "You beat the previous high score by %s points!"% str(int(score[0])-int(btsdis))
                    hst2 = ''
                else:
                    hsT = "You didn't get a new high score"
                    hst2 = 'The high score is currently %s points' %str(btsdis)
                k = open('hs.rsc','w')
                for i in highSc:
                    k.write(str(i[0])+"|"+str(i[1])+'\n')
                k.close()
            if endF >= endFm:
                if roundEnd:
                    #player is won and the time is up
                    location = 1
                    score = [str(int((((dif+.01)/maxD))*(60-cloct)*player.health)),float(dif/maxD)]
                    maint.stop()
                    loaded = False
                    stage = 0
                    infos = []
                    htbl = []
                    astrds = []
                    #print (dif/maxD)*(60-cloct)*player.health
                    #print score[0]
                    #write to scores page
                    #check if it beats any

                    #save to the last games file thing
                    lG.remove(lG[0])
                    lG.append([str(seed),str(round(float(dif/maxD),3)),str(score[0])])
                    fils = open('prvs.rsc','w')
                    a = '%s|%s|%s'%(str(seed),str(round(float(dif/maxD),3)),str(score[0]))
                    for i in lG:
                        fils.write('%s|%s|%s\n'%(str(i[0]),str(i[1]),str(i[2])))
                    fils.close()
                    dif = 0
                    #shots fired, baddies hit, asteroids hit, baddies killed, deaths
                    #wins, time spent playing (in levels)
                    stats[6] += cloct
                    fils = open('stats.rsc','w')
                    for i in stats:
                        fils.write(str(i)+'\n')
                    fils.write(str(max_fps))
                    fils.close()
                    break
            if roundEnd:
                #draw the text and stuff
                #text
                ent = butT.render(endT,0,(255,0,0))
                ds2 = butT.size(endT)
                screen.blit(ent, (320-ds2[0]/2,150,ds2[0],ds2[1]))
                ent = tF.render(hsT,0,(255,0,0))
                ds2 = tF.size(hsT)
                screen.blit(ent, (320-ds2[0]/2,250,ds2[0],ds2[1]))
                ent = tF.render(hst2,0,(255,0,0))
                ds2 = tF.size(hst2)
                screen.blit(ent, (320-ds2[0]/2,200,ds2[0],ds2[1]))
                endF += 1
            #pygame.draw.rect(screen,(0,255,0),[0,0,(640*(fd/float(fdm))),20],0)
            pygame.draw.rect(screen,(0,255,0),[0,618,644,22],2)
            pygame.draw.rect(screen,(0,255,0),[0,620,(640*(player.health/float(player.max))),20])
            ScreenUpdate(screen)
            clock.tick(300)

                
