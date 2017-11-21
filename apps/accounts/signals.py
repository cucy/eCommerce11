from django.dispatch import Signal

user_logged_in = Signal(
    providing_args=[
        'instance', 'request']
)  # 用户登录触发信号
