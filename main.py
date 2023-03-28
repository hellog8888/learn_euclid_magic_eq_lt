class Track:
    def __init__(self, start_x, start_y):
        self._start_x = start_x
        self._start_y = start_y
        self.lst_track_line = []

    def add_track(self, tr):
        self.lst_track_line.append(tr)

    def get_tracks(self):
        return tuple(self.lst_track_line)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        len_1 = ((self._start_x - self.lst_track_line[0].x) ** 2 + (self._start_y - self.lst_track_line[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_lenth(i) for i in range(1, len(self.lst_track_line))))

    def __get_lenth(self, i):
        return ((self.lst_track_line[i - 1].x - self.lst_track_line[i].x) ** 2 + (self.lst_track_line[i - 1].y - self.lst_track_line[i].y) ** 2) ** 0.5


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y