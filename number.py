import copy


# x座標,y座標,数字のデータを格納するためのクラス
class Number:
    x = 0
    y = 0
    data = 0
    # possibility[0]は使用しない
    possibility = []

    def __init__(self, x: int, y: int, data: int = 0):
        self.x = x
        self.y = y
        self.data = data
        self.possibility = [True] * 10

    def __str__(self):
        return str(self.data)

    def iscollect(self):
        cnt = 0
        tmp = 0
        for i in range(9):
            if self.possibility[i + 1]:
                tmp = i + 1
                cnt += 1
                if cnt > 1:
                    return 0
        if cnt == 1:
            return tmp
        else:
            return 0

    def isset(self):
        return self.data == 0

    def isposs(self, data: int):
        return self.possibility[data]

    def set_data(self, data: int):
        self.data = data
        self.possibility = [False] * 10

    def set_false(self, t: int):
        self.possibility[t] = False


# xが縦、yが横
class Number_data:
    def __init__(self):
        self.data = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.data[i][j] = Number(i, j)

    """
    def p(self):
        print(self.data)
    """

    def get_data(self, x: int, y: int) -> Number:
        return self.data[x][y]

    def set_data(self, x: int, y: int, data: int):
        self.data[x][y].set_data(data)


# 9つのデータ(縦、横、9マス)内に対して、それぞれの数字が何個可能性があるのかを保持　縦
class Group_ver:
    def __init__(self, v: int):
        self.possibility = [False] * 10
        self.v = v

    def iscollect(self, num_data: Number_data, data: int) -> bool:
        cnt = 0
        for i in range(9):
            if num_data.get_data(i, self.v).isposs(data):
                cnt += 1
        # print(cnt)
        if cnt == 0:
            # print(str(data) + " is finished.")
            return False
        elif cnt == 1:
            # print(str(data) + " is not finished.")
            return True
        else:
            return False

    def set_data(self, num_data: Number_data, data: int):
        for i in range(9):
            if num_data.get_data(i, self.v).isposs(data):
                # num_data.get_data(i, self.v).set_data(data)
                # return
                return [i, self.v]

    def delete_poss(self, num_data: Number_data, t: int):
        if self.possibility[t]:
            return True
        for i in range(9):
            num_data.get_data(i, self.v).set_false(t)
        self.possibility[t] = True
        return False
        # num_data.get_data(1, self.v).set_false(t)

    def judge(self, num_data: Number_data):
        for i in range(9):
            if self.iscollect(num_data, i + 1):
                self.set_data(num_data, i + 1)


# 9つのデータ(縦、横、9マス)内に対して、それぞれの数字が何個可能性があるのかを保持　横
class Group_hol:
    def __init__(self, v: int):
        self.possibility = [False] * 10
        self.v = v

    def iscollect(self, num_data: Number_data, data: int) -> bool:
        cnt = 0
        for i in range(9):
            if num_data.get_data(self.v, i).isposs(data):
                cnt += 1
        # print(cnt)
        if cnt == 0:
            # print(str(data) + " is finished.")
            return False
        elif cnt == 1:
            # print(str(data) + " is not finished.")
            return True
        else:
            return False

    def set_data(self, num_data: Number_data, data: int):
        for i in range(9):
            if num_data.get_data(self.v, i).isposs(data):
                # num_data.get_data(self.v, i).set_data(data)
                # return
                return [self.v, i]

    def delete_poss(self, num_data: Number_data, t: int):
        if self.possibility[t]:
            return True
        for i in range(9):
            num_data.get_data(self.v, i).set_false(t)
        self.possibility[t] = True
        return False
        # num_data.get_data(1, self.v).set_false(t)

    def judge(self, num_data: Number_data):
        for i in range(9):
            if self.iscollect(num_data, i + 1):
                self.set_data(num_data, i + 1)


