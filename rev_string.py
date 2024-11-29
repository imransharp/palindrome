def isPalindrome(val):
    for i in range(0, len(val)):
        if val[i] != val[len(val) - i - 1]:
            return False
        return True

# Main function
s = "sas"
ans = isPalindrome(s)
print(ans)
