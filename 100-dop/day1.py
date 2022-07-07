def RandomNameGen():
    city = input("""
    Welcome to the Band Name Generator.
    What's the name of the City you grew up in?
    """)
    name = input("""
    What was the name of your first / favorite pet?
    """)
    print (f"""
    Your band name could be {city} {name}!
    """)

RandomNameGen()