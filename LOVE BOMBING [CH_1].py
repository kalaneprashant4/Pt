import telebot


BOT_TOKEN= input ('BOT TOKEN')

print ('CHAPTER 1 IS STARTED')
bot = telebot.TeleBot(BOT_TOKEN)


loved_ehra= {
    "what is love bombing": "Love bombing is a form of emotional manipulation where someone overwhelms you with excessive affection, attention, and gifts to gain control or influence over you.",
    "how to spot love bombing": "Signs of love bombing include excessive compliments, quick declarations of love, overwhelming attention, grand gestures early in the relationship, and attempts to isolate you from friends and family.",
    "why do people use love bombing": "People often use love bombing to gain control over another person, to create a sense of dependency, or to manipulate them into a relationship. It's commonly seen in individuals with narcissistic tendencies or those seeking to exploit others.",
    "what are the effects of love bombing": "The effects can include emotional dependency, confusion, low self-esteem, anxiety, depression, and difficulty trusting others in future relationships.",
    "how to protect yourself from love bombing": "To protect yourself, set and maintain clear boundaries, take relationships slowly, keep your social support network close, and trust your instincts if something feels too intense or too good to be true.",
    "what is the cycle of love bombing": "The cycle usually starts with intense affection and attention (love bombing), followed by manipulation, control, or devaluation, and can lead to emotional or even physical abuse. The abuser may then return to love bombing to regain control if the victim pulls away.",
    "what is the psychological impact of love bombing": "Victims may experience anxiety, confusion, self-doubt, depression, emotional dependency, and difficulty establishing boundaries in future relationships.",
    "how is love bombing related to narcissism": "Love bombing is commonly used by individuals with narcissistic personality traits. Narcissists use love bombing to quickly gain control over their victims by creating emotional dependency.",
    "can love bombing happen in friendships": "Yes, love bombing can happen in friendships, where one person overwhelms the other with attention, compliments, and support to establish control or emotional dependency.",
    "how to recover from love bombing": "Recovering from love bombing requires rebuilding self-esteem, recognizing manipulation patterns, seeking therapy or support, and learning to establish healthy emotional boundaries.",
    "how do narcissists use love bombing": "Narcissists use love bombing to charm their targets, gain their trust, and make them emotionally dependent. Once dependency is established, they may use manipulation, gaslighting, or control tactics.",
    "what is trauma bonding": "Trauma bonding is a strong emotional attachment formed between a victim and their abuser, typically in situations where love bombing is followed by abuse. The victim feels emotionally dependent on the abuser, making it difficult to leave.",
    "why is love bombing dangerous": "Love bombing is dangerous because it creates emotional dependency, leading victims to ignore red flags. It can also set the stage for future manipulation, emotional abuse, or control.",
    "is love bombing always intentional": "While love bombing is often used intentionally by manipulators, sometimes people with insecure attachment styles may engage in love bombing behavior without malicious intent.",
    "how to recognize healthy affection vs love bombing": "Healthy affection builds gradually over time and respects personal boundaries. Love bombing, on the other hand, feels overwhelming and often involves pressure for immediate intimacy or commitment.",
    "what is the difference between love bombing and genuine love": "Love bombing is manipulative, fast-paced, and overwhelming. Genuine love is built gradually through mutual respect, trust, and communication, without the need for constant validation or control.",
    "can love bombing lead to long-term relationships": "In most cases, love bombing is a tactic used to gain control. While some relationships may continue long-term, they are often based on manipulation, power imbalances, and emotional dependency.",
    "how does love bombing affect self-esteem": "Love bombing initially boosts the victim's self-esteem, but once the manipulator withdraws affection, the victim often experiences confusion, self-doubt, and a drop in self-worth.",
    "can love bombing happen in online relationships": "Yes, love bombing can happen in online relationships where someone showers you with attention, messages, and compliments to create a fast emotional connection and dependency.",
    "how does love bombing differ from normal romantic behavior": "Normal romantic behavior develops at a steady pace with respect for boundaries. Love bombing, on the other hand, is characterized by excessive and rapid affection, often with the intent to control.",
    "what are some examples of love bombing": "Examples include excessive texting, calling, constant compliments, extravagant gifts, planning a future together within days of meeting, and rushing emotional intimacy early on.",
    "why do victims stay with love bombers": "Victims often stay due to the emotional dependency created during the love bombing phase. The abuser may also use intermittent reinforcement, alternating between affection and neglect, making it hard to leave.",
    "can love bombing happen in family relationships": "Yes, love bombing can occur in family dynamics where one family member overwhelms another with attention or gifts to manipulate or control their actions.",
    "what is the goal of love bombing": "The goal of love bombing is to create emotional dependency so that the manipulator can gain control, power, or influence over the victim.",
    "how does love bombing affect future relationships": "Victims of love bombing may struggle to trust others, set boundaries, or develop healthy attachments in future relationships due to their past experiences of manipulation and emotional abuse.",
    "is love bombing a form of abuse": "Yes, love bombing is considered a form of emotional abuse because it manipulates the victim's feelings and creates dependency for the purpose of control.",
    "what should i do if i think i'm being love bombed": "If you think you're being love bombed, slow down the pace of the relationship, establish clear boundaries, seek support from friends or a therapist, and trust your instincts if something feels off.",
    "how does love bombing lead to emotional dependency": "Love bombing creates a sense of overwhelming affection, making the victim feel special and valued. When the manipulator withdraws affection, the victim craves it more, leading to emotional dependency.",
    "why do narcissists love bomb": "Narcissists love bomb to gain control and admiration from others. It's part of their need for validation and power over others, and once they establish control, they may switch to manipulation or neglect.",
    "what are red flags of love bombing": "Red flags include moving too fast in the relationship, constant texting or messaging, over-the-top compliments, extravagant gifts, isolating you from friends or family, and talking about future plans early on.",
    "how to handle love bombing in a new relationship": "Take things slow, set boundaries, communicate openly, and don't be afraid to take space if you're feeling overwhelmed. Surround yourself with supportive friends and family.",
    "how can therapy help with love bombing": "Therapy can help victims of love bombing recognize manipulation patterns, rebuild self-esteem, and establish healthy emotional boundaries in future relationships.",
    "can love bombing happen in workplaces": "Yes, love bombing can happen in workplaces, where a boss or coworker may overwhelm an employee with praise, gifts, or attention to establish control or manipulate them for personal gain.",
    "how is love bombing related to control": "Love bombing is a tool used to gain control over the victim by making them emotionally dependent. Once dependency is established, the manipulator can exert power and influence over their actions.",
    "is love bombing the same as infatuation": "No, love bombing is manipulative and designed to create dependency, while infatuation is a natural feeling of excitement or attraction that may occur in the early stages of a relationship.",
    "how does love bombing affect mental health": "Love bombing can lead to confusion, anxiety, depression, and emotional instability. The victim may also experience difficulty trusting others or setting boundaries in future relationships.",
    "exit": "Thank you for using the Love Bombing Q&A Tool. Stay safe and take care!"
}


