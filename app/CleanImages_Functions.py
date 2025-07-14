
import cv2
import numpy as np


def equalHist(img):

    # Convertir a YCrCb
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Separar canales
    y, cr, cb = cv2.split(ycrcb)

    # Aplicar ecualización del histograma solo al canal Y (luminancia)
    y_eq = cv2.equalizeHist(y)

    # Recombinar canales
    ycrcb_eq = cv2.merge((y_eq, cr, cb))

    imagen_eq = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)

    return imagen_eq


def thresholdImg(img):

    # Separar en canales B, G, R
    b, g, r = cv2.split(img)

    # Aplicar umbral binario a cada canal
    _, binary_r = cv2.threshold(r, 15, 255, cv2.THRESH_TOZERO)
    _, binary_g = cv2.threshold(g, 15, 255, cv2.THRESH_TOZERO)
    _, binary_b = cv2.threshold(b, 15, 255, cv2.THRESH_TOZERO)

    # Unir los canales binarizados en una imagen RGB

    binary_color = cv2.merge([
        cv2.equalizeHist(binary_b),
        cv2.equalizeHist(binary_g),
        cv2.equalizeHist(binary_r)])

    return binary_color


def fourierTransform(img):

    b, g, r = cv2.split(img)

    # Aplicar FFT a cada canal
    def fft_channel(channel):
        f = np.fft.fft2(channel)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
        return magnitude_spectrum

    r_fft = fft_channel(r)
    g_fft = fft_channel(g)
    b_fft = fft_channel(b)

    fourier_img = cv2.merge([b_fft,g_fft,r_fft])

    return fourier_img