KEY_WORDS = ["plus", "minus", ["multiplied", "by"], ["divided", "by"]]

def answer(question):
    question = question.replace("What is ", "").replace(
        "?", "").replace("plus", "+").replace("minus", "-").replace("divided by", "/").replace("multiplied by", "*").split(" ")
    question.insert(0, "(")
    question.insert(4, ")")

    q = [x.isalpha() for x in question if x not in ("What", "is")] 
    if any(q):
        raise ValueError("unknown operation")

    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")


def main():
    o = answer("What is -3 plus 7 multiplied by -2?")
    print(o)


if __name__ == "__main__":
    main()