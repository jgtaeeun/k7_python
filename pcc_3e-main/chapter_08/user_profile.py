def build_profile(first, last, **user_info):    #**를 사용하여 딕셔너리
    """Build a dictionary containing everything we know about a user."""

    #딕셔너리 키,값 쌍으로 추가
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)