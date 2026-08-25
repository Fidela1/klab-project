# src/utils.py

def normalise(values, minimum=None, maximum=None):
    """
    Scale a list of numbers into the 0-1 range.
    
    Parameters:
    -----------
    values : list of numbers
        The values to normalize
    minimum : float, optional
        Custom minimum value to use
    maximum : float, optional
        Custom maximum value to use
    
    Returns:
    --------
    list : Normalized values in [0, 1] range
    """
    if not values:
        return []
    
    lo = min(values) if minimum is None else minimum
    hi = max(values) if maximum is None else maximum
    span = hi - lo
    
    if span == 0:
        return [0.5 for _ in values]
    
    return [(v - lo) / span for v in values]


def summarise_scores(scores):
    """
    Create a summary dictionary from a list of scores.
    
    Parameters:
    -----------
    scores : list of numbers
        The scores to summarize
    
    Returns:
    --------
    dict : Contains count, mean, minimum, maximum, above_threshold
    """
    if not scores:
        return {
            'count': 0,
            'mean': 0,
            'minimum': 0,
            'maximum': 0,
            'above_threshold': 0
        }
    
    above = sum(1 for s in scores if s >= 0.8)
    
    return {
        'count': len(scores),
        'mean': sum(scores) / len(scores),
        'minimum': min(scores),
        'maximum': max(scores),
        'above_threshold': above
    }


def safe_divide(numerator, denominator, default=0.0):
    """
    Divide two numbers safely with error handling.
    
    Parameters:
    -----------
    numerator : any
        The number to be divided
    denominator : any
        The number to divide by
    default : float, optional
        Value to return when division fails
    
    Returns:
    --------
    float : Result of division or default value
    """
    try:
        num = float(numerator)
        den = float(denominator)
        
        if den == 0:
            return default
        
        return num / den
    
    except (TypeError, ValueError):
        return default