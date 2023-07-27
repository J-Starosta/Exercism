def response(hey_bob):
    answer = ""
    if len(hey_bob.strip()) > 0:
        if hey_bob.isupper() and hey_bob.strip()[-1] == "?":
            answer = "Calm down, I know what I'm doing!"
        elif hey_bob.isupper():
            answer = "Whoa, chill out!"
        elif hey_bob.strip()[-1] == "?":
            answer = "Sure."
        else:
            answer = "Whatever."
    else:
        answer = "Fine. Be that way!"
    return answer
