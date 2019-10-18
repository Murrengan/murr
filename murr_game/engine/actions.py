class Actions:
    """
    Перечень возможных действий
    """

    punch = {'action_name:': 'punch', 'power': 5, 'help_text': 'hit', 'mana': '2'}

    @classmethod
    def weapon(cls):
        enrage = {'action_name:': 'enrage', 'power': 5, 'help_text': 'Update group punch +4 on 7 move', 'mana': '15'}
        bleed_strike = {'action_name:': 'bleed_strike', 'power': 5, 'help_text': 'Periodic damage 3 on 4 move',
                        'mana': '5'}
        strong_punch = {'action_name:': 'strong_punch', 'power': 5, 'help_text': 'Punch +5', 'mana': '5'}
        fear = {'action_name:': 'fear', 'power': 0, 'help_text': 'Try to scare the target on 3 moves', 'mana': '20'}
        return [cls.punch, enrage, bleed_strike, strong_punch, fear]

    @classmethod
    def magic(cls):
        mental_strike = {'power': 10, 'help_text': 'Классический удар сильнее на 10, мана 8'}
        actions_control = {'power': 10, 'help_text': 'Попытка напугать цель на 2 хода хода, мана 30'}
        healing = {'power': 10, 'help_text': 'Исцеление цели 20, мана 15'}
        return [cls.punch, mental_strike, actions_control, healing]

    @classmethod
    def trick(cls):
        liquid = {'power': 0, 'help_text': 'Возможность группе уклониться от атаки на 5 ходов, уклонение +20%, мана 20'}
        sleep = {'power': 0, 'help_text': 'Попытка усыпить или ослабить цель на 3 хода хода, мана 20'}
        blow = {'power': 15, 'help_text': 'Классический удар сильнее на 15, вероятность критического удара +15%,мана 20'}
        return [cls.punch, liquid, sleep, blow]
