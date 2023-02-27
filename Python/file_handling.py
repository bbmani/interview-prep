# Normal but not a good practise of handling the files
# Opening the file in explicit read mode
f = open("Python\\test_text.txt", "r")
print(f"The file name is {f.name}")
f.close()
'''
    the problem with the above code is that we might forget to close the file, which might overflow with the file memory descriptors, so the best practise to open a file is like below. It automatically closes the file after it comes out of the block. it is called context manager
'''
with open("Python\\test_text.txt", "r") as f:
    
    ''' Perfectly viable way to get the contents. But what if the contents are larger and we dont want to dump everything into memory?'''
    
    # f_contents = f.read()
    # print(f_contents)
    
    # Use read lines
    # print("Another way to read the file...")
    # f_contents_new = f.readlines()
    # print(f_contents_new)
    
    # Another way to read the file
    # for line in f:
    #     print(line, end="")
    
    # Character count can be passed out as an argument
    # file_contents = f.read(50)
    # print(file_contents)
    
    # file_contents = f.read(50)
    # print(file_contents)
    
    # read returns an empty string when no characters are available
    
    # Actual way of handling files
    size_to_read = 20
    file_contents = f.read(size_to_read)
    print(file_contents)
    
    print(f"The current location in the file now is {f.tell()}")
    print("Currently seeking to 23rd position in the file and reading the contents")
    
    f.seek(23)
    file_contents = f.read(size_to_read)
    print(file_contents)
    
    # while len(file_contents) > 0:
    #     print(file_contents,end="--")
    #     file_contents = f.read(size_to_read)
# print("Is the file F closed? : {}".format(f.closed))
''' File will be created if it doesnt exist, if not it will overwrite the file'''
with open("Python\\test_text.txt", "r") as rf:
    with open("Python\\test_text_copy.txt", "w") as wf:
        size_to_read = 10
        rf_contents = rf.read(size_to_read)
        
        while len(rf_contents) > 0:
            wf.write(rf_contents)
            rf_contents = rf.read(size_to_read)
        
        wf.write("\nFinally Written")
