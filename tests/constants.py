class Links:
    base_url = {"prod": "https://qastand.valhalla.pw/",
                "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"


POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}
NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("qa_test@list.ru", "12345")
]

