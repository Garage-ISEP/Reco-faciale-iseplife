import face_recognition


# Charger les images et les encodages des visages (base de données)
image1 = face_recognition.load_image_file("test.jpg")

encoding=[]
for i in range(len(face_recognition.face_encodings(image1))):
    encoding.append(face_recognition.face_encodings(image1)[i])

image2 = face_recognition.load_image_file("test_ben.jpg")
ben = face_recognition.face_encodings(image2)[0]

# Comparer les encodages pour déterminer si les visages correspondent
for i in range(len(encoding)):
    result = face_recognition.compare_faces([encoding[i]], ben)

    if result[0]:
        print("Les visages correspondent.")
    else:
        print("Les visages ne correspondent pas.")