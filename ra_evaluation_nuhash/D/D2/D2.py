import os

def file_traverse(root_dir):
    file_list = os.listdir(root_dir)
    for i in file_list:
        if not i.endswith('.txt'):
            file_path = root_dir +"/"+str(i)
            file_traverse(file_path)
        else:
            print(root_dir+"/"+str(i))

        
if __name__ == "__main__":
    file_traverse('C:/Users/Nuhash/Desktop/NSL_Exam/Solves/DataStructure_Algorithm/D2/test')