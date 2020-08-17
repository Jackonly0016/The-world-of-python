class MenuItem(object):
    def __init__(self, title, cost, long_desc='', short_desc='', item_type='main'):
        self.title = title
        self.cost = cost
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type

    def change_item_type(self, item_type):
        self.item_type = item_type

    def change_cost(self, cost):
        self.cost = cost

    def change_description(self, long_desc='', short_desc=''):
        if long_desc:
            self.long_desc = long_desc
        if short_desc:
            self.short_desc = short_desc

    def change_title(self, title):
        sef.title = title

    def print_item(self, desc_type='short'):
        print("{title} ... ${cost}.format(title=self.title, cost=self.cost)")
        if desc_type == 'short':
            print(self.short_desc)
        if desc_type == 'long':
            print(self.long_desc)

class Menu(object):
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def print_menu(self):
        print("Breakfast")
        for item in self.breakfast:
            item.print_item()
        print()
        print("Lunch")
        for item in self.lunch:
            item.print_item()
        print()
        print("Dinner")
        for item in self.dinner:
            item.print_item()

class CateringItem(MenuItem):
    def __init__(self, title, cost, number_servers,
            special_instr='', long_desc='', short_desc='', item_type='main'):
        super(MenuItem, self).__init__(
                title = title,
                cost = cost,
                long_desc = long_desc,
                short_desc = short_desc,
                item_type = item_type)
        self.number_servers = number_servers
        self.special_instr =special_instr

    def print_item(self, desc_type='short'):
        print("{title} ... ${cost}.format(title=self.title, cost=self.cost)")
        print("Serves: ", self.number_servers)
        if desc_type == 'short':
            print(self.short_desc)
        if desc_type == 'long':
            print(self.long_desc)
        if self.special_instr:
            print("Special instructions: ", self.special_instr)

