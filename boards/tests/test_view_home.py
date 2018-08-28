"""
from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from ..views import BoardListView

class HomeTests(TestCase):

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url=reverse('boards:board_topics',kwargs={'pk':self.board.pk})
        self.assertContains(self.response,'href="{0}"'.format(board_topics_url))

"""
