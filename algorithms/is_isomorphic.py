"""
    We need to determine whether two given strings, `first_string` and
    `second_string`,are isomorphic. Two strings are deemed isomorphic if
    the characters from`first_string` can be uniquely mapped to characters
    in `second_string`.This mapping should maintain the order of characters
    in both strings.
    It is essential that no two distinct characters from `first_string`
    can map to the same character in `second_string`, although
    a character can map to itself.

    For instance:
    - If `first_string = "egg"` and `second_string = "add"`, we observe that
    'e' can be mapped to 'a' and 'g' can be mapped to 'd', ensuring the
    integrity of the strings, resulting in a true output.
    - Conversely, in the scenario where
    `first_string = "foo"` and `second_string = "bar"`,
    we cannot find a valid isomorphic mapping, hence the output is false.
    - Finally, with `first_string = "paper"` and `second_string = "title"`,
    there exists a valid mapping where 'p' maps to 't', 'a' to 'i', and 'e'
    to 'l',indicating isomorphism between the strings,
    leading to a true output.

    To implement this logic, we can create a Python function that compares the characters
    of both strings and verifies if a valid mapping can be established.
    The function should return true if the strings are isomorphic and false otherwise.

"""


def is_isomorphic(f_str: str, s_str: str) -> bool:
    if len(f_str) != len(s_str):
        return False

    f_str_to_s_str_mapping = {}
    s_str_used = set()

    for i in range(len(f_str)):
        if f_str[i] not in f_str_to_s_str_mapping:
            if s_str[i] in s_str_used:
                return False
            f_str_to_s_str_mapping[f_str[i]] = s_str[i]
            s_str_used.add(s_str[i])
        else:
            if f_str_to_s_str_mapping[f_str[i]] != s_str[i]:
                return False

    return True
