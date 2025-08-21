def file_reader(path):
    try:
        with open(path, "r") as f:
            data = f.read()
            data_li = data.split(" ")
            dic = {}
            for word in data_li:
                if word not in dic.keys():
                    dic[word] = 1
                else:
                    dic[word] += 1

            freq_dic = dict(sorted(dic.items(), key= lambda x : x[1], reverse=True))
            return freq_dic

    except FileNotFoundError:
        return ("File not found, or Check your path.")

# print(file_reader(fr"D:\New folder\EV_Assigments\EV_Assessment\data.txt"))

def even_no(li):
    even_li = [x for x in li if x%2 == 0]
    even_li.sort()
    return even_li

li=[45,6,5,8,4,5,8,65,1,556,4]
# print(even_no(li))

def dic_student():
    student= {"Alice":85, "Bob": 92, "Charlie": 78, "David":90}
    student_li = list(sorted(student.items(), key=lambda x :x[1], reverse=True))
    print("Highest Score :-")
    print(f"Name : {student_li[0][0]}\nScore : {student_li[0][1]}")

dic_student()