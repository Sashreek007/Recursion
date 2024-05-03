def isPalindrome(strng):
    if len(strng) <= 1:
        return True
    else:
        return strng[0] == strng[-1] and isPalindrome(strng[:-1])