def cat_greeting(name: str, mood: str) -> str:
    """
    Return a playful cat-style greeting based on the user's name and mood.

    Args:
        name: The name to greet.
        mood: The mood of the greeting.

    Returns:
        A cat-themed greeting string.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(mood, str):
        raise TypeError("mood must be a string")

    clean_name = name.strip()
    clean_mood = mood.strip().lower()

    if not clean_name:
        raise ValueError("name must be a non-empty string")
    if not clean_mood:
        raise ValueError("mood must be a non-empty string")

    mood_messages = {
        "happy": f"Meow, {clean_name}! This sand cat is thrilled to see your happy paws today.",
        "sleepy": f"Purrr... hello, {clean_name}. This sand cat hopes you get a cozy nap soon.",
        "grumpy": f"Hiss... just kidding, {clean_name}. Even grumpy humans deserve a soft sand cat hello.",
        "excited": f"MROW! {clean_name}, your excitement is contagious.",
        "calm": f"Meow, {clean_name}. This sand cat approves of your calm and peaceful vibe today.",
    }

    if clean_mood not in mood_messages:
        raise ValueError("mood must be one of: happy, sleepy, grumpy, excited, calm")

    return mood_messages[clean_mood]


def cat_comfort(level: int = 1) -> str:
    """
    Return a comforting cat-style message based on the comfort level.

    Args:
        level: An integer comfort level from 1 to 5.

    Returns:
        A cat-themed comfort message.
    """
    # possible errors
    if not isinstance(level, int):
        raise TypeError("level must be an integer")

    if level < 1 or level > 5:
        raise ValueError("level must be between 1 and 5")

    # comfort messages
    comfort_messages = {
        1: "Purrr... this little sand cat wants to remind you that one small step is still progress.",
        2: "Purrr... it is okay to slow down for a moment. A calm mind can catch tricky bugs better.",
        3: "Purrr... everything will be okay. Take a short break, stretch a little, and come back with fresh eyes.",
        4: "Purrrr... you have already made it this far, so do not let this bug scare you. One careful paw-step at a time.",
        5: "PURRRR... developer emergency comfort activated. This sand cat strongly recommends water, a snack, and a tiny break before fighting the bug again. <3",
    }

    return comfort_messages[level]


def cat_fortune(weather: str, energy_level: int) -> str:
    """
    Return a playful cat-style fortune based on the weather and energy level.

    Args:
        weather     : Weather condition as a string.
        energy_level: An integer from 1 to 10.

    Returns:
        A cat-themed fortune string.
    """
    # possible errors
    if not isinstance(weather, str) or not weather.strip():
        raise ValueError("weather must be a non-empty string")

    if not isinstance(energy_level, int):
        raise TypeError("energy_level must be an integer")

    if energy_level < 1 or energy_level > 10:
        raise ValueError("energy_level must be between 1 and 10")

    # weather normalization
    init_weather = weather.strip().lower()
    weather_map = {
        "sunny" : "Sunny",
        "rainy" : "Rainy",
        "cloudy": "Cloudy",
        "snowy" : "Snowy",
        "windy" : "Windy",
    }

    if init_weather not in weather_map:
        raise ValueError("weather must be one of: sunny, rainy, cloudy, snowy, windy")

    weather_name = weather_map[init_weather]

    # weather messages
    weather_messages = {
        "Sunny" : "the warm sunbeams are inviting you to take a brave little leap today",
        "Rainy" : "even through the rain, a soft and lucky moment is still waiting for you",
        "Cloudy": "a gentle gray sky may bring you a calm and thoughtful kind of luck",
        "Snowy" : "a quiet snowy day is wrapping your fortune in extra softness and peace",
        "Windy" : "the lively wind may carry an unexpected little blessing to your paws",
    }

    # energy style
    if 1 <= energy_level <= 3:
        energy_style = "nap-friendly"
        intro        = "This is a nap-friendly cat fortune"
    elif 4 <= energy_level <= 7:
        energy_style = "cozy"
        intro        = "This is a cozy cat fortune"
    else:
        energy_style = "zoomie-powered"
        intro        = "This is a zoomie-powered cat fortune"

    return f"{intro} for a {weather_name} day: {weather_messages[weather_name]}"