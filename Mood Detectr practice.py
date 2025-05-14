from textblob import TextBlob

name = input('whats your name')
print('Nice to meet you',name)
print('I am going to detect your sentiment')
print('type exit to quit')


while True:
    sentence = input('please neter your sentence')
    if sentence.lower()=='exit':
        print('bye ✌')
        break

    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity


    if sentiment > 0:
        print('Yaay✨')
    elif sentiment <0:
        print('😒')
    else:
        print('Neutral')
