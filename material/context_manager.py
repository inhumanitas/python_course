# coding: utf-8

fh = open('test_file_path.txt', 'w')
fh.write('test string')

with open('test_file_path.txt', 'r') as fh:
    lines = fh.readlines()
    print lines


class Hypervisor(object):
    """
    Hypervisor representation
    """

    __locked = False

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False

    def is_locked(self):
        return self.__locked

    def power_action(self, action):
        raise NotImplemented()


hyp1 = Hypervisor()
hyp1.lock()
# hyp1.power_action(1)
hyp1.unlock()

hypervisors = [Hypervisor() for i in range(100)]

for h in hypervisors:
    h.lock()
    # h.power_action(1)
    h.unlock()


# ------------------------------------------------------------------------
# context manager

class LockNode(object):
    """
    Lock node context manager
    """

    def __init__(self, hypervisor):
        super(LockNode, self).__init__()
        self.hypervisor = hypervisor

    def __enter__(self):
        self.hypervisor.lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.hypervisor.unlock()
        # return True


with LockNode(hyp1):
    hyp1.power_action(1)


for h in hypervisors:
    with LockNode(h):
        h.power_action(1)
