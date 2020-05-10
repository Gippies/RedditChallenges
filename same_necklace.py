# https://old.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/


def same_necklace(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    for i in range(0, len(str_1)):
        new_str = ''
        for j in range(i, len(str_1) + i):
            new_str += str_1[j % len(str_1)]
        if str_2 == new_str:
            return True
    return False


if __name__ == '__main__':
    print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
    print(same_necklace("xxyyy", "xxxyy"))
