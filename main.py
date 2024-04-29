from mainwindow import *


def main():
    handle = Window()
    handle2 = Window()

    handle.title('Daw')
    handle.geometry('1280x720')

    assert (handle2 is handle)
    handle2.title('Daw')
    handle2.geometry('1280x720')

    handle.mainloop()
    handle2.mainloop()


if __name__ == '__main__':
    main()
