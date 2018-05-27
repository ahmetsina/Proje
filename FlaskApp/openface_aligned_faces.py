import dlib, sys, cv2,os
import numpy as np
import openface



# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

# Take the image file name from the command line
file_name = sys.argv[1]

# Create a HOG face detector using the built-in dlib class




def crop_face(img):
    file_name = img # sys.argv[1]
    predictor_model = "FeatureExtraction/shape_predictor_68_face_landmarks.dat"
    face_detector = dlib.get_frontal_face_detector()
    face_pose_predictor = dlib.shape_predictor(predictor_model)
    face_aligner = openface.AlignDlib(predictor_model)
    # Load the image
    image = cv2.imread(file_name)

    # Run the HOG face detector on the image data
    detected_faces = face_detector(image, 1)
    print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

    # Loop through each face we found in the image
    for i, face_rect in enumerate(detected_faces):

        # Detected faces are returned as an object with the coordinates
        # of the top, left, right and bottom edges
        print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))
        face_rect = dlib.rectangle(face_rect.left()-20, face_rect.top()-20, face_rect.right()+20, face_rect.bottom()+20)
        # Get the the face's pose
        pose_landmarks = face_pose_predictor(image, face_rect)
        # Use openface to calculate and perform the face alignment
        alignedFace = face_aligner.align(64, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE,landmarks=pose_landmarks)

        # Save the aligned image to a file
        fname, ext = os.path.splitext(file_name)
        print(fname + "_aligned_cropped.jpg")
        cv2.imwrite("{}_aligned_cropped.jpg".format(fname),alignedFace)
        cv2.waitKey(0)


dir_path = "FeatureExtraction/images/test_images"
directory = os.listdir(dir_path)
for file in directory:
    print(dir_path +"/" + file)
    print(os.getcwd())

    crop_face(dir_path +"/" + file)
