def kth_from_end(self, k):

    length = self.length_()

    if not -length <= k < length:
        raise Exception("k not in the range")

    step_count = None

    if k >= 0:
            step_count = length - k -1
    if k < 0:
            step_count = abs(k)-1

    current = self.head
    for _ in range(step_count):
        current = current.next
        return current.value
