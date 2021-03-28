from os import path
from pygame.locals import *
from sys import argv
from misc import *
from Button import Button
from SeedMethods import *
from Asteroid import Asteroid
from ShooterGuy import Sprayer
from LaserGuy import Laser
from Projectile import Bullet
from Player import Player
from Tablet import Tablet
from SmallButton import SmallButton
from SeedTablet import SeedTablet
from math import sin, cos, radians, degrees
import datetime
import sys
projectName = "Geometry in Space"


def getDifficulty(seed):
    gameSeed = intSeed(seed)
    currentDifficulty = 0
    for letter in gameSeed:
        if letter[0] == 'bad':
            if letter[1] is None:  # Standard shooter enemy
                currentDifficulty += 1.5
            elif not letter[1]:  # Sprayer, faster ROF but less accuracy and bullet speed
                currentDifficulty += 2
            else:  # Laser enemy
                currentDifficulty += 4
        else:
            # make it more random
            ops = letter[2]
            cnt = [320, 320]
            dx = ops[0] - cnt[0]
            dy = ops[1] - cnt[1]
            tos = sqrt(dx ** 2 + dy ** 2)
            if tos >= 400:
                currentDifficulty += 1.5
            elif tos >= 250:
                currentDifficulty += 2
            elif tos >= 75:
                currentDifficulty += 2.25
            else:
                currentDifficulty += 2.75
    return currentDifficulty


def formatPlayerBullet(playerPosition, playerAngle, mouseButtonDown):
    if not mouseButtonDown:
        playerAngle += 180
    x = playerPosition[0] + 20.0*float(cos(radians(playerAngle)))
    y = playerPosition[1] - 20.0*float(sin(radians(playerAngle)))
    argument = [x, y, playerPosition[0], playerPosition[1]]
    return Bullet(argument, True, 13)


def updateFPSCounter(text, pos=[640, 0]):
    framesRender = framesPerSecondFont.render(text, 1, (255, 0, 0))
    framesRect = framesPerSecondFont.size(text)
    desiredCenter = pos
    desiredCenter = [desiredCenter[0] - (framesRect[0]),
                     desiredCenter[1], framesRect[0], framesRect[1]]
    return [framesRender, desiredCenter]


def update(currentHP, maxHP, rectToCopyFrom):
    newRect = rectToCopyFrom.copy()
    percentage = float((float(currentHP) / float(maxHP)))
    pygame.draw.rect(screen, (0, 255, 0), (newRect[0] - 1, newRect[1] - 5, newRect[2] + 2, 3), 1)
    pygame.draw.rect(screen, (0, 255, 0), (newRect[0] - 1, newRect[1] - 5, newRect[2] * percentage + 1, 2), 0)

