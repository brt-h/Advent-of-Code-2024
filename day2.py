def is_safe(row):
    """
    Determines if the list of levels is safe.
    A list is safe if it is strictly increasing or decreasing,
    with each adjacent pair differing by at least 1 and at most 3.
    """
    sorted_row = sorted(row)  # Copy of the row sorted in ascending order
    reverse_sorted_row = sorted(row, reverse=True)  # Copy sorted in descending order

    # check the diff of each element adj is not more than 3 or less than 1
    for i in range(1, len(row)):
        diff = abs(row[i] - row[i - 1])
        if not(1 <= diff <= 3):
            return False
    
    return row == sorted_row or row == reverse_sorted_row

def can_be_made_safe(levels):
    """
    Checks if removing exactly one element from the list makes it safe.
    """
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False

def count_safe_reports(reports):
    """
    Counts how many reports are safe either in their original form
    or by removing exactly one element.
    """
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe(levels) or can_be_made_safe(levels):
            safe_count += 1
    return safe_count

# Example usage:
if __name__ == "__main__":
    with open("day2tk.txt") as f:
        reports = f.readlines()
    print(count_safe_reports(reports))