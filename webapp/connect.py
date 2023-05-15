from webapp import app
from flask import render_template
from webapp import card
from webapp import test


# connection for homepage
@app.route('/')
def index():
    return render_template("index.html")


# one-card page
@app.route('/oneCard', strict_slashes=False)
def one_Card():
    tarot_deck = card.get_deck()
    tarot_card = card.get_card(tarot_deck)
    # tarot_name = card.get_name()

    tarot_story = test.findFortuneTellingByName(tarot_card[0]['name'])
    tarot_storyReversed = test.findFortuneTellingByNameReversed(tarot_card[0]['name'])
    if tarot_card[0]['cardtype'] == "major":
        return render_template("oneCard.html",
                               name=tarot_card[0]['name'],
                               title=tarot_card[0]['name'],
                               rev=tarot_card[1],
                               meaning=tarot_story,
                               message=tarot_card[0]['message'],
                               reversed_meaning=tarot_storyReversed,
                               image=tarot_card[0]['image'],
                               url=tarot_card[0]['url'],
                               cardtype=tarot_card[0]['cardtype'])
    else:
        return render_template("oneCard.html",
                               name=tarot_card[0]['name'],
                               title=tarot_card[0]['name'],
                               rev=tarot_card[1],
                               meaning=tarot_story,
                               reversed_meaning=tarot_storyReversed,
                               image=tarot_card[0]['image'],
                               url=tarot_card[0]['url'],
                               cardtype=tarot_card[0]['cardtype'])


@app.route('/threeCard', strict_slashes=False)
def three_card():
    my_deck = card.get_deck()
    hand = []
    num = 1
    while num < 4:
        my_card = card.get_card(my_deck)
        hand.append(my_card)
        num += 1

    for i in range(len(hand)):
        tarot_story = test.findFortuneTellingByName(hand[i][0]['name'])
        hand[i][0]['desc'] = tarot_story
        hand[i][0]['rdesc'] = tarot_story


    return render_template("threeCard.html", hand=hand, title="Three card spread")

