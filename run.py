from auto.rewards import Rewards

with Rewards(teardown=True) as bot:
    try:
        #bot.rewards_page()
      #  bot.daily_boxes()
       # bot.activate()
        bot.search_page()
        bot.alert_handle()
        bot.searches()
    except:
        raise