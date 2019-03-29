import re

from core.courses import get_course

def course():
    course = get_course(41286)

    print(course)

if __name__ == '__main__':
    get_course()
