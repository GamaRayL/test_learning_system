from main.models import Group


def assign_user_to_group(subscribe):
    """Добавление пользователя в группу."""

    user = subscribe.user
    product = subscribe.product
    min_users = product.min_users
    max_users = product.max_users
    group_name = f'{product} ({Group.objects.count()})'

    # Получить или создать группу
    group, created = Group.objects.get_or_create(name=group_name, defaults={
        'name': f'{product} (1)',
        'product': product}
    )
    # Добавить пользователя в группу
    group.students.add(user)

    # Проверить, не превышено ли максимальное количество пользователей в группе
    if min_users <= group.students.count() < max_users:
        group.students.add(user)
    else:
        # Создать новую группу, если текущая переполнена
        new_group_num = Group.objects.count() + 1
        new_group_name = f'{product} ({new_group_num})'
        print('new_group_name:', new_group_name)
        group = Group.objects.create(name=new_group_name, product=product)
        group.students.add(user)
        print('Создать новую группу, если текущая переполнена')

    # current_time = timezone.localtime(timezone.now())
    # if current_time < product.start_datetime:
    #     pass
