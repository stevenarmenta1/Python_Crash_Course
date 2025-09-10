def build_profile(first, last, **user_info):
    '''This funciton accepts first and last name and accepts arbitrary # of arguments about user info'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Steven', 'Armenta', location='San Bernardino', job='Computer Operations Technician', favorite_team='Patriots')
print(user_profile)