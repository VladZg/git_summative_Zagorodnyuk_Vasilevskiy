def sort_shaker(s):

    length = len(s)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):

        swapped = False

        for i in range(start_index, end_index):

            if (s[i] > s[i + 1]):
                s[i], s[i + 1] = s[i + 1], s[i]
                swapped = True

        if (not(swapped)):
            break

        swapped = False

        end_index = end_index - 1

        for i in range(end_index - 1, start_index - 1, -1):

            if (s[i] > s[i + 1]):
                s[i], s[i + 1] = s[i + 1], s[i]
                swapped = True

        start_index = start_index + 1

    return(s)
