import numpy as np
import os
import re
from sklearn.mixture import BayesianGaussianMixture
from scipy import stats
from skimage.filters import threshold_otsu
from visualisation.plot_methods import plot_bgmm_results
from adaptive_thresholding.data_processing import preprocess_data

def otsu(data):
    if data.size == 0:
        print('No positive data points found')
        return float('inf')
    return threshold_otsu(data)

def find_intersections(pdf1, pdf2, x):
    intersections = [x[i] for i in range(1, len(x)) if (pdf1[i] - pdf2[i]) * (pdf1[i - 1] - pdf2[i - 1]) < 0 and pdf1[i] != 0 and pdf2[i] != 0]
    return intersections

def BGMM(data, save_plot_path):
    component = 2
    if data.size == 0:
        print('No positive data points found')
        return float('inf')

    gamma = np.exp(-1 / component)
    gmm = BayesianGaussianMixture(n_components=component, max_iter=3000, weight_concentration_prior=gamma).fit(data.reshape(-1, 1))

    min_value, max_value = np.min(data), np.max(data)
    extension = 0.1 * (max_value - min_value)
    x = np.arange(min_value - extension, max_value + extension, 0.01).reshape(-1, 1)

    sum_pdf = np.zeros_like(x)
    pdfs = []
    chosen_intersection = None

    for i in range(component):
        pdf = gmm.weights_[i] * stats.norm.pdf(x, gmm.means_[i], np.sqrt(gmm.covariances_[i]))
        pdfs.append(pdf)
        sum_pdf += pdf

        if i > 0:
            intersections = find_intersections(pdfs[i], pdfs[i - 1], x)
            if intersections:
                mean1, mean2 = sorted([gmm.means_[i - 1], gmm.means_[i]].flatten())
                chosen_intersection = next((ix for ix in intersections if mean1 <= ix <= mean2), None)

            if chosen_intersection is None:
                chosen_intersection = fallback_threshold(gmm)

    if chosen_intersection is None:
        chosen_intersection = fallback_threshold(gmm)

    if save_plot_path:
        plot_bgmm_results(data, x, sum_pdf, pdfs, chosen_intersection, save_plot_path)

    return chosen_intersection

def fallback_threshold(gmm):
    component_index = np.argmax(gmm.weights_)
    mean = gmm.means_[component_index].item()
    std = np.sqrt(gmm.covariances_[component_index]).item()
    return mean + 3 * std

def adaptive_thresholding(data, marker_columns, output_folder, file_name):
    for marker_name in marker_columns:
        print(f'Processing marker: {marker_name}')
        marker_data = data[marker_name].to_numpy()
        sample_data = preprocess_data(marker_data)

        # Apply 2-phase thresholding with Otsu as the first phase and BGMM as the second
        foreground_mask = sample_data > otsu(sample_data)
        bpat_plot_name = re.sub(r'[^a-zA-Z0-9_-]', '_', marker_name)
        bpat_plot_path = os.path.join(output_folder, '2PT-BGMM', os.path.splitext(file_name)[0])
        os.makedirs(bpat_plot_path, exist_ok=True)
        bpat_plot_filepath = os.path.join(bpat_plot_path, bpat_plot_name)

        # Threshold the masked data using BGMM
        data[f'{marker_name}_BPAT'] = BGMM(sample_data[foreground_mask], bpat_plot_filepath)

    return data
