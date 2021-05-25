def strategy(history, memory):
    """
    Do the opposite of opponents previous move
    """
    choice = 1
    if history.shape[1] > 0:
        choice = not history[1,-1]
        
    return choice, memory