# 9つのデータ(縦、横、9マス)内に対して、それぞれの数字が何個可能性があるのかを保持　正方形
class Group_sq:
    def __init__(self, h: int, w: int):
        self.possibility = [False] * 10
        self.h = h
        self.w = w

    def iscollect(self, num_data: Number_data, data: int) -> bool:
        cnt = 0
        for i in range(9):
            tmp1 = i // 3 + self.h * 3
            tmp2 = i % 3 + self.w * 3

            if num_data.get_data(tmp1, tmp2).isposs(data):
                cnt += 1
        # print(cnt)
        if cnt == 0:
            # print(str(data) + " is finished.")
            return False
        elif cnt == 1:
            # print(str(data) + " is not finished.")
            return True
        else:
            return False

    def set_data(self, num_data: Number_data, data: int):
        for i in range(9):
            tmp1 = i // 3 + self.h * 3
            tmp2 = i % 3 + self.w * 3
            if num_data.get_data(tmp1, tmp2).isposs(data):
                # num_data.get_data(tmp1, tmp2).set_data(data)
                # return
                return [tmp1, tmp2]

    def delete_poss(self, num_data: Number_data, t: int):
        if self.possibility[t]:
            return True
        for i in range(9):
            tmp1 = i // 3 + self.h * 3
            tmp2 = i % 3 + self.w * 3
            num_data.get_data(tmp1, tmp2).set_false(t)
        self.possibility[t] = True
        return False
        # num_data.get_data(1, self.v).set_false(t)

    def judge(self, num_data: Number_data):
        for i in range(9):
            if self.iscollect(num_data, i + 1):
                self.set_data(num_data, i + 1)


class suudoku:
    def __init__(self):
        self.num_data = Number_data()
        self.g_v = []
        self.g_h = []
        self.g_s = [[0] * 3 for i in range(3)]
        self.wrong = False
        for i in range(9):
            self.g_v.append(Group_ver(i))
            self.g_h.append(Group_hol(i))
        for i in range(3):
            for j in range(3):
                self.g_s[i][j] = Group_sq(i, j)

    def set_data(self, x: int, y: int, data: int):
        self.num_data.set_data(x, y, data)
        if self.g_v[y].delete_poss(self.num_data, data):
            self.wrong = True
        if self.g_h[x].delete_poss(self.num_data, data):
            self.wrong = True
        if self.g_s[x // 3][y // 3].delete_poss(self.num_data, data):
            self.wrong = True

    def P(self):
        for i in range(9):
            for j in range(9):
                # print(self.num_data.get_data(i, j).possibility[3], end=" ")
                # print("(" + str(self.num_data.get_data(i, j)) + ")", end=" ")
                print(self.num_data.get_data(i, j), end=" ")
            print('')

    def data_input(self) -> bool:
        is_change = True
        for k in range(9):
            if self.wrong:
                break
            for i in range(9):
                if self.g_v[i].iscollect(self.num_data, k + 1):
                    is_change = False
                    tmp = self.g_v[i].set_data(self.num_data, k + 1)
                    self.set_data(tmp[0], tmp[1], k + 1)
            if self.wrong:
                break
            for i in range(9):
                if self.g_h[i].iscollect(self.num_data, k + 1):
                    is_change = False
                    tmp = self.g_h[i].set_data(self.num_data, k + 1)
                    self.set_data(tmp[0], tmp[1], k + 1)
            if self.wrong:
                break
            for i in range(3):
                for j in range(3):
                    if self.g_s[i][j].iscollect(self.num_data, k + 1):
                        is_change = False
                        tmp = self.g_s[i][j].set_data(self.num_data, k + 1)
                        self.set_data(tmp[0], tmp[1], k + 1)

        for i in range(9):
            if self.wrong:
                break
            for j in range(9):
                tmp = self.num_data.get_data(i, j).iscollect()
                if tmp:
                    is_change = False
                    self.set_data(i, j, tmp)
        return is_change

    def make_copy(self, xx):
        self.num_data = xx.num_data
        self.g_v = xx.g_v
        self.g_h = xx.g_h
        self.g_s = xx.g_s
        # self.wrong = False

    def solve(self):
        while True:
            # self.P()
            # print("--------------------------------")
            if self.data_input():
                break
            if self.wrong:
                return False
        tmpx = 0
        tmpy = 0
        while not self.num_data.get_data(tmpx, tmpy).isset():
            tmpx += 1
            if tmpy > 8 and tmpx > 8:
                return True
            elif tmpx > 8:
                tmpy += 1
                tmpx = 0
                if tmpy > 8:
                    # print("this is answer")
                    return True
        # print(tmpx)
        # print(tmpy)
        for i in range(9):
            if self.num_data.get_data(tmpx, tmpy).isposs(i + 1):
                xx = copy.deepcopy(self)
                xx.set_data(tmpx, tmpy, i + 1)
                # print(str(tmpx) + "," + str(tmpy) + "," + str(i+1) + " is set")
                # xx.P()
                # print("--------------------------------")
                if xx.solve():
                    self.make_copy(xx)
                    return True
                else:
                    continue
        # print("i can't find any number")
        return False


if __name__ == '__main__':
    S = suudoku()
    """
    for i in range(8):
        S.set_data(5, i, i + 1)
    """
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        S.set_data(a, b, c)
    """
    for i in range(5):
        S.data_input()
    """
    S.solve()
    S.P()
