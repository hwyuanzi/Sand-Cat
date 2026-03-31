def cat_reaction(event: str, intensity: int = 1) -> str:
    """
    Return a dramatic cat reaction to a common programming event.

    Args:
        event: The programming event to react to. Valid options are
               "bug_fixed", "code_review", "deploy", "merge_conflict",
               "friday", and "monday".
        intensity: How dramatic the reaction should be (1 to 3).
                   1 = mild, 2 = moderate, 3 = maximum drama.

    Returns:
        A cat-themed reaction string.

    Raises:
        ValueError: If event is empty, not a valid event string, or intensity
                    is outside 1-3.
        TypeError:  If intensity is not an integer.
    """
    if not isinstance(event, str) or not event.strip():
        raise ValueError("event must be a non-empty string")

    if not isinstance(intensity, int) or isinstance(intensity, bool):
        raise TypeError("intensity must be an integer")

    if intensity < 1 or intensity > 3:
        raise ValueError("intensity must be between 1 and 3")

    clean_event = event.strip().lower()

    reactions = {
        "bug_fixed": {
            1: "Meow. The sand cat nods approvingly. Bug squashed.",
            2: "Purrr! The sand cat does a little victory stretch! That bug never stood a chance!",
            3: "MROW!! *knocks things off desk in celebration* THE BUG IS GONE! LONG LIVE CLEAN CODE!",
        },
        "code_review": {
            1: "Meow. The sand cat glances at your PR and blinks slowly. Looks fine.",
            2: "Purrr... the sand cat carefully inspects each line. 'Needs more comments,' it whispers.",
            3: "HISS! The sand cat has OPINIONS about your variable names! Refactor immediately!",
        },
        "deploy": {
            1: "Meow. The sand cat watches the deploy with one eye open.",
            2: "Purrr... the sand cat crosses its paws for good luck. May the servers be stable!",
            3: "MROW!! *hides under desk* IS IT FRIDAY?! WHY ARE WE DEPLOYING?! ROLLBACK PLAN READY?!",
        },
        "merge_conflict": {
            1: "Meow. The sand cat sighs. Conflicts happen to the best of us.",
            2: "Hiss... the sand cat stares at the diff with growing concern. This is a mess.",
            3: "HISS!! *fur standing on end* WHO TOUCHED MY BRANCH?! THIS IS A CATASTROPHE!",
        },
        "friday": {
            1: "Meow. The sand cat yawns. Almost weekend nap time.",
            2: "Purrr! The sand cat is ready to close the laptop and curl up for the weekend!",
            3: "MROW!! *zooms around the office* FREEDOM! NO MORE JIRA TICKETS UNTIL MONDAY!",
        },
        "monday": {
            1: "Meow... the sand cat reluctantly opens one eye. Is it really Monday already?",
            2: "Hiss... the sand cat drags itself to the keyboard. Coffee. Need coffee.",
            3: "*dead cat pose* The sand cat refuses to acknowledge Monday's existence. System.exit(0).",
        },
    }

    if clean_event not in reactions:
        valid = ", ".join(sorted(reactions.keys()))
        raise ValueError(f"event must be one of: {valid}")

    return reactions[clean_event][intensity]
