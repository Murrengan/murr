class CharacterEngine:

    def __init__(self, user, actions, base_class):

        self.name = user.name
        if base_class == 'weapon':
            self.actions = actions.weapon()
        if base_class == 'magic':
            self.actions = actions.magic()

    class Meta:
        ordering = ['name', 'actions']
        verbose_name_plural = 'asdljfasjdlfk'
