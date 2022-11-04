## before starting tutorial (record this last !!)

saying hi to people
inruducing video idea with our menu bot (telling people to contact me for info)
reminding them to like if they like dislike if they dont sub for more

## first section of tutorial

before we start coding (introduce keyboard types supported by telegram)
today we are talking about the replykeaboard (inline keyboard next videos)
how is that keyboard useful for users

## ideas for future videos

- inline keyboeard
- what is a programming language (set of tools)
- parse html links in telegram messages
- bar code generator bot
- quiz bot (sends polls of quizes like)
  ````
  def poll(msg):
    """
    on poll
    -
    sending quiz question randomly
    """
    chat_id = msg.chat.id
    question = 'كم عدد الاضلاع في جسم الانسان ؟'
    options =[
        "12",
        "24",
        "26",
        "18"
    ]
    bot.send_poll(chat_id,question,options,correct_option_id=1,type='quiz',open_period=60)
    ```
  ````
# telebot_replykeyboard