questions_list = list(loved_ehra.keys())


user_progress = {}



def answer_question(question):
    question = question.lower()
    if question in loved_ehra:
        return loved_ehra[question]
    else:
        return "Sorry, I don't have an answer to that question. Please try asking something else or type 'exit' to quit."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Love Bombing Q&A Tool!\nAsk your questions about love bombing or type 'exit' to stop.\nType '/more' if you want to receive questions and answers automatically.")

@bot.message_handler(commands=['more'])
def handle_more(message):
    user_id = message.from_user.id

   
    if user_id in user_progress:
        progress = user_progress[user_id]
    else:
        
        
        progress = 0

    
    if progress < len(questions_list):
        next_question = questions_list[progress]
        next_answer = loved_ehra[next_question]

        
        bot.reply_to(message, f"Question: {next_question.capitalize()}\nAnswer: {next_answer}")

        
        user_progress[user_id] = progress + 1
    else:
        
        bot.reply_to(message, "CHAPTER 1 OF LOVE BOMBING Type '/more' again to restart from the beginning, or ask me a question! BY @MYEHRA")

        
        user_progress[user_id] = 0



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_question = message.text
    if user_question.lower() == 'exit':
        bot.reply_to(message, "Thank you for using the Love Bombing Tool. Stay safe and take care!")
    else:
        answer = answer_question(user_question)
        bot.reply_to(message, answer)



bot.polling()
