#in python muss immer explzit angegeben werden, was mit der datei gemacht werden darf (lesen oder schreiben)

with open("Lesson3-example-text.txt", "r") as sample_file_stream: #r... read modus, w... write modus; Für den file-stream muss ein name vergeben werden
    content = sample_file_stream.read()
    print(content)



with open("Lesson3-example-text.txt", "r") as sample_file_stream_two:
    content_two = sample_file_stream_two.read().splitlines() #splitlines() retourniert eine liste (eine zeile pro listen-element)

    for line in content_two:
        print(line)

with open("lesson3-txt-write.txt", "w") as sample_write_stream:
    sample_write_stream.write("Hallo, das ist ein test trallala")
