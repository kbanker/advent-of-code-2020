f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

needed_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_hcl_chars = [char for char in '0123456789abcdef']
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_passport(p):
    isValid = True

    fields = p.split(' ')
    field_names = [field[:3] for field in fields]

    for field in needed_fields:
        if field not in field_names:
            isValid = False

    if not isValid:
        return isValid

    fields = [field.split(':') for field in fields]

    for f in fields:
        field = f[0]
        value = f[-1]
        #print(f)

        if field == 'byr':
            if int(value) >= 1920 and int(value) <= 2002:
                continue
            else:
                return False

        elif field == 'iyr':
            if int(value) >= 2010 and int(value) <= 2020:
                continue
            else:
                return False

        elif field == 'eyr':
            if int(value) >= 2020 and int(value) <= 2030:
                continue
            else:
                return False

        elif field == 'hgt':
            #print(value[:-2])
            if value[-2:] == 'in':
                h = int(value[:-2])
                if h >= 59 and h <= 76:
                    continue
                else:
                    return False
            elif value[-2:] == 'cm':
                h = int(value[:-2])
                if h >= 150 and h <= 193:
                    continue
                else:
                    return False
            else:
                return False

        elif field == 'hcl':
            if value[0] == '#' and len(value) == 7:
                for l in value[1:]:
                    if l not in valid_hcl_chars:
                        return False
            else:
                return False

        elif field == 'ecl':
            if value in valid_ecl:
                continue
            else:
                return False

        elif field == 'pid':
            if len(value) == 9 and type(eval(value.strip('0'))) is int:
                continue
            else:
                return False

    return isValid


passports = []
cp = ''
for line in lines:
    if line == '':
        passports.append(cp.strip())
        cp = ''
    else:
        cp = cp + ' ' + line
passports.append(cp)

count = 0
for p in passports:
    if check_passport(p):
        count += 1
print(count)
#check_passport(cp)
