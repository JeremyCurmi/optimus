from commands import return_command_type_if_given_command


def test_return_command_type_if_given_command():
    is_voice_command = True
    test_cases = [{'var': '$new$reminder',
                   'expected': (not is_voice_command, '$new')},
                  {'var': 'Hey man this is a test',
                   'expected': None},
                  {'var': 'Hey @optimus, command update ...',
                   'expected': (is_voice_command, '$update')}]
    for test in test_cases:
        got = return_command_type_if_given_command(test['var'])
        expected = test['expected']
        assert got == expected
