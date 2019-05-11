class BaseProcessor:
    MODEL = None

    def __init__(self, data):
        self._raw = data
        self.params = {}
        self.errors = {}
        self._instance = None
        self._processed_field = None

    def process(self):
        self._process()
        self._post_process()
        self._instance = self._get_instance()

    def save(self):
        self._instance.save()

    def delete(self):
        if self._instance.pk:
            self._instance.delete()

    def _process(self):
        for field in self._get_fields():
            method_name = f'_process_{field.name}'
            method = getattr(self, method_name, lambda: None)
            self._processed_field = field.name
            self.params[field.name] = method()

    def _post_process(self):
        pass

    def _get_fields(self):
        fields = []
        for field in self.MODEL._meta.fields:
            if field.name != 'id' or self._raw.get('id'):
                fields.append(field)
        return fields

    def _get_instance(self):
        try:
            return self.MODEL.objects.get(**self.params)
        except self.MODEL.DoesNotExist:
            return self.MODEL(**self.params)

    def _err(self, message, field=None):
        field = field or self._processed_field
        self.errors[field] = message
