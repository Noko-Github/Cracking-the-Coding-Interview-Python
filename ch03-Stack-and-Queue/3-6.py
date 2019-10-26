class AnimalNode:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        self.order = None
        self.next = None

    def set_order(self, order):
        self.order = order


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_to_tail(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def remove_from_head(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node

    def peek_head(self):
        if self.head is None:
            return None
        return self.head


class AnimalQueue:
    def __init__(self):
        self.order = 0
        self.dog_queue = LinkedList()
        self.cat_queue = LinkedList()

    def enqueue(self, value, type):
        node = AnimalNode(value, type=type)
        node.set_order(self.order)
        self.order += 1

        if type == 'dog':
            self.dog_queue.add_to_tail(node)
        else:
            self.cat_queue.add_to_tail(node)

    def dequeue_dog(self):
        return self.dog_queue.remove_from_head()

    def dequeue_cat(self):
        return self.cat_queue.remove_from_head()

    def dequeue_any(self):
        dog = self.dog_queue.peek_head()
        cat = self.cat_queue.peek_head()
        if dog.order < cat.order:
            return self.dog_queue.remove_from_head()
        else:
            return self.cat_queue.remove_from_head()


animal_queue = AnimalQueue()
animal_queue.enqueue(1, 'dog')
animal_queue.enqueue(2, 'cat')
animal_queue.enqueue(3, 'dog')
animal_queue.enqueue(4, 'cat')
animal_queue.enqueue(5, 'dog')
animal_queue.enqueue(6, 'cat')
animal_queue.enqueue(7, 'dog')
animal_queue.enqueue(8, 'cat')
animal_queue.enqueue(9, 'dog')

print(animal_queue.dequeue_any().value)
print(animal_queue.dequeue_dog().value)
print(animal_queue.dequeue_cat().value)
print(animal_queue.dequeue_any().value)
print(animal_queue.dequeue_cat().value)
