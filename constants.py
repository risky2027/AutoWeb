BASE_LINK = "https://qastand.valhalla.pw/"
LINKS = {"login": BASE_LINK + "login",
         "profile": BASE_LINK + "profile"}

POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}
NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("qa_test@list.ru", "12345")]
