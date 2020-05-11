# https://old.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

alpha_list = 'abcdefghijklmnopqrstuvwxyz'
morse_list = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
alpha_morse_map = dict(zip(alpha_list, morse_list))


def morsify_str(alpha_str):
    return ''.join([alpha_morse_map[c] for c in alpha_str])


if __name__ == '__main__':
    print(morsify_str('sos'))
    print(morsify_str('helloworld'))
