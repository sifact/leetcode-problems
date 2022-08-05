def numUniqueEmails(emails):
    seen = set()

    for email in emails:
        name, domain = email.split('@')
        local = name.split('+')[0].replace('.', '')
        seen.add(local + '@' + domain)

    return len(seen)


mails = []
for _ in range(int(input())):
    mails.append(input())

print(numUniqueEmails(mails))
