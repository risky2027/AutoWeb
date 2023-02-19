class Links:
    base_url = "https://qastand.valhalla.pw/"
    login = base_url + "login"
    profile = base_url + "profile"
    blog = base_url + "blog"


POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}
NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("qa_test@list.ru", "12345")
]

SESSION_COOKIE = {'name': 'session',
                  'value':
                  'eyJfZnJlc2giOmZhbHNlfQ.Y_IDrA.Be3ENJPpInFgJGKgqllFvvY8eLs'
                  }
