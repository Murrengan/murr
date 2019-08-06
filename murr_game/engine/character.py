class CharacterEngine:

    def __init__(self, user, actions, stats, base_class):

        self.name = user.name
        if base_class == 'weapon':
            self.actions = actions.weapon()
            self.stats = stats.weapon()
        if base_class == 'magic':
            self.actions = actions.magic()
            self.stats = stats.magic()

    class Meta:
        ordering = ['name', 'actions', 'stats']
        verbose_name_plural = 'asdljfasjdlfk'
