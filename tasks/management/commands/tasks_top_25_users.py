from django.contrib.auth.models import User
from django.core.management import BaseCommand

class Command(BaseCommand):
	def handle(self, *args, **options):
		users_tasks = {}

		for u in User.objects.all():
			users_tasks[u] = 0

			for t in u.tasks.all():
				users_tasks[u] += 1

		list_u_t = list(users_tasks.items())
		list_u_t.sort(key=lambda i: i[1])

		for i in range(25):
			print('У', list_u_t[-i][0], list_u_t[-i][1], 'задачь.')