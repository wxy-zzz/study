class FenwickTree:

    def __init__(self, size:int):
        """
        Args:
            size (int): フェニック木として扱う配列のサイズ
        Raises:
            ValueError:
        """
        if size < 1:
            raise ValueError("wrong value: size")
        self._size = size
        self._data = [0] * size
        self._ft = [0] * size


    @property
    def size(self) -> int:
        """
        Returns:
            int: フェニック木の配列サイズ
        """
        return self._size


    @property
    def data(self) -> list[int]:
        """
        Returns:
            list[int]: フェニック木の配列
        """
        return self._data


    def add(self, i: int, x: int) -> None:
        """配列の i 番目の値に x を足す
        Args:
            i (int): 配列の index (0-index)
            x (int): p 番目の値に加算する値
        Raises:
            IndexError
        """
        if (i < 0) or (self.size <= i):
            raise IndexError("wrong index: i")

        self._data[i] += x
        i += 1  # i == 0 の場合ビット演算で操作できなくなるので +1 している
        while i <= self.size:
            self._ft[i - 1] += x
            i += i & (-i)


    def update(self, i: int , x: int) -> None:
        """配列の i 番目の値を x に書き換える
        Args:
            i (int): 配列の index (0-index)
            x (int): 書き換え先の値
        Raises:
            IndexError
        """
        if (i < 0) or (self.size <= i):
            raise IndexError("wrong index: i")
        self.add(i, x - self._data[i])


    def _sum(self, i: int) -> int:
        """index 0 から index i までの値の総和を求める。
        ただし、index i の値は含めない。

        Args:
            i (int)
        Raises:
            IndexError
        Returns:
            int: 0 から i までの総和
        """
        if (self.size < i):
            raise IndexError("wrong index: i")

        ret = 0
        while i > 0:
            ret += self._ft[i - 1]
            i -= i & -i
        return ret


    def sum(self, left: int, right: int) -> int:
        """index left から index right までの値の総和を求める。
        ただし、index right の値は含めない。

        Args:
            left (int)
            right (int)
        Raises:
            IndexError
        Returns:
            int: left から right までの総和
        """
        if (left < 0) or (right < left) or (self.size < right):
            raise IndexError("wrong index: left, right")
        return self._sum(right) - self._sum(left)
