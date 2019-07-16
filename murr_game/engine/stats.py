import copy


class Stats:
    """
    Перечень характеристик
    """

    stats = {'hp': 100, 'mp': 40, 'armor': 0}

    @classmethod
    def weapon(cls):
        stats = copy.deepcopy(cls.stats)
        stats['hp'] += 10
        stats['mp'] -= 10
        stats['armor'] += 10
        return stats

    @classmethod
    def magic(cls):
        stats = copy.deepcopy(cls.stats)
        stats['hp'] -= 10
        stats['mp'] += 10
        return stats

    @classmethod
    def trick(cls):
        stats = copy.deepcopy(cls.stats)
        return stats
