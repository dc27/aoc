
import functools

file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

@functools.cache
def calc(record, groups):

    # BASE CASE
    # no groups left?
    if not groups:
        # if there are no # left to place it's valid
        if "#" not in record:
            return 1
        # invalid permutation
        else:
            return 0
    
    # there are still groups left
    # if there are no records then the config is invalid
    if not record:
        return 0

    next_char = record[0]
    next_group = groups[0]

    def pound(record, next_group):
        """
        Treats first char as a pound (#)
        """

        # if the first is a pound, then the first n chars must
        # be able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # if the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0
        
        # if the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # valid!
                return 1
            else:
                # more groups ... invalid
                return 0
            
        # Make sure the character that follows this group can be a separator
        if record[next_group] in "?.":
            return calc(record[next_group+1:], groups[1:])

        return 0
    
    def dot():
        """
        Treats first char as a dot (.)
        """
        return calc(record[1:], groups)
    
    if next_char == "#":

        out = pound()

    elif next_char == ".":

        out = dot()

    elif next_char == "?":

        out = dot() + pound()

    else:
        raise RuntimeError


    print(record, groups, "-->", out)
    return out


def unfold(record, raw_groups):

    r_unfolded = (record + "?") * 5
    g_unfolded = (raw_groups + ",") * 5
    print(g_unfolded)

    groups = [int(i) for i in g_unfolded[0:-1].split(",")]
    return (r_unfolded[0:-1], groups)


output = 0

for line in input_stream:

    record, raw_groups = line.split()

    r, groups = unfold(record, raw_groups)

    output += calc(r, tuple(groups))

    print("~"*80)

print(">>>", output, "<<<")




