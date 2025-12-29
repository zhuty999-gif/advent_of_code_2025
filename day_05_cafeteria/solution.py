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
