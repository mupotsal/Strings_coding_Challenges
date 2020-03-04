def spell_bee(spelling, answer):
    count = 0
    sp_len = len(spelling)
    an_len = len(answer)

    if sp_len == an_len:
        for i in range (sp_len):
            if spelling[i] != answer[i]:
                count += 1
    elif sp_len < an_len:
        dif = an_len - sp_len
        for i in range (sp_len):
            if spelling[i] != answer[i]:
                count += 1
        count += dif

    else:
        if sp_len > an_len:
            dif = sp_len-an_len
            for i in range (an_len):
                if answer[i] != spelling[i]:
                    count += 1
            count += dif
            print(count)
    if count >= 3:
        return "NO"
    elif count ==0:
        return True
    elif 1<= count <=2:
        return "almost there"


print(spell_bee("liberty","libe"))