if __name__ == "__main__":
    filePath = path.dirname(argv[0])
    windowSize = [640, 640]
    centeredXValue = windowSize[0] / 2
    centeredYValue = windowSize[1] / 2

    """General Pygame Setup"""
    screen = pygame.display.set_mode(windowSize)
    icons = pygame.image.load(filePath+'/resources/images/icon.png')
    pygame.key.set_repeat()
    pygame.display.set_icon(icons)
    pygame.display.set_caption(projectName, projectName)

    """Creates something to look at if being played on a Potato"""
    listOfBackgroundStars = createListOfStars()
    screen.fill((0, 0, 0))
    drawRectanglesFromList(listOfBackgroundStars, screen)

    """Font Setup"""
    pygame.font.init()
    framesPerSecondFont = pygame.font.Font(None, 16)
    loadingScreenFont = pygame.font.Font(None, 23)
    largeTitleScreenFont = pygame.font.SysFont('krungthep', 45)
    smallTitleScreenFont = pygame.font.SysFont('krungthep', 27)
    extraScreenFont = pygame.font.SysFont('krungthep', 35)

    """
    Variables for Controlling Game Elements
    Location is on a scale from 0-5
    0 - Main Menu
    1 - Seed Enter Room
    2 - Loading Screen Into Match
    3 - Actual Game, Once Loaded
    4 - Recent Seeds with Score
    5 - Random Seed Selection
    6 - Post Game Screen
    """
    location = 0
    gameSeed = ""
    gameSeedString = gameSeed[:]
    maxDifficulty = 29.25
    clock = pygame.time.Clock()
    player = None

    """Audio Loading"""
    pygame.mixer.init()
    explosionSound = pygame.mixer.Sound(filePath+"/resources/audio/explosion.wav")
    laserSound = pygame.mixer.Sound(filePath+"/resources/audio/fireLaser.wav")
    enemyLaserSound = pygame.mixer.Sound(filePath+"/resources/audio/fireLaser.wav")
    enemyHitSound = pygame.mixer.Sound(filePath+"/resources/audio/enemyHit.wav")
    clickSound = pygame.mixer.Sound(filePath+"/resources/audio/click.wav")
    asteroidHitSound = pygame.mixer.Sound(filePath+"/resources/audio/asteroidCollision.wav")
    baseVolume = .5

    explosionSound.set_volume(baseVolume + .35)
    laserSound.set_volume(baseVolume + .35)
    enemyLaserSound.set_volume(baseVolume + .15)
    enemyHitSound.set_volume(baseVolume + .20)
    clickSound.set_volume(.1)
    asteroidHitSound.set_volume(baseVolume + .20)

    playerSoundChannel = pygame.mixer.Channel(0)  # Player Sound Channel
    enemySoundChannel = pygame.mixer.Channel(1)  # Enemy Sound Channel

    """Establishment of Text Things That I Don't Care About"""
    selfCongratulatoryCredit = framesPerSecondFont.render('TheGrand547 2015-2016, 2018', 1, (255, 0, 0))
    selfCongratulatoryCreditLocation = getCoordinatesForCenteredTextBottomRight(
        framesPerSecondFont.size('TheGrand547 2015-2016, 2018'), [640, 640])
    mainTitleText = largeTitleScreenFont.render(projectName, 1, (255, 0, 0))
    mainTitleLocation = getCoordinatesToCenterTextMiddle(largeTitleScreenFont.size(projectName),
                                                         [windowSize[0]/2, 80])
    recentGamesText = extraScreenFont.render("Recent Games", 1, (255, 0, 0))
    randomSeedText = extraScreenFont.render("Random Seeds", 1, (255, 0, 0))
    pausedText = largeTitleScreenFont.render("--- Paused ---", 1, (255, 0, 0))

    try:
        highScoreFile = open(filePath+"/resources/text/highscore.txt", 'r')
        highScore = highScoreFile.readline().replace("\n", "").split("|")
        highScoreFile.close()
    except:
        highScore = ["0", "aaaaa"]

    pausedRect = getCoordinatesToCenterTextMiddle(largeTitleScreenFont.size("--- Paused ---"), [320, 320])
    recentGamesLocation = getCoordinatesToCenterTextMiddle(extraScreenFont.size("Recent Games"), [windowSize[0]/2, 170])
    listOfMenuButtons = [Button([320, 170], 2, "Play Game"), Button([320, 250], 1, "Set Game Seed"),
                         Button([320, 330], 4, "Recent Games"), Button([320, 410], 5, "Random Seeds"),
                         Button([320, 490], -1, "Exit")]
    listOfTablets = []
    listOfCurrentButtons = []

    listOfEnemies = []
    listOfAsteroids = []
    listOfBullets = []
    currentDifficulty = 0
    notPaused = True
    mouseButtonDown = False
    pressedLast = False
    pressedThis = False
    tabletsLoaded = False
    letters = ""
    currentIndex = 0
    lettersNotAllowed = '-1234567890,<.>/?;:!@#$%^&*()-_=+|\{[]}`~"' + "'"
    timeWhenPauseStarted = datetime.datetime.now()
    maxGameTime = 60 - 1  # 60 seconds but this way makes it a bit easier on my end cause i'm lazy af

    gameStartTime = datetime.datetime(2019, 2, 2, 2)
    timeOffset = datetime.timedelta()
    currentTime = datetime.timedelta()

    """
    Things for the end of each game
    """
    endOfGameMessages = []
    endOfGameButtons = [Button([320, 470], 1, "Play Again?"), Button([320, 550], -1, "Main Menu")]
    alreadyTakenScreenShot = False
    takeScreenShotNOW = False
    endGameLoaded = False
    endOfGameInfo = []

    """Main Game Loop"""
    while True:
        if location == 0:  # Main Menu
            endGameLoaded = False
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    #pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    for button in listOfMenuButtons:
                        if button.testMouseCollision() != 0:
                            location = button.testMouseCollision()
                            clickSound.play()
            drawRectanglesFromList(listOfBackgroundStars, screen)
            screen.blit(selfCongratulatoryCredit, selfCongratulatoryCreditLocation)
            for button in listOfMenuButtons:
                screen.blit(button.draw(), button.collisionArea)
            screen.blit(mainTitleText, mainTitleLocation)
            frameCounterThing = updateFPSCounter("FPS:"+str(int(clock.get_fps())))
            screen.blit(frameCounterThing[0], frameCounterThing[1])

            pygame.display.flip()
            clock.tick(60)
        elif location == 1:  # Seed Enter Room
            if letters == "":
                letters = generateSeed()
                currentIndex = 0
                listOfCurrentButtons = [Button([320, 380], 2, "Play"), SmallButton([0, 0], 0, "Back")]
            else:
                screen.fill((0, 0, 0))
                drawRectanglesFromList(listOfBackgroundStars, screen)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        for button in listOfCurrentButtons:
                            if button.collisionArea.collidepoint(pygame.mouse.get_pos()):
                                location = button.value
                                gameSeed = letters
                                letters = ""
                                clickSound.play()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            location = 0
                        elif event.key == K_RETURN:
                            location = 2
                            gameSeed = letters
                            letters = ""
                            clickSound.play()
                        elif event.key == K_LEFT:
                            currentIndex -= 1
                        elif event.key == K_RIGHT:
                            currentIndex += 1
                        else:
                            properKeyName = pygame.key.name(event.key)
                            if len(properKeyName) <= 1 and properKeyName not in lettersNotAllowed:
                                letters = list(letters)
                                letters[currentIndex] = properKeyName
                                letters = ''.join(letters)
                                currentIndex += 1
                            elif properKeyName == "backspace":
                                currentIndex += 1
                            elif properKeyName == "space":
                                currentIndex -= 1
                        if currentIndex > 4:
                            currentIndex = 0
                        elif currentIndex < 0:
                            currentIndex = 4

                screen.blit(selfCongratulatoryCredit, selfCongratulatoryCreditLocation)
                for button in listOfCurrentButtons:
                    screen.blit(button.draw(), button.collisionArea)

                ds2 = largeTitleScreenFont.size(letters)
                ste = largeTitleScreenFont.size(letters[currentIndex:currentIndex + 1])
                srs = largeTitleScreenFont.size(letters[:currentIndex])
                '''testing'''
                pygame.draw.rect(screen, (0, 255, 0), (320 - ds2[0] / 2 + srs[0], 249, ste[0] + 1, ste[1] + 1), 0)
                # draw current letter
                ent = largeTitleScreenFont.render(letters, 0, (255, 0, 0))
                screen.blit(ent, (320 - ds2[0] / 2, 250, ds2[0], ds2[1]))

                screen.blit(mainTitleText, mainTitleLocation)
                frameCounterThing = updateFPSCounter("FPS:" + str(int(clock.get_fps())))
                screen.blit(frameCounterThing[0], frameCounterThing[1])

                pygame.display.flip()
                clock.tick(60)

                if location != 1:
                    listOfCurrentButtons = []
        elif location == 2:  # Loading Screen Into Game
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            if gameSeed == "":
                gameSeed = generateSeed()
            gameSeedString = gameSeed[:]
            gameSeed = intSeed(gameSeed)
            currentDifficulty = 0
            listOfEnemies = []
            listOfAsteroids = []
            for letter in gameSeed:
                if letter[0] == 'bad':
                    if letter[1] is None:  # Standard shooter enemy
                        listOfEnemies.append(Sprayer(letter[2]))
                        currentDifficulty += 1.5
                    elif not letter[1]:  # Sprayer, faster ROF but less accuracy and bullet speed
                        listOfEnemies.append(Sprayer(letter[2], offset=5, rateOfFire=60, bulletSpeed=5.0))
                        currentDifficulty += 2
                    else:   # Laser enemy
                        listOfEnemies.append(Laser(letter[2]))
                        currentDifficulty += 4
                else:
                    listOfAsteroids.append(Asteroid(letter[2], letter[1]))
                    # make it more random
                    ops = letter[2]
                    cnt = [320, 320]
                    dx = ops[0] - cnt[0]
                    dy = ops[1] - cnt[1]
                    tos = sqrt(dx ** 2 + dy ** 2)
                    if tos >= 400:
                        currentDifficulty += 1.5
                    elif tos >= 250:
                        currentDifficulty += 2
                    elif tos >= 75:
                        currentDifficulty += 2.25
                    else:
                        currentDifficulty += 2.75
            location = 3
            player = Player((centeredXValue, centeredYValue))
            notPaused = True
            gameStartTime = datetime.datetime.now()
        elif location == 3:  # Game
            screen.fill((0, 0, 0))
            drawRectanglesFromList(listOfBackgroundStars, screen)
            playerCenter = [player.rectangle.center[0], player.rectangle.center[1]]
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if notPaused:  # Run when it becomes paused
                            timeWhenPauseStarted = datetime.datetime.now()
                        else:  # Run when it becomes unpaused
                            timeOffset += datetime.datetime.now() - timeWhenPauseStarted
                        notPaused = toggle(notPaused)
            keysThatArePressed = pygame.key.get_pressed()
            if keysThatArePressed[K_w] or keysThatArePressed[K_UP]:
                playerCenter[0] -= player.xComp(player.speed)
                playerCenter[1] += player.yComp(player.speed)
            elif keysThatArePressed[K_s] or keysThatArePressed[K_DOWN]:
                playerCenter[1] += player.xComp(player.speed)
                playerCenter[0] -= player.yComp(player.speed)
            if keysThatArePressed[K_a] or keysThatArePressed[K_LEFT]:
                playerCenter[1] += player.xComp(player.speed)
                playerCenter[0] += player.yComp(player.speed)
            elif keysThatArePressed[K_d] or keysThatArePressed[K_RIGHT]:
                playerCenter[1] -= player.xComp(player.speed)
                playerCenter[0] -= player.yComp(player.speed)
            """
            Update Order: Player, Enemies, Asteroids, Bullets
            """
            toDrawThePlayer = player.update(notPaused, playerCenter)
            playerPosition = playerCenter
            playerRect = player.rectangle
            playerHitBox = player.hitBox
            screen.blit(toDrawThePlayer[0], toDrawThePlayer[1])
            if toDrawThePlayer[2]:
                #  Player must fire this frame
                listOfBullets.append(formatPlayerBullet(playerPosition, player.getAngle(), mouseButtonDown))
            for individualEnemy in listOfEnemies:
                result = individualEnemy.update(playerPosition, notPaused)
                if result:  # Enemy isn't dead
                    screen.blit(result[0][0], result[0][1])
                    if result[2]:  # Means to shoot
                        listOfBullets.append(Bullet(result[2][0], result[2][2], bulletSpeed=result[2][1]))
                    elif result[2] is None and result[1] > 0:  # Means laser enemy hit the player
                        player.currentHealth -= result[1]
                    elif result[2] is None:
                        if result[4]:
                            pygame.draw.aaline(screen, result[3], playerPosition, individualEnemy.rectangle.center, 2)
                    update(individualEnemy.currentHealth, individualEnemy.maxHealth, individualEnemy.rectangle)
                else:
                    listOfEnemies.remove(individualEnemy)

            for individualAsteroid in listOfAsteroids:
                result = individualAsteroid.draw(notPaused, listOfEnemies, playerPosition,
                                                 listOfAsteroids, playerHitBox)
                screen.blit(result[0], result[1])
                player.currentHealth -= result[2]

            for bullet in listOfBullets:
                result = bullet.update(playerRect, playerHitBox, listOfEnemies, listOfAsteroids, notPaused)
                if result:
                    screen.blit(result[0], result[1])
                    if result[2] > 0:  # Player was hit
                        enemySoundChannel.play(enemyHitSound)
                        player.currentHealth -= result[2]
                    if result[2] < 0:  # Enemy Hit
                        enemySoundChannel.play(enemyHitSound)
                else:
                    listOfBullets.remove(bullet)

            update(player.currentHealth, player.maxHealth, player.rectangle)
            """
            Adding the FPS, seed and difficulty to the top right of the screen
            """
            difficultyRender = framesPerSecondFont.render('DIF:' + str(round(float(currentDifficulty) /
                                                                             maxDifficulty, 3)), 1, (255, 0, 0))
            seedRender = framesPerSecondFont.render('SEED:' + str(gameSeedString.lower()), 1, (255, 0, 0))
            frameCounterThing = updateFPSCounter("FPS:"+str(int(clock.get_fps())))
            screen.blit(frameCounterThing[0], frameCounterThing[1])
            difficultyThing = updateFPSCounter('DIF:' + str(round(float(currentDifficulty) /
                                                                  maxDifficulty, 3)),
                                               [640, frameCounterThing[1][3]])
            screen.blit(difficultyRender, difficultyThing[1])
            seedThing = updateFPSCounter('SEED:' + str(gameSeedString.lower()), [640, difficultyThing[1][3]
                                                                                 + difficultyThing[1][1]])
            screen.blit(seedRender, seedThing[1])
            currentTime = datetime.datetime.now()
            if not notPaused:
                # If its paused
                screen.blit(pausedText, pausedRect)
                timeSpent = (timeWhenPauseStarted - gameStartTime - timeOffset)
                timeString = str(maxGameTime - timeSpent.seconds) + "{0:.2f}".format(
                    1 - (timeSpent.microseconds /
                         1000000.0)).lstrip("10")
            else:
                # If it isn't paused
                timeSpent = (currentTime - gameStartTime - timeOffset)
                timeString = str(maxGameTime - timeSpent.seconds) + "{0:.2f}".format(
                    1 - (timeSpent.microseconds /
                         1000000.0)).lstrip("10")

                if player.currentHealth <= 0 or timeSpent.seconds > maxGameTime:
                    # If the played died or ran out of time
                    endOfGameMessages = ["Stage: " + gameSeedString.upper(), "Difficulty: " +
                                         str(round(float(currentDifficulty) / maxDifficulty, 3)),
                                         "Mission Failed", "Better Luck Next Time"]
                    endOfGameInfo = [gameSeedString, str(currentDifficulty/maxDifficulty), "Loss"]
                    location = 6
                if not listOfEnemies:
                    # All enemies have died, therefore the player has won
                    totalTimeForPointsCalculation = float(timeString)
                    scoreForThisRun = totalTimeForPointsCalculation * currentDifficulty * player.currentHealth
                    endOfGameMessages = ["Stage: " + gameSeedString.upper(), "Difficulty: " +
                                         str(round(float(currentDifficulty) / maxDifficulty, 3)),
                                         "HP to Points: " + str(player.currentHealth),
                                         "Time Multiplier: " + str(totalTimeForPointsCalculation),
                                         "Total Points: " + "{:,}".format(int(scoreForThisRun))]
                    endOfGameInfo = [gameSeedString, str(currentDifficulty / maxDifficulty),
                                     "{:,}".format(int(scoreForThisRun))]
                    if scoreForThisRun > int(highScore[0].replace(",", "")):
                        endOfGameMessages.append("NEW HIGH SCORE!!!")
                    else:
                        endOfGameMessages.append("You failed to achieve a high score")
                    location = 6
            currentTimeText = extraScreenFont.render(timeString, 1, (255, 0, 0))
            currentTimeRect = getCoordinatesToCenterTextMiddle(extraScreenFont.size(timeString), [320, 26])
            screen.blit(currentTimeText, currentTimeRect)

            pygame.display.flip()
            clock.tick(60)
        elif location == 4:  # Recent Games
            if not listOfTablets:
                lastFewGames = readFromFile(filePath + "/resources/text/previousGames.rsc")  # Seed | Difficulty | Score
                startingX = 82+155/2
                listOfTablets = []
                for game in lastFewGames:
                    listOfTablets.append(Tablet([startingX, 340], game))
                    startingX += 160

                listOfCurrentButtons.append(SmallButton([0, 0], 0, "Back"))
            else:
                #  Recent Scores have already been loaded so we should continue
                screen.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            location = 0
                    if event.type == MOUSEBUTTONDOWN:
                        for tablet in listOfTablets:
                            if tablet.rectangle.collidepoint(pygame.mouse.get_pos()):
                                location = 2
                                gameSeed = tablet.toReturnUponClick
                                listOfTablets = []
                        for button in listOfCurrentButtons:
                            if button.collisionArea.collidepoint(pygame.mouse.get_pos()):
                                location = button.value
                                listOfCurrentButtons = []
                                listOfTablets = []
                                clickSound.play()
                drawRectanglesFromList(listOfBackgroundStars, screen)
                for tablet in listOfTablets:
                    result = tablet.update()
                    screen.blit(result, tablet.rectangle)
                for button in listOfCurrentButtons:
                    result = button.draw()
                    screen.blit(result, button.collisionArea)

                screen.blit(selfCongratulatoryCredit, selfCongratulatoryCreditLocation)
                screen.blit(mainTitleText, mainTitleLocation)
                screen.blit(recentGamesText, recentGamesLocation)
                frameCounterThing = updateFPSCounter("FPS:" + str(int(clock.get_fps())))
                screen.blit(frameCounterThing[0], frameCounterThing[1])

                pygame.display.flip()
                clock.tick(60)
        elif location == 5:  # Random Seeds
            screen.fill((0, 0, 0))
            drawRectanglesFromList(listOfBackgroundStars, screen)
            if not tabletsLoaded:
                startingX = 82 + 155/2
                for iteration in [1, 2, 3]:
                    randomSeed = generateSeed()
                    difficulty = getDifficulty(randomSeed)
                    listOfTablets.append(SeedTablet([startingX, 370], randomSeed, "{0:.3f}".format(difficulty
                                                                                                   / maxDifficulty),
                                                    "Option " + str(iteration)))
                    startingX += 160
                listOfCurrentButtons.append(SmallButton([0, 0], 0, "Back"))
                listOfCurrentButtons.append(SmallButton([320-52, 200], 5, "Randomize"))
                tabletsLoaded = True
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        location = 0
                if event.type == MOUSEBUTTONDOWN:
                    for tablet in listOfTablets:
                        if tablet.rectangle.collidepoint(pygame.mouse.get_pos()):
                            location = 2
                            gameSeed = tablet.toReturnUponClick
                            listOfTablets = []
                            clickSound.play()
                    for button in listOfCurrentButtons:
                        if button.collisionArea.collidepoint(pygame.mouse.get_pos()):
                            location = button.value
                            tabletsLoaded = False
                            clickSound.play()
            drawRectanglesFromList(listOfBackgroundStars, screen)
            for tablet in listOfTablets:
                result = tablet.update()
                screen.blit(result, tablet.rectangle)
            for button in listOfCurrentButtons:
                result = button.draw()
                screen.blit(result, button.collisionArea)

            screen.blit(selfCongratulatoryCredit, selfCongratulatoryCreditLocation)
            screen.blit(mainTitleText, mainTitleLocation)
            screen.blit(randomSeedText, recentGamesLocation)
            frameCounterThing = updateFPSCounter("FPS:" + str(int(clock.get_fps())))
            screen.blit(frameCounterThing[0], frameCounterThing[1])

            clock.tick(60)
            pygame.display.flip()
            if location != 5:
                listOfCurrentButtons = []
                listOfTablets = []
        elif location == 6:   # End of game screen, regardless of win or loss
            # Add to the last 3 games list
            if not endGameLoaded:  
                endGameLoaded = not endGameLoaded
                lastFewGames = readFromFile(filePath + "/resources/text/previousGames.rsc")
                lastFewGames.pop()
                lastFewGames.insert(0, "|".join(endOfGameInfo))
                writeToFileFromList(lastFewGames, filePath + "/resources/text/previousGames.rsc")
                if endOfGameMessages[-1] == "NEW HIGH SCORE!!!":
                    writeToFileFromList([endOfGameInfo[2] + "|" + endOfGameInfo[0]],
                                        filePath + "/resources/text/highscore.txt")
            screen.fill((0, 0, 0))
            gameSeed = ""
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    for button in endOfGameButtons:
                        if button.testMouseCollision() != 0:
                            location = button.testMouseCollision() + 1
                            clickSound.play()
                if event.type == KEYDOWN and not alreadyTakenScreenShot:
                    if event.key == K_SPACE:
                        alreadyTakenScreenShot = toggle(alreadyTakenScreenShot)
                        takeScreenShotNOW = True
            startingY = 150
            for text in endOfGameMessages:
                newTextRender = extraScreenFont.render(text, 1, (255, 0, 0))
                newTextSize = getCoordinatesToCenterTextMiddle(extraScreenFont.size(text), [320, startingY])
                screen.blit(newTextRender, newTextSize)
                startingY += 50
            for button in endOfGameButtons:
                screen.blit(button.draw(), button.collisionArea)
            drawRectanglesFromList(listOfBackgroundStars, screen)
            screen.blit(selfCongratulatoryCredit, selfCongratulatoryCreditLocation)
            screen.blit(mainTitleText, mainTitleLocation)
            frameCounterThing = updateFPSCounter("FPS:" + str(int(clock.get_fps())))
            screen.blit(frameCounterThing[0], frameCounterThing[1])
            if takeScreenShotNOW and alreadyTakenScreenShot:
                takeScreenShotNOW = False
                now = datetime.datetime.now()
                nowString = ".".join([str(now.year), str(now.month), str(now.day), str(now.hour), str(now.minute)])
                pygame.image.save(screen, filePath+"/screenshots/Screenshot"+nowString+".png")
            pygame.display.flip()
            clock.tick(60)

        else:
            pygame.quit()
            sys.exit()
