from time import sleep
from threading import Thread
from threading import current_thread


class MyThread(Thread):

    def run(self):
        sleep(3)
        print('I am running inside {}'.format(current_thread()))


if __name__ == '__main__':
    print('before starting thread')
    thread1 = MyThread()
    thread2 = MyThread()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('from {} thread'.format(current_thread()))
