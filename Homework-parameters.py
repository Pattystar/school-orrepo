# Тут было бы неполхо импортировать module, содержащий список возможных formts данных.
# Существует ли такой?

class Format(object):
    def __init__(self, formt):
        self.formt = formt

    def add_formt(self, formt):
        if not in module.formts:  # Импортированный модуль
            raise OrderException('Невозможно создать документ в указанном формате.')

        self.formts.append(formt)

    def get_info(self):
        return self.format


class Prarm(Format):
    def __init__(self, name, text, formt)
        super().__init__(formt)
        self.name = name
        self.text = text

    def get_info(self):
        return param. {}: {}. {}.format(self.name, self.text, self.formt)
    
