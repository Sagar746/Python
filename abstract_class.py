from abc import ABC, abstractmethod


class BankApp(ABC):
    def database(self):
        print('Connected to database')

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):
    '''
    object will not run until you, implement abstract security method.
    '''
    def mobile_login(self):
        print('Login into Mobile')

    def security(self):
        print('Mobile Security')


mob = MobileApp()
mob.mobile_login()
mob.security()