class HashTableEntry:
    # Node
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.stored = 0
        self.storage = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # number of keys stored divided by capacity
        return self.stored / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        fnv_prime = 1099511628211
        fnv_offset_basis = 14695981039346656037

        hash_index = fnv_offset_basis

        bytes_representation = key.encode()
        # encoding key input, gives back bytes that represent the key (usually a string)
        # now we have a bunch of numbers which we can compute with

        for byte in bytes_representation:
            hash_index *= fnv_prime
            hash_index ^= byte

        return hash_index

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # mod with length of data, get the remainder
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        # if no collision, store key value pair as the head of a linked list
        if not self.storage[index]:
            self.storage[index] = HashTableEntry(key, value)
            self.stored += 1

        # if something already exists at that index, add to linked list
        else:
            # store pointer to current node
            current_node = self.storage[index]

            # if not updating a key/value, go to end of list
            while current_node.key != key and current_node.next:
                # stored node pointer is now the next node
                current_node = current_node.next

            # if updating existing entry value
            if current_node.key == key:
                current_node.value = value

            # else, add to end of list
            else:
                current_node.next = HashTableEntry(key, value)
                self.stored += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        # store pointer to current node
        current_node = self.storage[index]

        if not current_node:
            print("Key not found.")

        # value to delete is head
        elif not current_node.next:
            self.storage[index] = None
            self.stored -= 1

        else:
            # store pointer to previous node
            previous_node = None

            # while key doesn't match and not at end of list, move to next node
            while current_node.key != key and current_node.next:
                previous_node = current_node
                current_node = current_node.next

            # element to delete is at end of list so make next pointer None
            if not current_node.next:
                previous_node.next = None
                self.stored -= 1

            # element to delete is in middle
            else:
                # reassign pointers
                previous_node.next = current_node.next
                self.stored -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        # if node exists, store as current node
        if self.storage[index]:
            current_node = self.storage[index]

            # while key doesn't match and there is a next, move to next
            while current_node.key != key and current_node.next:
                current_node = current_node.next

            # if at end of list, that is the key
            if not current_node.next:
                return current_node.value

            # else, that node is the correct node
            else:
                return current_node.value

        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # pointer to old hash table
        old_storage = self.storage

        # initalize new hash table
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # resize old hash table
        for elem in old_storage:
            if elem:
                current_node = elem

                while current_node:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next


# this means we are running from the command line
# otherwise we are being imported
# therefore this will only run in this .py file from the command line
if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
