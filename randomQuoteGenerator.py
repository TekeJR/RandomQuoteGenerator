import random

successQuotes = [
    "Success is not final; failure is not fatal: It is the courage to continue that counts. —Winston Churchill", 
    "It is better to fail in originality than to succeed in imitation. —Herman Melville",
    "The road to success and the road to failure are almost exactly the same. —Colin R. Davis",
    "Success usually comes to those who are too busy to be looking for it. —Henry David Thoreau",
    "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success. —Dale Carnegie",
    "Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan ‘Press On’ has solved and always will solve the problems of the human race. —Calvin Coolidge",
    "There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind. —Mister Rogers",
    "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable. —John Wooden",
    "I never dreamed about success. I worked for it.” —Estée Lauder",
    "Success is getting what you want; happiness is wanting what you get. ―W. P. Kinsella"
]

personalQuotes = [
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. —Winston Churchill",
    "Don’t let yesterday take up too much of today. —Will Rogers",
    "You learn more from failure than from success. Don’t let it stop you. Failure builds character. —Unknown",
    "If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. —Steve Jobs",
    "Experience is a hard teacher because she gives the test first, the lesson afterward. ―Vernon Sanders Law",
    "To know how much there is to know is the beginning of learning to live. —Dorothy West",
    "Goal setting is the secret to a compelling future. —Tony Robbins"
]

def displayQuotes():
    quoteNum = random.randint(0,1)
    if quoteNum == 0 : 
         print(random.choice(successQuotes))
    if quoteNum == 1 :
         print(random.choice(personalQuotes))

displayQuotes()
