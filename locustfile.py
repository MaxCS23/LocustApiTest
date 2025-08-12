from locust_tests.users.basic_user import BasicUser
from locust_tests.users.heavy_user import HeavyUser
from locust_tests.users.data_user import DataUser

users = [BasicUser, HeavyUser, DataUser]
