from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define options for dropdowns
EMOTIONS = [
    "Anger: I felt mad.", "Anger: I felt upset.", "Anger: I felt annoyed.",
    "Anger: I felt furious.", "Anger: I felt irritated.", "Jealousy: I felt envious.",
    "Jealousy: I felt unhappy.", "Jealousy: I felt left out.", "Jealousy: I felt bitter.",
    "Jealousy: I felt not good enough.", "Hatred: I felt lots of dislike.", "Hatred: I felt angry.",
    "Hatred: I felt mean.", "Hatred: I felt disgusted.", "Hatred: I felt hurt.",
    "Bitterness: I felt resentful.", "Bitterness: I felt grumpy.", "Bitterness: I felt sour.",
    "Bitterness: I felt sad.", "Bitterness: I felt heavy.", "Selfishness: I felt greedy.",
    "Selfishness: I felt stuck up.", "Selfishness: I felt selfish.", "Selfishness: I felt uncaring.",
    "Selfishness: I felt inconsiderate.", "Love: I felt caring.", "Love: I felt warm inside.",
    "Love: I felt friendly.", "Love: I felt happy for others.", "Love: I felt compassionate.",
    "Joy: I felt very happy.", "Joy: I felt cheerful.", "Joy: I felt excited.",
    "Joy: I felt playful.", "Joy: I felt glad.", "Peace: I felt calm.", "Peace: I felt relaxed.",
    "Peace: I felt safe.", "Peace: I felt content.", "Peace: I felt easygoing.",
    "Forbearance (Patience): I felt understanding.", "Forbearance (Patience): I felt tolerant.",
    "Forbearance (Patience): I felt calm while waiting.", "Forbearance (Patience): I felt accepting.",
    "Forbearance (Patience): I felt steady.", "Kindness: I felt helpful.", "Kindness: I felt friendly.",
    "Kindness: I felt generous.", "Kindness: I felt nice.", "Kindness: I felt caring.",
    "Goodness: I felt pure.", "Goodness: I felt honest.", "Goodness: I felt trustworthy.",
    "Goodness: I felt right.", "Goodness: I felt decent.", "Faithfulness: I felt loyal.",
    "Faithfulness: I felt true.", "Faithfulness: I felt committed.", "Faithfulness: I felt devoted.",
    "Faithfulness: I felt steady.", "Gentleness: I felt soft.", "Gentleness: I felt calm.",
    "Gentleness: I felt kind.", "Gentleness: I felt mild.", "Gentleness: I felt tender.",
    "Self-Control: I felt focused.", "Self-Control: I felt disciplined.",
    "Self-Control: I felt in charge of myself.", "Self-Control: I felt patient.",
    "Self-Control: I felt reserved."
]

FRUITS_OF_THE_SPIRIT = [
    "Love", "Joy", "Peace", "Patience", "Kindness", "Goodness", "Faithfulness", "Gentleness", "Self-Control"
]

FRUITS_OF_THE_FLESH = [
    "Anger", "Jealousy", "Hatred", "Bitterness", "Selfishness"
]

@app.route('/')
def index():
    return render_template('index.html', emotions=EMOTIONS, fruits_of_the_spirit=FRUITS_OF_THE_SPIRIT,
                           fruits_of_the_flesh=FRUITS_OF_THE_FLESH)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "date": request.form.get("date"),
        "morning_reflection": request.form.get("morning_reflection"),
        "situation": request.form.get("situation"),
        "handled": request.form.get("handled"),
        "emotion": request.form.get("emotion"),
        "fruit_of_the_spirit": request.form.get("fruit_of_the_spirit"),
        "fruit_of_the_flesh": request.form.get("fruit_of_the_flesh"),
        "effectiveness": request.form.get("effectiveness"),
        "overview": request.form.get("overview")
    }
    # Save the data to a file for persistence
    with open("user_data.txt", "a") as file:
        file.write(f"{data}\n")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
