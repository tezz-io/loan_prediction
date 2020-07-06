import csv

class Main:
    def csv_r(self, string):
        data_set = open(string, 'r')
        data_list = []
        
        for line in data_set:
            data_list.append(line)

        new_data_list = []
        for line in data_list:
            l = line.split(',')
            new_data_list.append(l)
        
        return new_data_list

    def main(self):
        data_set = self.csv_r('data.csv')
        final_data_set = []
        for line in data_set:
            flag = 0
            for i in range(0, len(line)):
                if(line[i] == ''):
                    flag = 1
            if flag == 0:
                final_data_set.append(line)

        for line in final_data_set:
            if(line[-1] =='Y\n'):
                line[-1] = 'Y'
            else:
                line[-1] = 'N'

        print(len(data_set))
        print(len(final_data_set))

        
        with open("final.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(final_data_set)







main = Main()
main.main()