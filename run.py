from auto.rewards import Rewards

with Rewards(teardown=True) as bot:
    try:
        bot.landing_page()
        bot.daily_boxes()
    
    except:
        raise