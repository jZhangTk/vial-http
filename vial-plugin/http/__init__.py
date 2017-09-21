import vial


def init():
    vial.register_command('VialHttp', '.plugin.http')
    vial.register_command('VialHttpBasicAuth', '.plugin.basic_auth_cmd', nargs='?')
    vial.register_function('VialHttpBasicAuth()', '.plugin.basic_auth_func')
