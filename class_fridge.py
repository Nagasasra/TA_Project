class Fridge:

    def __init__(self, capacity=15):
        # the value for capacity is abstracted, it's not based on any real world measurement such as meters or
        # kilogram or mole so it's up to your imagination, sorry I can't come up with any ideas for this one
        self.__capacity = capacity
        # the fridge is empty at start, you are free to fill it with whatever you want
        self.__items = []
        self.__dicts = {}

    def store_an_item(self):
        item = input("Let's fill the Fridge with a/an: ")
        if sum(self.__dicts.values()) == self.__capacity:
            print("Sorry, the fridge has reached it's maximum capacity.")
            return False
        elif item in self.__items:
            self.__dicts[item] += 1
            return True
        else:
            self.__items += [item]
            self.__dicts[item] = 1
            return True

    def capacity_check(self):
        # available_space = self.__capacity - len(self.__items)
        available_space = self.__capacity - sum(self.__dicts.values())
        if len(self.__items) == 0:
            print("The current fridge is empty, it can hold as many as", self.__capacity, "items.")
        # elif len(self.__items) == self.__capacity:
        elif sum(self.__dicts.values()) == self.__capacity:
            print("The current fridge has reached its maximum capacity, which holds", self.__capacity, "items.")
        else:
            print("This fridge can still hold " + str(available_space) + " more items out of", self.__capacity)

    def print_items_amount(self):
        print("The list of items with its corresponding amount in the fridge:", self.__dicts)

    def print_items_list(self):
        print("The kind of things currently on the fridge:", self.__items)

    def retrieve_an_item(self):
        # iteration = 0
        item = input("Let's take something out of the fridge, which is a/an: ")
        if item in self.__items:
            if self.__dicts[item] >= 1:
                self.__dicts[item] -= 1
                if self.__dicts[item] == 0:
                    self.__items.remove(item)
                    return True
                else:
                    return True
        else:
            return False, print("ERROR: Requested item not found")
        # while iteration < len(self.__items): # decided not to use this since the implementation of dictionaries
            # if self.__items[iteration] == item:
                # self.__items.pop(iteration)
                # return iteration, (self.__dicts[item] - 1)
            # iteration += 1

    def replace_an_item(self):
        if self.retrieve_an_item() is not False:
            self.store_an_item()

    # def replace_according_to_idx(self): # decided not to include this one since the implementation of dictionaries
        # idx_retrieved = self.retrieve_an_item()
        # if idx_retrieved is not None:
            # new_item = input("Let's replace it according to its corresponding index (" + str(idx_retrieved) + ") with: ")
            # self.store(new_item)
            # self.__items.insert(idx_retrieved, new_item)


