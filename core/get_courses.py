import re

from courses import *
from accounts import get_subaccounts
from terms import get_canvas_terms

def course():
    # course_pages = get_course_pages(2531)
    course_id = 2531
    page_url = 7149

    course_pages = get_course_page(2531, 7149)
    new_content = '<p>Test Content. Hi there.</p>' + course_pages['body']
    print(course_pages['body'])

    # update_course_page_contents(course_id, page_url, new_content)

    # courses = get_courses_by_account_id(1, 4)

    # print(courses)

    # terms = get_canvas_terms()

    # print(terms)

    # accounts = get_subaccounts(1)

    # print(accounts)

if __name__ == '__main__':
    course()
