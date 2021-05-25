def strategy(history, memory):
    """
    use titFotTat for first 8 turns
    Always cooperate if cooporation has occurred at least 6 times in first 8 turns
    """
    choice = 1
    if history.shape[1] > 0 and history.shape[1] < 8:
        choice = history[1,-1]
        
    elif history.shape[1] == 8:
        memory = sum(history[1]) > 5
    elif history.shape[1] > 8:
        choice = memory
    return choice, memory
