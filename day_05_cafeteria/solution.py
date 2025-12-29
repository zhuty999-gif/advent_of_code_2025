def load_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    parts = content.split('\n\n')
    
    ranges_raw = parts[0].splitlines()
    ranges = []
    for line in ranges_raw:
        start, end = map(int, line.split('-'))
        ranges.append(range(start, end + 1))
    
    ids_raw = parts[1].splitlines()
    ids = [int(line) for line in ids_raw]
    
    return ranges, ids



def is_id_fresh(id, ranges):
    """ Given an id and a list of ranges, find if the id is fresh. """
    return any(id in r for r in ranges)
    

def count_fresh_ids(ids, ranges):
    """ Given a list of ids and a list of ranges, count how many ids are fresh. """
    return sum(is_id_fresh(id, ranges) for id in ids)


def has_overlap(range_x, range_y):
    """ Checks if two ranges have any overlap. """
    if range_x[-1] in range_y or range_y[-1] in range_x:
        return True
    else:
        return False


def count_unique_fresh_ids_helper(ranges):
    """ Per prompt part II, this function counts the number of unique fresh ids given ids and ranges. 
        This function is a feeder function that gets feed into the recursion loop. """
    unique_ranges = []
    for r in ranges:
        if any([has_overlap(r, rr) for rr in unique_ranges]):
            for i in range(len(unique_ranges)):
                if has_overlap(r, unique_ranges[i]):
                    unique_ranges[i] = range(min(r[0], unique_ranges[i][0]), max(r[-1]+1, unique_ranges[i][-1]+1))
                    break
        else:
            unique_ranges.append(r)
    return unique_ranges



def count_unique_fresh_ids(ranges):
    """ Per prompt part II, this function counts the number of unique fresh ids given ids and ranges. """
    cur_zip = ranges
    next_step = count_unique_fresh_ids_helper(cur_zip)

    while cur_zip != next_step:
        cur_zip = next_step
        next_step = count_unique_fresh_ids_helper(cur_zip)

    count = sum([len(r) for r in cur_zip])
    return count