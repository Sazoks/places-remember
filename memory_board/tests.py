import random

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Memory


class MemoriesTest(TestCase):
    """
    Тесты для контроллеров с основным функционалом.

    Тестами покрыт основной функционал: получение списка
    воспоминаний и добавление новых воспоминаний.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """Метод для установки тестовых данных"""

        MAX_TEST_DATA = 5

        cls.USERS_PASSWORD = 'pass_123_PASS'
        cls.UserModel = get_user_model()

        # Создаем в тестовой БД несколько юзеров.
        cls.UserModel.objects.bulk_create([
            cls.UserModel(
                username=f'username_{i}',
                email=f'email_{i}@user.com',
                password=cls.USERS_PASSWORD,
            )
            for i in range(MAX_TEST_DATA)
        ])

        # .bulk_create только лишь создает записи в БД.
        # Для получения этих записей с id нужно сделать запрос.
        cls.test_users = cls.UserModel.objects.all()

        # Генерируем для каждого пользователя по несколько воспоминаний.
        MIN_COUNT_MEMORIES = 1
        MAX_COUNT_MEMORIES = 5
        for current_user in cls.test_users:
            memories_current_user = [
                Memory(
                    title=f'title_{i}',
                    description=f'description_{i}',
                    address=f'address_{i}',
                    user=current_user,
                )
                for i in range(random.randint(MIN_COUNT_MEMORIES,
                                              MAX_COUNT_MEMORIES))
            ]
            Memory.objects.bulk_create(memories_current_user)

    def test_user_memories(self) -> None:
        """
        Тестирование получения списка воспоминаний для каждого пользователя.

        Тестируем для каджого пользователя, чтобы убедиться, что пользователь
        имеет доступ только к своим воспоминаниям и никаким другим.
        """

        for current_user in self.test_users:
            with self.subTest(f'Воспоминания {current_user.username}'):
                # Пропускаем процедуру авторизации.
                self.client.force_login(current_user)

                # Делаем GET-запрос на получение списка воспоминаний.
                response = self.client.get(reverse('memory_board:list_or_create'))

                self.assertEqual(response.status_code, 200)

                # Генерируем списки с id воспоминаний и проверяем по ним.
                response_memories_id = \
                    tuple(response.context['memories'].values_list('pk', flat=True))
                current_user_memories_id = \
                    tuple(current_user.memories.values_list('pk', flat=True))

                self.assertEqual(response_memories_id, current_user_memories_id)

    def test_create_memory(self) -> None:
        """Тест создания нового воспоминания"""

        current_user = self.test_users[0]
        old_count_memories = current_user.memories.count()

        self.client.force_login(current_user)

        # Делаем запрос на создание нового воспоминания.
        response = self.client.post(
            path=reverse('memory_board:list_or_create'),
            data={
                'title': 'new_title',
                'description': 'new_description',
                'address': 'new_address',
            },
        )

        # При успешном добавлении нового воспоминания происходит редирект на
        # ту же страницу с формой и списком.
        self.assertRedirects(
            response=response,
            expected_url=reverse('memory_board:list_or_create'),
            status_code=302,
            target_status_code=200,
        )
        self.assertEqual(current_user.memories.count(), old_count_memories + 1)
