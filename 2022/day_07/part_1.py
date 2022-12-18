file = 'input.txt'

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    if keys[-1] in list(dic.keys()):
        dic[keys[-1]].update(value)
    else:
        dic[keys[-1]] = value

# create file structure dict
file_structure = {}

path = []
pwd = ''

# read file into file structure dict
for line in open(file):
    l = line.strip()
    if l[0] == '$':
        if l[2:4] == 'cd':
            pwd = l[5:]
            # make a new dir in pwd in file_structure
            if pwd != '..':
                path.append(pwd)
                nested_set(file_structure, path, value = {})
            else:
                last_loc = path.pop()
    else: 
        # add files to dirs (later I would regret using this structure)
        val, f = l.split(' ')
        if val != 'dir':
            val = int(val)
            nested_set(file_structure, path, {f :val})

dir_sizes = {}

def get_size(dir):
    size = 0
    for v in dir.values():
        if isinstance(v, dict):
            size += get_size(v)
        else:
            size += v

    return(size)

def get_dir_sizes(d, counter):
    for k, v in d.items():
        if isinstance(v, dict):
            # got stuck here for aages not realising dirs could have the same name
            # bodge (is just to add a loop number in front of each different dir
            # so they don't get wrongly updated / deleted)
            dir_sizes[''.join([str(counter), k])] = get_size(d[k])
            # add to recursion counter
            get_dir_sizes.count += 1
            counter = get_dir_sizes.count
            get_dir_sizes(v, counter)
    
    pass

# The R in IHR stands for 'I hate recursion'

get_dir_sizes.count = 0
get_dir_sizes(file_structure, counter = 0)

# get total size of all the small dirs
small_dirs_total_size = 0

for v in dir_sizes.values():
    if v <= 100000:
        small_dirs_total_size += v

print(small_dirs_total_size)