from skimage.io import imread
from skimage import color
from skimage.filters import threshold_otsu, gaussian
from skimage.transform import resize
from skimage import measure
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler


class ECG:

    # ---------------- IMAGE LOAD ----------------
    def getImage(self, image):
        return imread(image)

    # ---------------- GRAYSCALE ----------------
    def GrayImgae(self, image):
        image_gray = color.rgb2gray(image)
        image_gray = resize(image_gray, (1572, 2213))
        return image_gray

    # ---------------- LEAD DIVISION ----------------
    def DividingLeads(self, image):

        Leads = [
            image[300:600, 150:643],
            image[300:600, 646:1135],
            image[300:600, 1140:1625],
            image[300:600, 1630:2125],
            image[600:900, 150:643],
            image[600:900, 646:1135],
            image[600:900, 1140:1625],
            image[600:900, 1630:2125],
            image[900:1200, 150:643],
            image[900:1200, 646:1135],
            image[900:1200, 1140:1625],
            image[900:1200, 1630:2125],
        ]

        return Leads

    # ---------------- PREPROCESS ----------------
    def preprocess(self, img):
        gray = color.rgb2gray(img)
        blur = gaussian(gray, sigma=1)
        thresh = threshold_otsu(blur)
        binary = blur < thresh
        binary = resize(binary, (300, 450))
        return binary

    # ---------------- SIGNAL EXTRACTION ----------------
    def extract_signal(self, lead_img):

        binary = self.preprocess(lead_img)

        contours = measure.find_contours(binary, 0.8)

        if len(contours) == 0:
            return np.zeros(255)

        # Take largest contour
        contour = max(contours, key=lambda x: x.shape[0])

        # Resize to fixed length
        contour = resize(contour, (255, 2))

        signal = contour[:, 0]

        # Normalize
        scaler = MinMaxScaler()
        signal = scaler.fit_transform(signal.reshape(-1, 1)).flatten()

        return signal

    # ---------------- COMBINE 1D SIGNAL ----------------
    def CombineConvert1Dsignal(self, Leads):

        signals = []

        for lead in Leads:
            sig = self.extract_signal(lead)
            signals.append(sig)

        final_signal = np.concatenate(signals)   # 🔥 NO CSV

        final_signal = final_signal.reshape(1, -1)

        return final_signal

    # ---------------- PCA ----------------
    def DimensionalReduciton(self, signal):

        pca = joblib.load('Models/PCA_ECG.pkl')
        reduced = pca.transform(signal)

        return reduced

    # ---------------- PREDICTION + CONFIDENCE ----------------
    def ModelLoad_predict(self, final_df):

        model = joblib.load('Models/Heart_Prediction_using_ECG.pkl')

        prediction = model.predict(final_df)
        probabilities = model.predict_proba(final_df)

        confidence = np.max(probabilities)

        labels = {
            0: "Abnormal Heartbeat",
            1: "Myocardial Infarction",
            2: "Normal",
            3: "History of MI"
        }

        return labels.get(prediction[0], "Unknown"), confidence