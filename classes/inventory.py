

class ItemInterface:
    def __init__(self, name, itemType, description, value):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError
    
    def setName(self, name):
        raise NotImplementedError

    def getType(self):
        raise NotImplementedError

    def setType(self, itemType):
        raise NotImplementedError
    
    def getDescription(self):
        raise NotImplementedError
    
    def setDescription(self, description):
        raise NotImplementedError

    def getValue(self):
        raise NotImplementedError

    def setValue(self, value):
        raise NotImplementedError

class Item(ItemInterface):
    def __init__(self, name, itemType, description, value):
        self.name = name
        self.type = itemType
        self.description = description
        self.value = value
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        return self

    def getType(self):
        return self.type

    def setType(self, itemType):
        self.type = itemType
        return self
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self.value

class ItemManagerInterface:
    def __init__(self, item: ItemInterface, quantity):
        raise NotImplementedError
    
    def getItem(self):
        raise NotImplementedError
    
    def setItem(self, item):
        raise NotImplementedError
    
    def getQuantity(self):
        raise NotImplementedError
    
    def setQuantity(self, quantity):
        raise NotImplementedError
    
    def use(self):
        raise NotImplementedError

class ItemManager(ItemManagerInterface):
    def __init__(self, item: ItemInterface, quantity):
        self.item = item
        self.quantity = quantity
    
    def getItem(self):
        return self.item
    
    def setItem(self, item):
        self.item = item
        return self
    
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity
        return self
    
    def use(self):
        if self.quantity > 0:
            return True
        else:
            return False
        