from typing import Union, Dict

from api.api_client import Client


class BlogApi(Client):
    """"Класс с методами для отправки api-запросов к блогу"""
    _posts = "api/posts"

    #def __init__(self, url):
    #    super().__init__(url)
    #    self._posts = "api/posts"

    def get_user_posts(self) -> Union[Dict, None]:
        """Метод для получения всех постов пользователя"""
        a = self._session.get("https://qastand.valhalla.pw/api/posts")
        return self.get(self._posts)

    def delete_user_posts(self, post_id: int) -> Union[Dict, None]:
        """Метод для получения всех постов пользователя"""
        return self.delete(f"{self._posts}/{post_id}")

    #post create
