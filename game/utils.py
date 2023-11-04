def draw_options(options:dict) -> str:
    '''Draw options.'''
    response = '\n'
    for option in list(options):
        response += f' {option} - {options[option]}\n'
    return response
