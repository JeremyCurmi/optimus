import commands


def test_check_is_command():
    test_cases = [{'var': '$new$reminder', 'expected': True},
                  {'var': 'This is a test', 'expected': False},
                  {'var': '$this$isatest', 'expected': False},
                  {'var': 'Hey @optimus, command update', 'expected': True}]
    for test in test_cases:
        got = commands.check_is_command(test['var'])
        expected = test['expected']
        assert got == expected


def test_select_command_type():
    test_cases = [{'var': '$new$reminder', 'expected': (False, 'new')},
                  {'var': 'command delete', 'expected': (True, 'delete')},
                  {'var': '$update$greeting_term',
                      'expected': (False, 'update')},
                  {'var': 'Hey @optimus, command update', 'expected': (True, 'update')}]
    for test in test_cases:
        got = commands.select_command_type(test['var'])
        expected = test['expected']
        assert got == expected
