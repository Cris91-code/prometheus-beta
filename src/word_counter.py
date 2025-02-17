def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    A word is defined as a sequence of characters separated by whitespace.
    
    Args:
        text (str): The input string to count words in.
    
    Returns:
        int: The number of words in the string.
    
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Spaces   around   words  ")
        3
        >>> count_words("")
        0
    """
    # If the input is None or an empty string, return 0
    if not text:
        return 0
    
    # Split the string by whitespace and filter out empty strings
    words = text.strip().split()
    
    return len(words)