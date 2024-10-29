import matplotlib.pyplot as plt

def plot_bgmm_results(data, x, sum_pdf, pdfs, chosen_intersection, save_path):
    """
    Plot the results of the Bayesian Gaussian Mixture Model (BGMM) analysis.

    Parameters:
    data (array-like): Original data used in the BGMM analysis.
    x (array-like): Array of x values for plotting the PDFs.
    sum_pdf (array-like): Summed probability density function of all GMM components.
    pdfs (list of arrays): Individual PDFs of each GMM component.
    chosen_intersection (float): The calculated threshold value from the BGMM analysis.
    save_path (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
    plt.plot(x, sum_pdf, color='r', label='Summed PDF')

    # Plot individual PDFs
    for i, pdf in enumerate(pdfs):
        plt.plot(x, pdf, label=f'PDF Component {i+1}')

    plt.axvline(chosen_intersection, color='b', linestyle='--', label=f'Chosen Threshold: {chosen_intersection:.2f}')
    plt.title('Bayesian Gaussian Mixture Model Thresholding')
    plt.xlabel('Data Values')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.savefig(save_path)
    plt.close()
