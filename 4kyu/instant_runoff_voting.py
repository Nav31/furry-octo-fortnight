# https://www.codewars.com/kata/instant-runoff-voting/train/python


def runoff(voters):
    """
    This is a function to determine the winner of an election.
    :param voters: <LIST> of <LIST> containg voter choice
    :return: Winner or None
    """

    result_dict, len_of_sub_arr = {}, len(voters[0]),
    total_votes = sum([x for x in range(1, len_of_sub_arr+1)]) * len(voters)
    cut_off = total_votes // 2

    for sub_arr in voters:
        for idx, candidate in enumerate(sub_arr):
            if candidate not in result_dict:
                result_dict[candidate] = len_of_sub_arr - idx
            else:
                result_dict[candidate] += len_of_sub_arr - idx

    min_list, max_list, counter = [], [], 0
    for key, val in result_dict.items():
        min_list = min_list or [[val, key]]
        max_list = max_list or [[val, key]]
        if counter > 0:
            if max_list[0] and val > max_list[0][0]:
                max_list = [[val, key]]
            elif val == max_list[0][0]:
                max_list.append([val, key])
            if val < min_list[0][0]:
                min_list = [[val, key]]
            elif val == min_list[0][0]:
                min_list.append([val, key])
        else:
            counter += 1

    if len(max_list) == 1 and max_list[0][0] > cut_off:
        return max_list[0][1]
    else:
        if min_list == max_list and len(min_list) > 1:
            return None
        else:
            new_voters = []
            new_min_list = [sub_arr[1] for sub_arr in min_list]
            for sub_arr in voters:
                new_voters.append([char for char in sub_arr if char not in new_min_list])
            print(new_voters)
            return runoff(new_voters)
    # Loop through voters populate dictionary with results
    # step 2: loop through the dictionary
    # if winner != "":
    #     return winner
    # else:
    #     result_dict = {}
    # # else recurse



# voters = [["dem", "ind", "rep"],
#           ["rep", "ind", "dem"],
#           ["ind", "dem", "rep"],
#           ["ind", "rep", "dem"]]

voters = [["a", "c", "d", "e", "b"],
         ["e", "b", "d", "c", "a"],
         ["d", "e", "c", "a", "b"],
         ["c", "e", "d", "b", "a"],
         ["b", "e", "a", "c", "d"]]
print(runoff(voters))