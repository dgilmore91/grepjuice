import re


def cleanTweet(tweetToClean, separators):
    currentTextState = tweetToClean
    for separator in separators:
        currentTextState = cleanWithSeparator(currentTextState, separator)
    return getFirstQuestion(currentTextState)


def cleanWithSeparator(tweetToClean, separatorString):
    splitText = tweetToClean.split()

    fixedText = []
    for substring in splitText:
        if(substring[:len(separatorString)] != separatorString):

            fixedText.append(substring)

    fixedText.append('\n')

    return ' '.join(fixedText)


def getFirstQuestion(tweetWithQuestion):
    pattern = re.compile('(?<=_\?)')
    return pattern.split(tweetWithQuestion)


def getAllSentences(tweetWithSentences):
    pattern = re.compile(r'\?')
    print pattern.search(tweetWithSentences)
