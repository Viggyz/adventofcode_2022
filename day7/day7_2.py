import sys, re, pprint
sys.stdin = open('input.in', 'r')

TOTAL_SPACE = 70000000
TOTAL_REQUIRED = 30000000

file_struc = dict()
cur_loc = []
cur_dir = None

cmd_pattern = re.compile(r'^\$ (cd|ls)( \.\.| \w+| \/){0,1}$')
op_pattern = re.compile(r'^(dir|\d+){1} (\w+|\w+\.\w+)$')

dirs = []
total_sum = 0

def calc_size(dir_name):
    cur_dir = file_struc[dir_name]
    if cur_dir['full_size'] != 0:
        return cur_dir['full_size']
    elif len(cur_dir['dirs'])==0:
        cur_dir['full_size'] = cur_dir['files_size']
        return cur_dir['full_size']
    else:
        total_size = 0
        for dir in cur_dir['dirs']:
            total_size += calc_size(dir)
        cur_dir['full_size'] = total_size + cur_dir['files_size']
        return cur_dir['full_size']

try:
    while line:=input():
        if line_match:=cmd_pattern.search(line):
            cmd, loc = line_match.groups() 
            loc = loc.strip() if loc else loc
            if cmd=='ls':
                pass
            if cmd=='cd':
                if loc=='/':
                    cur_dir = '/'
                    cur_loc.append(cur_dir)
                    file_struc[cur_dir] = {
                        'files_size': 0,
                        'full_size': 0,
                        'dirs': [],
                        'files': [],
                    }
                    dirs.append(cur_dir)
                elif loc=='..':
                    cur_dir = cur_loc.pop()
                    if len(file_struc[cur_dir]['dirs'])==0:
                        file_struc[cur_dir]['full_size'] = file_struc[cur_dir]['files_size']
                else:
                    cur_dir = cur_loc[-1]+'/'+loc if cur_loc[-1]!='/' else cur_loc[-1]+loc
                    cur_loc.append(cur_dir)
                    file_struc[cur_dir] = {
                        'files_size': 0,
                        'full_size': 0,
                        'dirs': [],
                        'files': [],
                    }
                    dirs.append(cur_dir)
                print(cur_loc)
        elif line_match:=op_pattern.search(line):
            type_or_size, file_name = line_match.groups()
            if type_or_size == 'dir':
                file_struc[cur_dir]['dirs'].append(
                    cur_dir+"/"+file_name if cur_dir!='/' else cur_dir+file_name
                )
            else:
                file_struc[cur_dir]['files_size'] += int(type_or_size)
                file_struc[cur_dir]['files'].append(file_name)
        else:
            raise ValueError("Invalid line", line)
except EOFError:
    printer = pprint.PrettyPrinter()
    print("Pre-directory summation")
    # printer.pprint(file_struc)

    assert(len(set(dirs))==len(dirs), f"{len(set(dirs))}, {len(dirs)}")
    total_size = calc_size('/')
    remaining_space = TOTAL_SPACE - total_size
    remaining_required = TOTAL_REQUIRED - remaining_space
    min_required = total_size
    for dir_name in dirs:
        dir_size = file_struc[dir_name]['full_size']
        if dir_size > remaining_required and dir_size < min_required:
            min_required = dir_size
    print("Post-directory summation")
    printer.pprint(file_struc)
    print("Final space required")
    print(min_required)
