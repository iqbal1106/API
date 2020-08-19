import os


#def soldier("C://", "JPMC.doc","")

import os
def soldier(path, format):
    os.chdir(path)
    i = 0

    files = os.listdir(path)

    with open("hafsa.txt", "w") as filehandle:

        for file in files:
            fileCapitalized=file.capitalize()
            i=i+1
            filehandle.writelines("%s\n" %fileCapitalized)
        filehandle.writelines("total files are:" + str(i))
        # here we have to come out of the for loop so that we can perform another function
        #otherwise it will not allow.

    with open("sarah.txt", "w" ) as filehandle:
        for file in files:
            print(os.path.splitext(file)[1])

            if os.path.splitext(file)[1] == ".jpg":

                filehandle.writelines("\n" + file)


soldier(r"C:\Users\Iqbal\Desktop", ".jpg")


#
# import os
# def soldier(path, file, format)
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}{format}")
#             i +=1

# import requests
#
# r=requests.get("https://www.youtube.com/watch?v=u6_aYV-1LAE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=82")
# print(r.text
#       )