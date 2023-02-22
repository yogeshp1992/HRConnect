
class HandleCSV:
    file_name="employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.file_name,"r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.file_name) as bar:
            yield bar.readline()

    @classmethod
    def read_csv_line_by_line_(cls):
        with open(cls.file_name) as foo:
            for line_number, line in enumerate(foo.readlines()):
                if line_number >= 0:
                    yield line
                    line_number = line_number + 1
class_obj=HandleCSV()
a=class_obj.read_entire_csv()
#print(a)
b=class_obj.read_csv_line_by_line_()
itr_=iter(b)
print(type(itr_))
print(next(itr_))
print(next(itr_))
print(next(itr_))
print(next(itr_))
print(next(itr_))





