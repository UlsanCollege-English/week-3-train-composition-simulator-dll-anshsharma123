# src/train.py

class _Car:
    __slots__ = ("id", "prev", "next")
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        """Attach a new car to the front."""
        node = _Car(car_id)
        if not self.head:  # empty train
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def attach_back(self, car_id):
        """Attach a new car to the back."""
        node = _Car(car_id)
        if not self.tail:  # empty train
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def detach_front(self):
        """Detach car from the front and return its id."""
        if not self.head:
            return None
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # train is now empty
        return node.id

    def detach_back(self):
        """Detach car from the back and return its id."""
        if not self.tail:
            return None
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None  # train is now empty
        return node.id

    def detach(self, car_id):
        """
        Remove the first car with matching id.
        Return True if removed, False otherwise.
        """
        node = self.head
        while node:
            if node.id == car_id:
                # Fix neighbors
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                return True
            node = node.next
        return False

    def to_list(self):
        """Return all car ids as a list."""
        out = []
        node = self.head
        while node:
            out.append(node.id)
            node = node.next
        return out
