from typing import Optional


def taking_input()->Optional[str]:
    "Taking input from the user"    

    try:  
        query = input("What you want to ask : ").strip()
        if not query:
            raise ValueError("Your question is empty.")

    except ValueError as e:
        print(e)
        return None
    return query    