import base64

client_id =  #spotify client Id
client_secret = #spotify client secret
refresh_token = #spotify totken
youtube_key = # youtube api
user_id = #user name spotify


# Concatenate client_id and client_secret with a colon in between
client_credentials = f"{client_id}:{client_secret}"

# Encode the concatenated string to base64
base_64 = base64.b64encode(client_credentials.encode()).decode()

#video playlist id here 
# how to do :- paste your youtube playlist url in chatgpt3 ask generate Playlist Id 
# Then paste here
neutral="PLbgGC47xqU0QDzDt3rP6_Iy6eMoOdqkDn"
happy="PLbgGC47xqU0T3GqDw8k5U8D-XZePzYkg4"
sad= "PLTMjKkzPoGXwg2s46Ytks3TZ8iWy-GDdO"
angry="PLTMjKkzPoGXwMKf9xhgpV8G8hEldq9HlZ"
surprise="PLbgGC47xqU0QDzDt3rP6_Iy6eMoOdqkDn"
fear="PLTMjKkzPoGXzNKyg3J3Tl_rklq7qG3uIP"

#spotify playlist id here 
# how to do :- paste your spotify playlist url in chatgpt3 ask generate Playlist Id 
# Then paste here
mneutral = "37i9dQZF1DWTt3gMo0DLxA"
mhappy="3L1UaheH1Xf3OQF6XcRP6m"
msad="0zmyFEUqh8sft3nh1aL1oT"
mangry="0b0pE8SeYz17nroEbiGCpR"
msurprise="1YpJXeOw0c4TrAG7U9c95c"
mfear="0JATw0IpBrmAmAyYjkIbdW"


# edit your own Quotes

emotion_quotes = {
    'Happy': [
        "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
        "The only thing that will make you happy is being happy with who you are. - Goldie Hawn",
        "Happiness is not by chance, but by choice. - Jim Rohn",
        "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
        "Happiness is the secret to all beauty. There is no beauty without happiness. - Christian Dior"
    ],
    'Sad': [
        "Tears are words that need to be written. - Paulo Coelho",
        "The way sadness works is one of the strange riddles of the world. - Lemony Snicket",
        "Every man has his secret sorrows which the world knows not; and often times we call a man cold when he is only sad. - Henry Wadsworth Longfellow",
        "You cannot protect yourself from sadness without protecting yourself from happiness. - Jonathan Safran Foer",
        "The word 'happy' would lose its meaning if it were not balanced by sadness. - Carl Jung"
    ],
    'Neutral': [
        "Life is a journey, not a destination. - Ralph Waldo Emerson",
        "Be yourself; everyone else is already taken. - Oscar Wilde",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
        "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown"
    ],
    'Angry': [
        "Speak when you are angry and you will make the best speech you will ever regret. - Ambrose Bierce",
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. - Mark Twain",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "Anger is never without a reason, but seldom with a good one. - Benjamin Franklin",
        "When angry, count to four; when very angry, swear. - Mark Twain"
    ],
    'Surprise': [
        "Life is full of surprises. - John Major",
        "The only thing that should surprise us is that there are still some things that can surprise us. - Francois de La Rochefoucauld",
        "The moments of happiness we enjoy take us by surprise. It is not that we seize them, but that they seize us. - Ashley Montagu",
        "Life is full of surprises and serendipity. - Rob Lowe",
        "The biggest surprise in life is that there are no surprises. - Uma Thurman"
    ],
    'Fear': [
        "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
        "The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown. - H.P. Lovecraft",
        "Expose yourself to your deepest fear; after that, fear has no power. - Jim Morrison",
        "Fear keeps us focused on the past or worried about the future. - Jonatan Mårtensson",
        "Don't give in to your fears. If you do, you won't be able to talk to your heart. - Paulo Coelho"
    ]
}

# you can edit what ever you want
constant_messages = {
    'Angry':"Angry:- I know you're passionate and driven. Use that fire within you to fuel positive change and stand up for what's right. Channel your energy into productive actions and let go of what no longer serves you. You can transform anger into determination and make a difference in the world!",
    'Happy':"Happy:- You're like a ray of sunshine brightening up everyone's day! Keep spreading your infectious joy and laughter wherever you go. Remember, even on cloudy days, your light can shine through. Embrace the little moments of bliss and cherish the beauty of life. Your smile is contagious, so let it sparkle!",
    'Fear':"Fear:-  It's okay to feel scared sometimes. But remember, courage isn't the absence of fear; it's facing your fears head-on. You're stronger and braver than you think. Trust in yourself and your abilities. Step out of your comfort zone and embrace new challenges. With every step you take, you're conquering fear and growing into the fearless warrior within you!",
    'Sad':"Sad:- I know you're feeling overwhelmed right now, but it's okay to not be okay. Allow yourself to feel and acknowledge your emotions. Remember, sadness is just a temporary visitor; it doesn't define who you are. Reach out to loved ones for support and comfort. Take gentle care of yourself and know that brighter days are ahead. You're not alone, and you're stronger than you realize!",
    'Neutral':"Netural:- Sometimes it's easy to feel overlooked or overshadowed, but you're an essential part of the emotional spectrum. Your calm and balanced presence brings stability and grounding to chaotic situations. Embrace your role as the steady anchor amidst life's storms. Take this opportunity to recharge and find peace within yourself. Your tranquil energy is a valuable gift to the world!",
    'Surprise': "Surprise:- Life is full of unexpected twists and turns, and that's what makes it exciting! Embrace the element of surprise and welcome the unknown with open arms. Instead of fearing change, see it as an opportunity for growth and adventure. Keep an open mind and heart, and allow yourself to be pleasantly surprised by the magic of life!"
}