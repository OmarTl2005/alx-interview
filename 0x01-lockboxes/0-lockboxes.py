def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    if len(boxes) <= 1:
        return True
    if not isinstance(boxes, list):
        return False

    keys = [0]
    new_keys = set([0])

    while new_keys:
        current_keys = new_keys.copy()
        new_keys.clear()

        for key in current_keys:
            for box in boxes[key]:
                if box not in keys:
                    new_keys.add(box)
                    keys.append(box)

    return len(keys) == len(boxes)
