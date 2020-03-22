import configparser
import getpass
import pymysql


class Decorators:
    # Question now is: Why would you use this decorator if you can just call the method?
    # It doesn't interact with the variables..
    @staticmethod
    def determine_environment(func):
        def wrapper(*args, **kwargs):
            sensitive_configuration = configparser.ConfigParser()
            try:
                sensitive_configuration.read("sensitive.ini")
                if not sensitive_configuration.sections():
                    print(
                        "Could not read sensitive configuration file. You need your own credentials to launch this program"
                    )
                else:
                    global_configuration = configparser.ConfigParser()
                    global_configuration.read("configuration.ini")
                    if (
                        getpass.getuser()
                        == sensitive_configuration["PRODUCTION"]["ServerUser"]
                    ):
                        if (
                            global_configuration["DEFAULT"]["ActiveEnvironment"]
                            != "PRODUCTION"
                        ):
                            global_configuration["DEFAULT"][
                                "ActiveEnvironment"
                            ] = "PRODUCTION"
                            with open("configuration.ini", "w") as conf:
                                global_configuration.write(conf)
                            print("environment set to: PRODUCTION")
                    elif (
                        global_configuration["DEFAULT"]["ActiveEnvironment"] != "LOCAL"
                    ):
                        global_configuration["DEFAULT"]["ActiveEnvironment"] = "LOCAL"
                        with open("configuration.ini", "w") as conf:
                            global_configuration.write(conf)
                        print("environment set to: LOCAL")
            except Exception as ex:
                print("failed to determine environment")
                print(ex)
            return func(*args, **kwargs)

        return wrapper

    def query(func):
        def wrapper(cnx):
            cursor = cnx.cursor()
            func(cursor)
            cursor.close()
            cnx.close()

        return wrapper
