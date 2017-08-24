def create_report(filename):
    '''
    Returns a dictionary of counts of: various characters, sentences and words
    '''
    count_dict = {'chars': 0, 'sentences': 0, 'words': 0}
    with open(filename) as file_handle:
        for line in file_handle:
            parse_line(line, count_dict)
    return count_dict

def parse_line(line, count_dict):
    '''
    Update count_dict with content of line
    Character count includes trailing whitepace.
    '''
    #update character count
    count_dict['chars'] += len(line) #'\n' end line Python 3 takes this into account

    #update sentences counts
    consistent_punct = handle_punct(line)
    count_dict['sentences'] += len(consistent_punct.split('.')) - 1

    #update word count_dict, will use split, works on all white space
    count_dict['words'] += len(line.split())

def handle_punct(line):
    '''
    Change ?, !, ... to a .
    '''
    no_question = line.replace('?', '.')
    no_exclam = no_question.replace('!', '.')
    no_ellipses = no_exclam.replace('...', '.')

    return no_ellipses

if __name__ == '__main__':
    filename = 'frankenstein_chpts_123.txt'
    print(create_report(filename))
