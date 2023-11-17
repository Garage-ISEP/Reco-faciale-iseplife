import cv2

# Chargez le fichier XML du classificateur de visage Haar
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Chargez l'image sur laquelle vous souhaitez détecter les visages
image = cv2.imread('photos_test/test.jpg')

# Convertissez l'image en niveaux de gris pour la détection de visage
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Utilisez le classificateur de visage pour détecter les visages dans l'image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dessine un rectangle autour du visage

# Enregistrez l'image modifiée avec les rectangles dessinés
cv2.imwrite('test_rect.jpg', image)

# Affichez l'image avec les rectangles (optionnel)
cv2.imshow('Image avec rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

