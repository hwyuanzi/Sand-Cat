def draw_cat(style: str = "sleeping") -> str:
    """
    Generates and returns various cute ASCII cat text arts depending on the style parameter.
    
    Args:
        style (str): The desired cat style. Valid options are "sleeping", "stretching",
                     "sitting", "playing", "coding", "ninja", and "loaf". Defaults to "sleeping".
                     
    Returns:
        str: The ASCII art of the sand cat.
    """
    # Normalize the input to make the function more robust
    style_normalized = style.strip().lower()

    if style_normalized == "sleeping":
        art = r"""
   |\___/|
   ( v_v ) zZz...
    \_^_/ 
   (_____)__
"""
    elif style_normalized == "stretching":
        art = r"""
   /\_/\      _
  ( o.o )____/ )
   > ^ <      /
  /  _  \____/
"""
    elif style_normalized == "sitting":
        art = r"""
   /\_/\
  ( ^.^ )
   > ^ <
  /  _  \
 / /| |\ \
(__(___)__)
"""
    elif style_normalized == "playing":
        art = r"""
   /\_/\
  ( ✧ω✧ )   o
   > ^ <   /
  /  _  \_/
"""
    elif style_normalized == "coding":
        art = r"""
   /\_/\
  ( @.@ )  [Bug]
   > ^ <   /
  / [___] \
"""
    elif style_normalized == "ninja":
        art = r"""
   /\_/\
  ( -_- )  ---*
   > ^ <
  /  _  \
"""
    elif style_normalized == "loaf":
        art = r"""
   /\_/\
  ( -.- )
  (_____)
"""
    else:
        # Fallback for invalid styles - a confused cat!
        art = f"""
   /\_/\  ?
  ( ?.? )/ 
   > ^ <  
  /  _  \ 
[Meow? Unknown style '{style}', here is a confused cat!]
"""
    
    # Strip the leading/trailing empty newlines for a cleaner output
    return art.strip('\n')