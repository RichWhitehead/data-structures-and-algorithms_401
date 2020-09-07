from linked_list import LinkedList:
  
  
class Hashtable:
  
  def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

  def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].append([key, value])
        
  def _hash(self, key):
        # Get the ascii value of each char in the key
        hash_total = 0

        for ch in key:
            # sum char's
            hash_total += ord(ch)

        # multiple by some prime number for this example
        # modulo by size
        return (hash_total * 199) % self.size


  def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head

        while current:
            if current.data[0] == key:
                return current.data[1]
              
  def contains(self, key):
        """Method that takes in the key and returns a boolean, indicating if the key exists in the table already"""

        index = self.hash(key)

        if self._array[index] != 0 and self._array[index].includes(key):
            return True
        else:
            return False
