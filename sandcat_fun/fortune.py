def get_fortune(treats: int = 1) -> str:
    """
    The magical sand cat predicts your fortune. 
    The more treats (fish) you offer, the better your fortune might be!
    
    Args:
        treats (int): The number of treats given to the cat. Defaults to 1.
        
    Returns:
        str: A mystical developer fortune predicted by the sand cat.
        
    Raises:
        TypeError: If `treats` is not an integer.
    """
    # Input validation: Ensure treats is strictly an integer (booleans are a subclass of int in Python, so we exclude them)
    if not isinstance(treats, int) or isinstance(treats, bool):
        raise TypeError("Meow! The sand cat only accepts integers for treats!")

    # Determine fortune based on the number of treats
    if treats < 0:
        return "HISS! The Sand Cat deletes your production database! (Just kidding... but seriously, no negative treats allowed.)"
    elif treats == 0:
        return "The Sand Cat stares at your empty hands and judges your unformatted code. No treats, no fortune."
    elif 1 <= treats <= 3:
        return "Meow. The Sand Cat predicts a mild syntax error in your near future, but nothing a quick nap can't fix."
    elif 4 <= treats <= 9:
        return "Purrr! The Sand Cat is pleased. A bug you've been chasing for days will suddenly make sense today!"
    else:
        return "MROW! *happy tippy taps* The Sand Cat blesses your repository! Your code will compile flawlessly today, and all your PRs will be approved without comments!"