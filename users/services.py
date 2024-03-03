from django.db.models import Count

from main.models import Group


def assign_user_to_group(subscribe):
    """Добавление пользователя в группу."""
    user = subscribe.user
    product = subscribe.product
    min_users = product.min_users
    max_users = product.max_users
    num_existing_groups = max(1, product.groups.count())
    new_group_name = f'{product} ({num_existing_groups})'

    group = Group.objects.filter(name=new_group_name).first()

    if not group:
        group = Group.objects.create(name=new_group_name, product=product)
        group.students.add(user)
        print(f'Создана новая группа {group.name}')
    else:
        # Проверить, не превышено ли максимальное количество пользователей в группе
        if min_users <= group.students.count() < max_users:
            group.students.add(user)
            print(f'Пользователь добавлен в текущую группу {group.name}')
        else:
            # Создать новую группу, если текущая переполнена
            new_group_num = num_existing_groups + 1
            new_group_name = f'{product} ({new_group_num})'
            group = Group.objects.create(name=new_group_name, product=product)
            group.students.add(user)
            print(f'Текущая группа переполнена. Создаю новую группу {group.name} (и добавлю пользователя)')


def shuffle_students_in_group():
    groups_to_process = Group.objects.annotate(num_students=Count('students')).filter(num_students__lt=3)

    for group in groups_to_process:
        prefix = group.name.split('.')[0]
        print(f'Обработка групп с префиксом {prefix}')

        similar_groups = Group.objects.filter(name__contains=prefix)

        for similar_group in similar_groups:
            print(similar_group.students.all())
            print(f'Группы с похожим названием: {similar_group}')


shuffle_students_in_group()

# current_time = timezone.localtime(timezone.now())
# if current_time < product.start_datetime:
#     pass
