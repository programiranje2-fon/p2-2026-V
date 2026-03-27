# Zadatak 1
def concat_index_wise(l1, l2):
    # Option 1
    # l3 = []
    # for i in range(len(l1)):
    #     l3.append(l1[i] + l2[i])
    # return l3
    # Option 2
    # l3 = []
    # for i, j in zip(l1, l2):
    #     l3.append(i + j)
    # return l3
    # Option 3
    return [i + j for i, j in zip(l1, l2)]


# Zadatak 2
def digits_in_string(string):
    # Option 1
    # digits = []
    # for ch in string:
    #     if ch.isdigit(): digits.append(ch)
    # return digits
    # Option 2
    return [ch for ch in string if ch.isdigit()]


# Zadatak 3
def palindrom(text):
    text = [ch.lower() for ch in text if ch.isalnum()]
    # Option 1
    # midpoint = round(len(text)/2)
    # for i in range(midpoint):
    #     if text[i] != text[-(i+1)]:
    #         return False
    # return True
    # Option 2
    # midpoint = round(len(text)/2)
    # return all([text[i] == text[-(i+1)] for i in range(midpoint)])
    # Option 3
    # text_reversed = list(reversed(text))
    # return all(text[i] == text_reversed[i] for i in range(len(text)))
    # Option 4
    text_reversed = reversed(text)
    return all(ch == ch_rev for ch, ch_rev in zip(text, text_reversed))


# Zadatak 4

# 1. Najmanje 1 slovo između [a-z] tj. najmanje 1 malo slovo
# 2. Najmanje 1 broj između [0-9] tj. najmanje 1 cifra
# 3. Najmanje 1 slovo između [A-Z] tj. najmanje 1 veliko slovo
# 4. Najmanje 1 od sledećih znakova: $,#,@
# 5. Dužina u opsegu 6-12 (uključujući 6 i 12)

def passwords_check(passwords):
    passwords_list = [p.strip() for p in passwords.split(",")]
    valid_passwords = []
    # Option 1
    # for word in passwords_list:
    #     if len(word) < 6 or len(word) > 12:
    #         continue
    #     if not any([ch.islower() for ch in word]):
    #         continue
    #     if not any([ch.isdigit() for ch in word]):
    #         continue
    #     if not any([ch.isupper() for ch in word]):
    #         continue
    #     if not any(ch in "$#@" for ch in word):
    #         continue
    #     valid_passwords.append(word)
    # Option 2
    # for word in passwords_list:
    #     if len(word) < 6 or len(word) > 12:
    #         continue
    #     valid = [False]*4
    #     if any([ch.islower() for ch in word]): valid[0] = True
    #     if any([ch.isdigit() for ch in word]): valid[1] = True
    #     if any([ch.isupper() for ch in word]): valid[2] = True
    #     if any([ch in "$#@" for ch in word]): valid[3] = True
    #     if all(valid):
    #         valid_passwords.append(word)
    # Option 3
    for word in passwords_list:
        if len(word) < 6 or len(word) > 12:
            continue
        valid = [False]*4
        for ch in word:
            if ch.islower(): valid[0] = True
            elif ch.isdigit(): valid[1] = True
            elif ch.isupper(): valid[2] = True
            elif ch in "$#@": valid[3] = True
        if all(valid):
            valid_passwords.append(word)
    print("Valid passwords: " + ", ".join(valid_passwords))


# Zadatak 5
def server_status(state_log):
    log_lines = [line.strip() for line in state_log.split("\n") if line.strip() != ""]
    all_servers = []
    defect_servers = []
    for line in reversed(log_lines):
        _, s_name, _, s_state = line.split()
        if s_name not in all_servers:
            all_servers.append(s_name)
            if s_state == "down":
                defect_servers.append(s_name)

    print(f"Number of servers with logged state: {len(all_servers)}")
    print(f"Proportion of servers that are down: {len(defect_servers)/len(all_servers):.2f}")
    if len(defect_servers) > 0:
        print("Servers currently down: " + ", ".join(defect_servers))
    else:
        print("All servers are up and running!")


# Zadatak 6
def anagram(s1, s2):
    s1_clean = [ch.lower() for ch in s1 if ch.isalnum()]
    s2_clean = [ch.lower() for ch in s2 if ch.isalnum()]
    # Option 1
    # if len(s1_clean) != len(s2_clean):
    #     return False
    # return all([ch in s2_clean for ch in s1_clean])
    # Option 2
    s1_clean.sort()
    s2_clean.sort()
    return "".join(s1_clean) == "".join(s2_clean)


# Zadatak 7
def are_all_even(number):
    while number > 0:
        number, last_digit = divmod(number, 10)
        if last_digit % 2 != 0:
            return False
    return True

def all_even_digits():
    selection = []

    # Option 1
    # for num in range(100, 401):
    #     if all([digit in "02468" for digit in str(num)]):
    #         selection.append(num)

    # Option 2
    for num in range(100, 401):
        if are_all_even(num):
            selection.append(num)

    print(", ".join([str(num) for num in selection]))

    return selection


if __name__ == "__main__":

    # Zadatak 1
    # list1 = ["M", "na", "i", "Ke", "hi"]
    # list2 = ["y", "me", "s", "lly"]
    # print(concat_index_wise(list1, list2))


    # Zadatak 2
    # s1 = "Tokyo's 2024 population is now estimated at 37,115,035."
    # s2 = "Tokyo is one of the most populated cities."
    # print(digits_in_string(s1))
    # print(digits_in_string(s2))


    # Zadatak 3
    # s1 = "potop"
    # print(f"{s1}: {palindrom(s1)}")
    # s2 = "Sir ima miris"
    # print(f"{s2}: {palindrom(s2)}")
    # s3 = "ananas"
    # print(f"{s3}: {palindrom(s3)}")


    # Zadatak 4
    # passwords_to_check = "ABd1234@1, a F1#,2w3E*,2We334#5, t_456WR"
    # print(f"Passwords to check: {passwords_to_check}")
    # passwords_check(passwords_to_check)


    # Zadatak 5
    # server_state_log = '''
    #     Server abc01 is up
    #     Server abc02 is down
    #     Server abc03 is down
    #     Server xyz01 is up
    #     Server xyz02 is up
    #     Server abc02 is up
    #     Server abc01 is down
    #     '''
    # server_status(server_state_log)


    # Zadatak 6
    # print(anagram('ortoped', 'torpedo'))
    # print(anagram('ortopedi', 'torpedo'))
    # print(anagram('On sa tla Like', 'Nikola Tesla'))


    # Zadatak 7
    all_even_digits()
