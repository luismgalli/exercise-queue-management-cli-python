class Queue:

    def __init__(self, mode, current_queue):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode



    def enqueue(self, item):
        self._queue.append(item)
        pass
    def dequeue(self):
        comensal = self._queue[0]
        if self._mode == 'FIFO':
            comensal = self._queue[0]
            #print(comensal)
            self._queue.pop(0)
        elif self._mode == 'LIFO':
            comensal = self._queue[-1]
            self._queue.pop(-1)
        else:
            print('error')
        return comensal 
    def get_queue(self):
        return self._queue
    def size(self):
        x = len(self._queue)
        return x