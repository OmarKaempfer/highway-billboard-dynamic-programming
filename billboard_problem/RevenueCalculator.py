# Find maximum revenue by placing billboards on the highway
# with a minimum distance constraint


def max_revenue_tabulation(total_miles, possible_positions, revenue, min_distance):
    """
    Find the maximum revenue by placing billboards on the highway
    with a minimum distance constraint. Uses a tabulation approach.
    :param total_miles: the total number of miles
    :param possible_positions: an array with the possible billboard positions
    :param revenue: an array with the revenue for each possible billboard position
    :param min_distance: the distance constraint, no billboard can be placed within
    t miles or less than it
    :return: the maximum possible revenue
    """

    total_positions = len(possible_positions)

    # Stores the maximum revenue for each mile
    max_rev = [0]*(total_miles + 1)
    # Billboard positions index
    next_position_index = 0

    for i in range(1, total_miles + 1):

        # Check if all billboards are already placed
        if next_position_index < total_positions:

            # If this mile isn't a billboard position, copy the
            # previous maximum revenue
            if possible_positions[next_position_index] != i:
                max_rev[i] = max_rev[i-1]

            # This mile is a billboard position
            else:
                # In the first t miles we just compare the
                # billboards between them and place just the
                # one with the highest revenue
                if i <= min_distance:
                    max_rev[i] = max(max_rev[i-1], revenue[next_position_index])
                # Check whether we must replace a previously placed
                # billboard with a higher revenue one
                else:
                    max_rev[i] = max(max_rev[i - min_distance - 1] + revenue[next_position_index],
                                     max_rev[i-1])
                next_position_index += 1

        else:
            max_rev[i] = max_rev[i - 1]

    return max_rev[total_miles]
