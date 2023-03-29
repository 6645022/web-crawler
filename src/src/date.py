import arrow


class Date:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        split_value = value.split(' ')
        formatted_date = split_value[3] + ' ' + split_value[1][:2] + ' ' + split_value[4] + ' ' + split_value[5]
        utc_time = arrow.get(formatted_date, 'MMMM DD YYYY HH:mm:ss', tzinfo='utc')
        self._name = utc_time
