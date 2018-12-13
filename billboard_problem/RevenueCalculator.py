class RevenueCalculator:
    def __init__(self):
        self.dictionary = {}

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

    @staticmethod
    def max_revenue_tabulation(possible_positions, revenue, min_distance):
        """
        Find the maximum revenue by placing billboards on the highway
        with a minimum distance constraint. Uses a tabulation approach.
        :param possible_positions: an array with the possible billboard positions
        :param revenue: an array with the revenue for each possible billboard position
        :param min_distance: the distance constraint, no billboard can be placed within
        t miles or less than it
        :return: the maximum possible revenue
        """

        total_positions = len(possible_positions)
        total_miles = possible_positions[total_positions - 1]

        # Stores the maximum revenue for each mile
        max_rev = [0] * (total_miles + 1)
        # Billboard positions index
        next_position_index = 0

        for i in range(1, total_miles + 1):

            # Check if all billboards are already placed
            if next_position_index < total_positions:

                # If this mile isn't a billboard position, copy the
                # previous maximum revenue
                if possible_positions[next_position_index] != i:
                    max_rev[i] = max_rev[i - 1]

                # This mile is a billboard position
                else:
                    # In the first t miles we just compare the
                    # billboards between them and place just the
                    # one with the highest revenue
                    if i <= min_distance:
                        max_rev[i] = max(max_rev[i - 1], revenue[next_position_index])
                    # Check whether we must replace a previously placed
                    # billboard with a higher revenue one
                    else:
                        max_rev[i] = max(max_rev[i - min_distance - 1] + revenue[next_position_index],
                                         max_rev[i - 1])
                    next_position_index += 1

            else:
                max_rev[i] = max_rev[i - 1]

        return max_rev[total_miles]

    def max_revenue_memoization(self, possible_positions, revenue, min_distance):
        """
        Find the maximum revenue by placing billboards on the highway
        with a minimum distance constraint. Uses a memoization approach.
        :param possible_positions: an array with the possible billboard positions
        :param revenue: an array with the revenue for each possible billboard position
        :param min_distance: the distance constraint, no billboard can be placed within
        t miles or less than it
        :return: the maximum possible revenue
        """
        current_pos_key = tuple([min_distance] + possible_positions + revenue)

        if current_pos_key in self.dictionary:
            return self.dictionary[current_pos_key]

        else:
            # si tenemos un solo elemento, éste será el máximo revenue

            if len(possible_positions) == 1:
                self.dictionary[current_pos_key] = revenue[0]
                return self.dictionary[current_pos_key]

            # recorremos de arriba a abajo, tomamos última posición
            current_pos = possible_positions[len(possible_positions) - 1]
            # obtenemos el max revenue hasta ahora, (del elemento actual para abajo sin contar con el actual)
            current_max_rev = self.max_revenue_memoization(possible_positions[0:len(possible_positions) - 1],
                                                           revenue[0:len(revenue) - 1], min_distance)

            # en las posiciones comprendidas entre 0 y la distancia mínima solo puede haber 1 billboard
            if current_pos < min_distance:
                self.dictionary[current_pos_key] = max(revenue[len(revenue) - 1], current_max_rev)
                return self.dictionary[current_pos_key]

            previous_pos = possible_positions[len(possible_positions) - 2]

            # en caso de no cumplir con la distancia mínima decidimos si reemplazar billboards
            if current_pos - previous_pos <= min_distance:

                # será 0 por defecto, en caso de no tener otro punto previo al billboard anterior,
                # el previous_max_rev permanecerá en 0
                previous_max_rev = 0
                # max_rev previo a la colocación del billboard anterior, si no hay no entra en el bucle
                # quedando el previous_max_rev en 0
                for i in range(2, len(possible_positions)):
                    previous_pos = possible_positions[len(possible_positions) - i - 1]
                    # el punto de comparación previo al billboard anterior debe ser un punto más allá de la
                    # distancia mínima
                    if current_pos - previous_pos > min_distance:
                        previous_max_rev = \
                            self.max_revenue_memoization(possible_positions[0:len(possible_positions) - i],
                                                         revenue[0:len(revenue) - i], min_distance)
                        break

                # Reemplazamos billboard si el nuevo da mejor revenue
                # Si no, no colocamos el billboard actual y mantenemos el antiguo
                self.dictionary[current_pos_key] = max(previous_max_rev + revenue[len(revenue) - 1], current_max_rev)

                return self.dictionary[current_pos_key]
            # si cumple con la distancia simplemente lo colocamos
            self.dictionary[current_pos_key] = current_max_rev + revenue[len(revenue) - 1]

            return self.dictionary[current_pos_key]
