class cts():
    def __init__(self,filename):
        self.read_file(filename)

    def read_file(self,filename):
        with open(filename) as f:
            # 读取规格
            line = f.readline()
            size = line[:-1].split(' ')
            # 读取原点坐标
            line = f.readline()
            source = line[7:-1].split(' ')
            # 读取sink个数
            line = f.readline()
            self.sinknum = line[9:-1].split(' ')
            self.sinknum = int(self.sinknum[0])
            # 读取sink
            for i in range(1, self.sinknum + 1):
                line = f.readline()
                line = line[:-1].split(' ')
                sink = Point(float(line[1]), float(line[2]), float(line[3]))
                sink.id = int(line[0])
                self.sink.append(sink)
                self.childpathlength = 0
            # 忽略
            for i in range(0, 9):
                line = f.readline()
            line = f.readline()
            self.blockagenum = int(line[13:-1])
            print(self.blockagenum)
            for i in range(0, self.blockagenum):
                line = f.readline()
                line = line[:-1].split(' ')
                blo = Blockage(float(line[0]), float(line[1]), float(line[2]), float(line[3]))
                self.blockage.append(blo)
        f.close()