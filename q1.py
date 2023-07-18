def create_movie_list(input_file, delimiter, keys, null_value, title_id, information):
    x = 5
    results = list()
    memo = set()
    with open(input_file, 'r', encoding=None) as f:
        lines = f.readlines()
    for line in lines[1:]:
        parts = line.strip().split(delimiter)
        info_dict = dict()
        if parts[0] not in memo:
            memo.add(parts[0])
            if x != 5:
                results.append(d_line)
            x = 3
            d_line = dict()
            d_line[title_id] = parts[0]
            d_line[information] = []
            for i in range(len(keys)):
                j = i + 2
                if parts[j] != null_value:
                    info_dict[keys[i]] = parts[j]
            if parts[1] == '1':
                d_line['original_title'] = parts[2]
            d_line[information].append(info_dict)
        else:
            for i in range(len(keys)):
                j = i + 2
                if parts[j] != null_value:
                    info_dict[keys[i]] = parts[j]
            d_line[information].append(info_dict)
            if parts[1] == '1':
                d_line['original_title'] = parts[2]
    if x != 5:
        results.append(d_line)
    return results
input_file = '/Users/erenbardak/msds501_computation_2023_eren/2ndHW/Assigned/imdb_titles_medium.tsv'
delimiter = '\t'
keys = ['title', 'region', 'language', 'types']
null_value = '\\N'
title_id = 'id'
information = 'info'
movie_list = create_movie_list(input_file, delimiter, keys, null_value, title_id, information)
print(movie_list)

def return_title_id_original_title_dict(movie_list, title_id):
    original_title_dict= {}
    for movie in movie_list:
        if 'original_title' in movie and title_id in movie:
            original_title_dict[title_id]=movie['original_title']

    return  original_title_dict


def return_information_element_set(**kargs):

    movie_list = kargs['movie_list']
    key = kargs['key']
    unique_info_set={}
    information ='information'
    for movie in movie_list:
        if information in movie:
            for info_dict in movie[information]:
                if key in info_dict:
                    unique_info_set.add(info_dict[key])
    print(unique_info_set)                
    return unique_info_set  